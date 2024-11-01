# best_search_engine

L'idée de la méthode TF-IDF est de calculer le score TF-IDF d'un documents pour tous les mots qu'il contient sauf les plus courants, puis de créer une matrice avec pour dimensions, le nombre de documents et le nombre de mots lemmatisés uniques (pas de répétition) dans tous ces documents. En d'autres mots, chaque colonne de cette matrice correspond au vecteur d'un document.

Cela permet par la suite de créer un vecteur TF-IDF pour chaque requête et de le comparer avec les vecteurs de chaque document présent dans la matrice et d'ainsi trouver le document contenant des termes similaires

On utilisera: 
- TfidfVectorizer et cosine_similarity de sklearn
- stopwords, word_tokenize et WordNetLemmatizer de nltk

J'ai laissé ce qu'on avait déjà fait dans le fichier python pour le moment