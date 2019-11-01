# Spanish vesion
import spacy
from spacy.matcher import Matcher

nlp_es = spacy.load('es_core_news_sm')
matcher_es = Matcher(nlp_es.vocab)
pattern_es = [
  { 'LEMMA': 'amar', 'POS': 'VERB'},
  { 'POS': 'NOUN' }
]
matcher_es.add('LOVE_PATTERN', None, pattern_es)
doc_es = nlp_es('amaba a los perros pero ahora amo más a los gatos.')
doc_es = nlp_es('Amaba a los perros pero ahora amo más a los gatos.')

matches_es = matcher_es(doc_es)

for token in doc_es:
  print('lemma_:', token.lemma_, '==== pos_: ', token.pos_, '==== text: ', token.text )
  print('\n')

for matcher_id,start,end in matches_es:
  matched_span = doc_es[start:end]
  print(matched_span.text)
