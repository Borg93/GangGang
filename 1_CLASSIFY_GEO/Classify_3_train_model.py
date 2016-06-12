import Classify_helpers as ch
import json
import os
import random
import sys
import re
import numpy as np
from functools import partial

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.utils import np_utils, generic_utils

if len(sys.argv) < 2:
    print "ERROR: provide suffix for model file"
    exit(1)
MODEL_SUFFIX = sys.argv[1]


######### get training data

geometry = ["box", "tetrahedra"]

filepaths = [ str(ch.DATADIR + f + ".json") for f in geometry ]

all_data = []

for index in xrange(len(geometry)):

    filename = filepaths[index]
    geo = geometry[index]

    label = [0] * len(geometry)
    label[index] = 1

    with open(filename) as fp:
        data = json.load(fp)
        for datum in data:
            datum.update({'geometry':geo, 'label':label})

    
    all_data.extend(data)


random.shuffle(all_data)

training_data = np.array(map(lambda x: x['data'], all_data))
training_labels = np.array(map(lambda x: x['label'], all_data))


######## sMODEL

def makeCNN():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same', input_shape=(3, helpers.IMAGE_HEIGHT, helpers.IMAGE_WIDTH)))
    model.add(Activation('relu'))

    model.add(Convolution2D(32, 3, 3, border_mode='same'))
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
     
    model.add(Convolution2D(64, 3, 3, border_mode='same', input_shape=(3, helpers.IMAGE_HEIGHT, helpers.IMAGE_WIDTH)))
    model.add(Activation('relu'))

    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
     
    model.add(Flatten())
    model.add(Dense(input_dim = (64*8*8), output_dim = 512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
     
    model.add(Dense(input_dim=512, output_dim=2))
    model.add(Activation('softmax'))

    model = makeCNN()
    return model


def makeNormal():
    model = Sequential()
    
    model.add(Dense(500, input_shape=(1000,), init='uniform'))
    model.add(Activation("tanh"))
    model.add(Dropout(0.25))

    model.add(Dense(500, init='uniform'))
    model.add(Activation("tanh"))
    model.add(Dropout(0.25))

    model.add(Dense(50, init = 'uniform'))
    model.add(Activation("tanh"))
    model.add(Dropout(0.25))

    model.add(Dense(len(geometry)))
    model.add(Activation("softmax"))
    return model

model = makeNormal()

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)

#model.compile(loss='mse', optimizer=sgd, metrics=['accuracy'])
#model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])
#model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

print("begin to train")

history = model.fit(training_data, training_labels,
        nb_epoch = 1000, 
        batch_size= 16, 
        verbose= 2, 
        validation_split=0.2,
        shuffle=True)

####### SAVING

print ("saving model to file..")

json_string = model.to_json()
open(ch.MODELDIR + 'model_architecture__' + MODEL_SUFFIX + '.json', 'w').write(json_string)
model.save_weights(ch.MODELDIR + 'model_weights__' + MODEL_SUFFIX + '.h5')




