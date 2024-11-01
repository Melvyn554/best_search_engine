import os
import re
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk


parser = argparse.ArgumentParser(description="""The Best Search Engine: Research a wikipedia article, the closest within our database will be outputed.""")
parser.add_argument("--query", metavar="query", dest="query", 
                    required=True, action="store",
                    help="""Write your query. It can be multiple words.""")


Class Engine:
    def __init__(self, path_documents_folder):
        self.path = path_documents_folder
        #self.documents = ? Est-ce qu'on stock les documents ici ou est-ce qu'on parcourt le fichier donné quand nécessaire ?
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = set(stopwords.words('english'))

    """
    * Méthode pour tokeniser, retirer les stopwords et lemmatiser un document
    """
    def __preprocess_document__(document):
        # TODO: Compléter (utiliser word_tokenize, lemmatizer et stopwords)

    """
    * Méthode pour créer l'espace vectoriel du modèle TF-IDF
    """
    def create_vector_space():
        # TODO: Compléter (utiliser __preprocess_document__ et TfidfVectorizer)

    def rechercher(query):
        # TODO: Compléter (Preprocess la query, la transformer en tfidf, 
        #       calculer la distance (1 - cosine_similarity) avec tous les éléments de l'espace vectoriel,
        #       ne renvoyer que le document avec la plus courte distance)
        


# Fonction pour retirer la ponctuation et les majuscules d'un string
def remove_punctuation_and_caps(sentence):
    return sentence

# Fonction pour calculer le TF-IDF d'un document
def compute_tf_idf

# Fonction pour 

# Fonction pour rechercher un mot dans un fichier
def search_word_in_file(file_path, word):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if re.search(rf'\b{word}\b', content):  # \b pour chercher un mot entier
            print(f"Mot trouvé dans le fichier: {file_path}")

# Fonction pour parcourir un répertoire et chercher un mot dans tous les fichiers
def search_word_in_directory(directory, word):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                search_word_in_file(file_path, word)
            except Exception as e:
                print(f"Impossible d'ouvrir le fichier {file_path} : {e}")


if __name__ == "__main__":
    directory = 'wiki_split_extract_2k' 
    words = parser.parse_args().query
    search_word_in_directory(directory, words)
