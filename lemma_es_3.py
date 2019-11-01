# Spanish vesion
# Análisis de lemma
import spacy
from spacy.matcher import Matcher

nlp_es = spacy.load('es_core_news_sm')

doc_downcase_ok = nlp_es('amaba a los perros pero ahora amo más a los gatos.')
doc_uppercase_fails = nlp_es('Amaba a los perros pero ahora amo más a los gatos.')

for token in doc_downcase_ok:
  print('lemma_:', token.lemma_, '==== pos_: ', token.pos_, '==== text: ', token.text, 'dep_:', token.dep_)
  print('\n')
