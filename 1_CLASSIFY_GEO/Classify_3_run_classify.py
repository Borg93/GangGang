import Classify_helpers as ch

import sys

import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json

if len(sys.argv) < 2:
    print "ERROR: provide suffix for model file"
    exit(1)
MODEL_SUFFIX = sys.argv[1]

geometry = ["6poly", "tetrahedra", "cone", "cylinder"]

all_data = ch.load_training_data(geometry)

(training_data, test_data) = ch.split_data(all_data, 0.2)

test_data_np = np.array(map(lambda x: x['data'], test_data))
test_labels_np = np.array(map(lambda x: x['label'], test_data))

classify_data_np = np.array(map(lambda x: x['data'], [all_data[0]]))
classify_labels_np = np.array(map(lambda x: x['label'], [all_data[0]]))

print test_data_np


## LOAD MODULE

model = model_from_json(open(ch.MODELDIR + ch.MODEL_ARCH_PREFIX + MODEL_SUFFIX + '.json').read())
model.load_weights(ch.MODELDIR + ch.MODEL_WEIGHTS_PREFIX + MODEL_SUFFIX + '.h5')
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

score = model.evaluate(test_data_np, test_labels_np)
print('Test score:', score[0])
print('Test accuracy:', score[1])

classes = model.predict(classify_data_np)

print classes

"""
classes = model.predict(imgarr)
chance = classes[0][0]

print "chance that you are procrastinating right now:"
print chance, "%, or:",
textchance = ch.prob_to_text(chance)
print textchance

if(chance > 0.5):
    voice = random.choice(ch.normalvoices)
    os.system("say -v " + voice + " You are " + textchance)

time.sleep(3)
"""
