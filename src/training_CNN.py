# Pour TensorFlow
from keras import layers, models, preprocessing

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Réduit la verbosité des avertissements TensorFlow

print("Début")

train_datagen = preprocessing.image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    r'C:\Users\33678\VsCode\CNN Hommes-Femmes\reduc_data\img_redim',
    target_size=(836, 670),  # Les dimensions que vous avez choisies
    batch_size=16,
    class_mode='binary'  # ou 'categorical' selon le nombre de classes
)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(836, 670, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # 1 neurone pour une classification binaire
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(train_generator, epochs=10)


