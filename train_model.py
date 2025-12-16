import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def main():
    # ===============================
    # 1. Carregar o dataset MNIST
    # ===============================
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Normalização
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # Ajuste de formato para CNN (28, 28, 1)
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    # ===============================
    # 2. Construção do modelo CNN
    # ===============================
    model = keras.Sequential([
        layers.Input(shape=(28, 28, 1)),

        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),

        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    # ===============================
    # 3. Treinamento
    # ===============================
    model.fit(
        x_train,
        y_train,
        validation_split=0.1,
        epochs=5,
        batch_size=32,
        verbose=2
    )

    # ===============================
    # 4. Avaliação
    # ===============================
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print(f"Acurácia no conjunto de testes: {accuracy:.4f}")

    # ===============================
    # 5. Salvar modelo
    # ===============================
    model.save("model.h5")
    print("Modelo salvo como model.h5")

if __name__ == "__main__":
    main()

