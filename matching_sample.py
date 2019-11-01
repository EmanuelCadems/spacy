import spacy
from spacy.matcher import Matcher

# Spanish vesion
nlp_es = spacy.load('es_core_news_sm')
matcher_es = Matcher(nlp_es.vocab)
pattern_es = [
  { 'LEMMA': 'amar', 'POS': 'VERB'},
  { 'POS': 'NOUN' }
]
matcher_es.add('LOVE_PATTERN', None, pattern_es)
doc_es = nlp_es('Amaba a los perros pero ahora amo más a los gatos.')

matches_es = matcher_es(doc_es)

for token in doc_es:
  print('pos_: ', token.pos_, '\n text: ', token.text, '\n lemma_:', token.lemma_ ,'\n dep_', token.dep_, '\n head', token.head)

for matcher_id,start,end in matches_es:
  matched_span = doc_es[start:end]
  print(matched_span.text)


import spacy
from spacy.matcher import Matcher

# English vesion
nlp_en = spacy.load('en_core_web_sm')
matcher_en = Matcher(nlp_en.vocab)
pattern_en = [
  { 'LEMMA': 'love', 'POS': 'VERB'},
  { 'POS': 'NOUN' }
]
matcher_en.add('LOVE_PATTERN', None, pattern_en)
doc_en = nlp_en('I loved dogs but now I love cats more.')

matches_en = matcher_en(doc_en)

for matcher_id,start,end in matches_en:
  matched_span = doc_en[start:end]
  print(matched_span.text)
