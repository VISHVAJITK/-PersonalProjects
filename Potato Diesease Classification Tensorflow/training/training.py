from keras.layers.preprocessing.image_preprocessing import HORIZONTAL_AND_VERTICAL
import tensorflow as tf
import keras
from keras import layers
import matplotlib.pyplot as plt

image_size = 256
batch_size = 32

 
directory = r'E:\Projects\Potato_Diesease\data'
datasets = tf.keras.utils.image_dataset_from_directory(
    directory,
    labels="inferred",
    batch_size=batch_size,
    image_size=(image_size,image_size),
    shuffle=True,
)

class_names = datasets.class_names


for images, label in datasets.take(1):
    fig, ax  = plt.subplots(5,2, figsize= (10,15))
    for row in range(5):
        for col in range(2):
            ax[row, col].imshow(images[row+col].numpy().astype('uint8'))
            ax[row, col].axis('off')
            ax[row, col].set_title(class_names[label[row+col]])


def make_datasets(ds, train_split= 0.8,val_split = 0.1, test_split= 0.1):
    
    train_size = int(len(ds)* train_split)
    val_size = int(len(ds)* val_split)

    train_ds = ds.take(train_size)
    val_ds = ds.skip(train_size).take(val_size)
    test_ds = ds.skip(train_size).skip(val_size)

    return train_ds, val_ds, test_ds


train_ds, val_ds, test_ds = make_datasets(datasets)


## Agumentation
resizing_rescaling = keras.models.Sequential([
    layers.Resizing(image_size,image_size),
    layers.Rescaling(1/256)
])

## Agumentation

data_agumentation = keras.models.Sequential([
    layers.RandomFlip(mode="horizontal_and_vertical"),
    layers.RandomRotation(0.2)
])


## Model Building
channels = 3
n_classes = 3


inputs = keras.Input(shape = (image_size, image_size,channels))
x = resizing_rescaling(inputs)
x = data_agumentation(x)
x = layers.Conv2D(32, kernel_size = (3,3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64,  kernel_size = (3,3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64,  kernel_size = (3,3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Conv2D(64, (3, 3), activation='relu')(x)
x = layers.MaxPooling2D((2, 2))(x)
x = layers.Flatten()(x)
x = layers.Dense(64, activation='relu')(x)
outputs = layers.Dense(n_classes, activation='softmax')(x)

model = keras.Model(inputs = inputs, outputs = outputs)

model.summary()


model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy']
)

history = model.fit(
    train_ds,
    batch_size=batch_size,
    validation_data=val_ds,
    verbose=1,
    epochs=30,
)

import pandas as pd
epochs = 30
data = pd.DataFrame(history.history)
data['epochs'] = range(epochs)

fig, (ax1,ax2) = plt.subplots(1,2)
ax1.plot(data.epochs, data.accuracy, label = 'train accuracy')
ax1.plot(data.epochs, data.val_accuracy, label = "validation accuracy")
ax1.set_xlabel('epochs')
ax1.set_ylabel('Accuracy')
ax1.set_title('Accuracy')

ax2.plot(data.epochs, data.loss, label = 'training loss')
ax2.plot(data.epochs, data.val_loss, label = "validation loss")
ax2.set_xlabel('epochs')
ax2.set_ylabel('loss')
ax2.set_title('loss')

plt.legend()
plt.show()

import numpy as np
for images_batch, labels_batch in test_ds.take(1):
    
    first_image = images_batch[0].numpy().astype('uint8')
    first_label = labels_batch[0].numpy()
    
    print("first image to predict")
    plt.imshow(first_image)
    print("actual label:",class_names[first_label])
    
    batch_prediction = model.predict(images_batch)
    print("predicted label:",class_names[np.argmax(batch_prediction[0])])



def predict(model, image):
    image_array = tf.keras.utils.img_to_array(
        image, data_format=None, dtype=None)
    image_array = tf.expand_dims(image_array, 0)

    predictions = model.predict(image_array)


    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence



plt.figure(figsize=(15, 15))
for images, labels in test_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        
        predicted_class, confidence = predict(model, images[i].numpy())
        actual_class = class_names[labels[i]] 
        
        plt.title(f"Actual: {actual_class},\n Predicted: {predicted_class}.\n Confidence: {confidence}%")
        
        plt.axis("off")



import os
model_version = max([int(i) for i in os.listdir("../models") + [0]])+1
model.save(f"../models/{model_version}")

model.save("../potatoes.h5")