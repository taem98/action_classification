import logging
from helpers.model_loader import model
from helpers.data_loader import get_generator

import tensorflow as tf
import os

def model_train(model):
    
    # parameters about model and path
    learning_rate = 0.01
    epochs = 1

    save_model_name = "first_test"
    result_base_dir = "../model_results/{}/".format(save_model_name)
    logging_dir = result_base_dir + "logging"
    checkpoint_dir = result_base_dir + "checkpoints"

    os.makedirs(result_base_dir)
    os.mkdir(logging_dir)
    os.mkdir(checkpoint_dir)
    
    def scheduler(epoch: int) -> float:
        if epoch < epochs * 0.5:
            return learning_rate
        if epoch >= epochs * 0.5 and epoch < epochs * 0.75:
            return learning_rate / 10.0
        return learning_rate / 10.0 / 10.0

    optimizer = tf.keras.optimizers.Adam(lr = learning_rate)

    model.compile(
        optimizer=optimizer,
        loss='binary_crossentropy',
        metrics=['accuracy'],
    )

    lr_sched_callback = tf.keras.callbacks.LearningRateScheduler(scheduler)

    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=logging_dir, update_freq=1
    )  

    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=os.path.join(
            checkpoint_dir, "checkpoint-weights-{epoch:02d}-{val_loss:.2f}.ckpt"
        ),
        save_weights_only=True,
        save_best_only=True,
        monitor='val_loss',
        verbose=1
    )

    train_generator = get_generator('train')
    validation_generator = get_generator('validation')

    _ = model.fit(
        train_generator,
        # steps_per_epoch=[all data / batch size],
        epochs=epochs,
        callbacks=[lr_sched_callback, tensorboard_callback, checkpoint_callback],
        # callbacks=[lr_sched_callback, tensorboard_callback],
        validation_data=validation_generator,
    )

    model.save(result_base_dir+save_model_name+'.h5')


if __name__ == '__main__':
    
    model = model()
    model_train(model)

