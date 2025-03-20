import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from dent_detection import DentDetector
from pathlib import Path

def load_and_preprocess_data(data_dir):
    """Load and preprocess training data"""
    # Data augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        validation_split=0.2
    )

    # Load training data
    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )

    # Load validation data
    validation_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )

    return train_generator, validation_generator

def train_model(model, train_generator, validation_generator, epochs=10):
    """Train the model with the provided data"""
    # Add callbacks for better training
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=2)
    ]

    # Train the model
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        callbacks=callbacks
    )

    return history

def save_model(model, save_path):
    """Save the trained model"""
    model.save(save_path)

def main():
    # Initialize the detector and get the model
    detector = DentDetector()
    model = detector.model

    # Set up data directory
    data_dir = Path('data')
    if not data_dir.exists():
        print(f"Please create a 'data' directory with 'dent' and 'no_dent' subdirectories")
        print(f"containing corresponding training images before running this script.")
        return

    # Load and preprocess data
    train_generator, validation_generator = load_and_preprocess_data(data_dir)

    # Train the model
    history = train_model(model, train_generator, validation_generator)

    # Save the trained model
    save_model(model, 'trained_dent_model.h5')

    print("Training completed successfully!")

if __name__ == '__main__':
    main()