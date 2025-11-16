import requests
import spacy

jane = requests.get("https://github.com/dustywhite7/Econ8320/raw/master/AssignmentData/janeEyreCh1to3.txt").text

nlp = spacy.load("en_core_web_sm")
doc = nlp(jane)

sentences = [i for i in doc.sents]

tokens = [token for token in sentences[1]]

