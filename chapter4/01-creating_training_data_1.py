# spaCy’s rule-based Matcher is a great way to quickly create training data for
# named entity models. A list of sentences is available as the variable TEXTS.
# You can print it the IPython shell to inspect it. We want to find all
# mentions of different iPhone models, so we can create training data to teach
# a model to recognize them as 'GADGET'.

# Write a pattern for two tokens whose lowercase forms match 'iphone' and 'x'.
# Write a pattern for two tokens: one token whose lowercase form matches
# 'iphone' and an optional digit using the '?' operator.

import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match 'iphone' and 'x'
pattern1 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# Token whose lowercase form matches 'iphone' and an optional digit
pattern2 = [{'LOWER': 'iphone'}, {'IS_DIGIT': True, 'OP': '?'}]

# Add patterns to the matcher
matcher.add("GADGET", None, pattern1, pattern2)

for sentence in TEXTS:
  doc = nlp(sentence)
  print('sentence:', doc.text)
  matches = matcher(doc)
  for matcher_id,start,end in matches:
    print('matched:', doc[start:end].text)
