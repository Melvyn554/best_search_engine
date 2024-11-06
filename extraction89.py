import os
import re
import spacy
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np

nltk.download("stopwords")
nlp = spacy.load('fr_core_news_sm')

class SearchEngine:
    def __init__(self, path_documents_folder):
        self.stopwords = set(stopwords.words('french'))
        self.path = path_documents_folder
        self.documents = []
        self.document_names = []
        self.tfidf_matrix = None
        self.vectorizer = TfidfVectorizer()
        self.stemmer = SnowballStemmer("french")
        
    def __preprocess_document__(self, document):
        document = document.lower()
        doc = nlp(document)
        stemmed_tokens = [
            self.stemmer.stem(token.text) for token in doc 
            if token.text not in self.stopwords and not token.is_punct
        ]
        preprocessed_document = ' '.join(stemmed_tokens)
        return preprocessed_document

    def create_vector_space(self):
        for root, dirs, files in os.walk(self.path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    preprocessed_content = self.__preprocess_document__(content)
                    self.documents.append(preprocessed_content)
                    self.document_names.append(file_name)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def rechercher(self, query, coverage_weight=1.5):
        preprocessed_query = self.__preprocess_document__(query)
        query_vector = self.vectorizer.transform([preprocessed_query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        query_terms = set(preprocessed_query.split())
        term_idf = dict(zip(self.vectorizer.get_feature_names_out(), self.vectorizer.idf_))
        adjusted_similarities = []
        for idx, doc in enumerate(self.documents):
            doc_terms = set(doc.split())
            common_terms = query_terms.intersection(doc_terms)
            coverage_score = sum(term_idf.get(term, 0) for term in common_terms) / len(query_terms) * coverage_weight
            adjusted_similarity = cosine_similarities[idx] * coverage_score
            adjusted_similarities.append(adjusted_similarity)
        adjusted_similarities = np.array(adjusted_similarities)
        best_match_index = np.argmax(adjusted_similarities)
        best_similarity = adjusted_similarities[best_match_index]
        print(f"Meilleure similarité ajustée : {best_similarity}")
        return self.document_names[best_match_index]

if __name__ == "__main__":
    directory = 'wiki_split_extract_2k'
    search_engine = SearchEngine(directory)
    search_engine.create_vector_space()
    csv_path = 'Requete.csv'
    queries_df = pd.read_csv(csv_path)
    correct_matches = 0
    total_tests = len(queries_df)

    for index, row in queries_df.iterrows():
        query = row['Query']
        expected_file = row['Answer file']
        result_file = search_engine.rechercher(query)
        is_correct = result_file == expected_file
        status = "test validé" if is_correct else "test invalidé"
        print(f"Requête : {query}")
        print(f"Fichier attendu : {expected_file}")
        print(f"Fichier trouvé : {result_file}")
        print(f"Résultat : {status}\n")
        if is_correct:
            correct_matches += 1
    success_rate = (correct_matches / total_tests) * 100
    print(f"Taux de réussite : {success_rate:.2f}%")
