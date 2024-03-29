import spacy
import random
import json

with open("exercises/gadgets.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("GADGET")

# Start the training
nlp.begin_training()

# Loop for 10 iterations
for itn in range(10):
    random.shuffle(TRAINING_DATA)
    losses = {}
    for batch in spacy.util.minibatch(TRAINING_DATA, size=2):
        texts = [text for text, entities in batch]
        annotations = [entities for text, entities in batch]
        nlp.update(texts, annotations, losses=losses)
        print(losses)


doc = nlp("Apple is slowing down the iPhone 8 and iPhone X - how to stop it")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
