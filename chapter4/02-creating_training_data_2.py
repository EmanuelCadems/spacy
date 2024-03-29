# Let’s use the match patterns we’ve created in the previous exercise to bootstrap a set of training examples. A list of sentences is available as the variable TEXTS.

# Create a doc object for each text using nlp.pipe.
# Match on the doc and create a list of matched spans.
# Get (start character, end character, label) tuples of matched spans.
# Format each example as a tuple of the text and a dict, mapping 'entities' to the entity tuples.
# Append the example to TRAINING_DATA and inspect the printed data.

import json
from spacy.matcher import Matcher
from spacy.lang.en import English

with open("exercises/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = English()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True, "OP": "?"}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# Create a Doc object for each text in TEXTS
for doc in nlp.pipe(TEXTS):
    # Match on the doc and create a list of matched spans
    spans = [doc[start:end] for match_id, start, end in matcher(doc)]
    # Get (start character, end character, label) tuples of matches
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Format the matches as a (doc.text, entities) tuple
    training_example = (doc.text, {"entities": entities})
    # Append the example to the training data
    TRAINING_DATA.append(training_example)

print(*TRAINING_DATA, sep="\n")
