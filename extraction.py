import os
import re
import argparse

parser = argparse.ArgumentParser(description="""The Best Search Engine: Research a wikipedia article, the closest within our database will be outputed.""")
parser.add_argument("--query", metavar="query", dest="query", 
                    required=True, action="store",
                    help="""Write your query. It can be multiple words.""")

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

# Exemple d'utilisation
directory = 'wiki_split_extract_2k' 
words = parser.parse_args().query
search_word_in_directory(directory, words)
