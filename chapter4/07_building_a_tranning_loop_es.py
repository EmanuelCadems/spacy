import spacy
import random
import json

with open("exercises/insultos.json") as f:
    TRAINING_DATA = json.loads(f.read())

nlp = spacy.blank("es")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner)
ner.add_label("INSULTO")

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

new_sample1 = "Se lo dije al boludo de Pedro, pero no me escuchó"
new_sample2 = "Sos un pelotudo!"
new_sample3 = "haceme caso, boludo"
new_sample4 = "Sos un boludo! Mirá lo que hiciste"
doc = nlp(new_sample1)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# "le pedí que me entregara con tiempo la carpeta para ir adelantando el trabajo y, como el muy boludo no la trajo, ahora no podemos cumplir con los plazos acordados; seré el rey de los boludos, pero dejame que te siga contando"
# 'Es el boludo de la sección.' no
# "Un segundo antes de salir me dice: mirá que se lo dije al pendejo boludo." no
# "Y él me dijo: ‘Boludo, esto tiene que ser de verdad’"
# "Aquella noche, mientras me agazapaba en la sombra del parque y el pasado me explotaba en la cara, escuché quince veces una canción, Paloma, que el boludo Andrés Calamaro había puesto en mi vida mucho tiempo atrás." no
# "¡Qué boludo!"
# "Eres un boludo"
# "No digas boludeces"
# "Boludo aprende a manejar."
# "Boludo viste el nuevo trailer de ..."
# "Sos un boludo era mas fácil si lo hacías así."

# 'Aquella vez, "boludo" no estuvo en el repertorio, tal vez porque ya no era una "mala palabra".' Si
# "puedes esperarlo hasta mañana, es un huevón que nunca tiene urgencia"
# "Hay que ser ejemplo de huevón"
# "este a veces es huevón y a veces no"
