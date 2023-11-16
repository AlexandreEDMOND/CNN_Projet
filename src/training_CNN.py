
from keras import layers, models, preprocessing

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def training_CNN():
    print("Début")

    train_datagen = preprocessing.image.ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        r'./reduc_data/img_norm',
        target_size=(200, 200),
        batch_size=16,
        class_mode='binary'
    )

    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(train_generator, epochs=10)


