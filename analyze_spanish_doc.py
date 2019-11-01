import spacy

text = 'Para Diego Falcone, head portfolio manager de Cohen, el proceso de dolarización continuará cualquiera sea el escenario post 27 de octubre, aunque en algunos casos será "más sensible al precio". "Si Mauricio Macri logra entrar en el ballottage, tal vez los ahorristas decidan dolarizarse a $65 o $66, pero no estén dispuestos a hacerlo a $79 o $80, como se vio en los últimos días", apuntó.'

# Spanish version
nlp_es = spacy.load('es_core_news_sm')
doc_es = nlp_es(text)
for ent in doc_es.ents:
  print(ent.text, ent.label_)

# English version
nlp_en = spacy.load('en_core_web_sm')
doc_en = nlp_en(text)
for ent in doc_en.ents:
  print(ent.text, ent.label_)

