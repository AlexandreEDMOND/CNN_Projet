
from keras import layers, models, preprocessing

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def training_CNN(nom_dossier, dimension_photo, model_save_path):
    print("Début")

    train_datagen = preprocessing.image.ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        os.path.join(nom_dossier, "img_norm"),
        target_size=dimension_photo,
        batch_size=16,
        class_mode='binary'
    )

    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(dimension_photo[0], dimension_photo[1], 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(train_generator, epochs=10)

    # Enregistrez le modèle
    if not os.path.exists("./models"):
        os.makedirs("./models")
    model.save(model_save_path)
    print(f"Modèle enregistré à {model_save_path}")


