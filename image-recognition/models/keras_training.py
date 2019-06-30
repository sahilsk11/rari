#import keras
from keras.models import Sequential
from keras.layers import Convolution2D

classifier = Sequential()

classifier.add(Convolutional2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

classifier.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))

classifier.add(keras.layers.Flatten())

classifier.add(keras.layers.Dense(output_dim=128, activation='relu'))
classifier.add(keras.layers.Dense(output_dim=1, activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

train_datagen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
    'train',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

test_set = test_datagen.flow_from_directory(
    'test',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

