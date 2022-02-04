import tensorflow as tf



def CRBP(x, num_filter,
        conv_kernel_size, conv_stride,
        pooling_kernel_size, pooling_stride):

    x = tf.keras.layers.Conv2D(
            filters=num_filter,
            kernel_size=conv_kernel_size,
            strides=conv_stride,
            padding="same",
            use_bias=False,
            kernel_regularizer=tf.keras.regularizers.l2(l=1e-4),
            kernel_initializer=tf.keras.initializers.he_normal()
            )(x)
    x = tf.keras.layers.ReLU()(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPool2D(
            pool_size=pooling_kernel_size,
            strides=pooling_stride
            )(x)

    return x


def CRB(x, num_filter,
        conv_kernel_size, conv_stride):

    x = tf.keras.layers.Conv2D(
            filters=num_filter,
            kernel_size=conv_kernel_size,
            strides=conv_stride,
            padding="same",
            use_bias=False,
            kernel_regularizer=tf.keras.regularizers.l2(l=1e-4),
            kernel_initializer=tf.keras.initializers.he_normal()
            )(x)
    x = tf.keras.layers.ReLU()(x)
    x = tf.keras.layers.BatchNormalization()(x)

    return x


def DBR(x, num_filter):
    x = tf.keras.layers.Dense(num_filter)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.ReLU()(x)
    
    return x


def DS(x, num_filter):
    x = tf.keras.layers.Dense(num_filter,
                            activation='sigmoid')(x)
    
    return x


def model():
    dropout = 0.2
    num_class = 4
    input_shape = (192, 112, 3)

    conv_kernel_size = (3, 3)
    conv_stride = (1, 1)
    pooling_kernel_size = (2, 2)
    pooling_stride = (2, 2)

    
    inputs = tf.keras.Input(shape=input_shape, name="input")

    x = CRBP(inputs, 16,
                conv_kernel_size, conv_stride,
                pooling_kernel_size, pooling_stride)
    x = CRBP(x, 32,
                conv_kernel_size, conv_stride,
                pooling_kernel_size, pooling_stride)
    x = CRBP(x, 64,
                conv_kernel_size, conv_stride,
                pooling_kernel_size, pooling_stride)
    x = CRBP(x, 64,
                conv_kernel_size, conv_stride,
                pooling_kernel_size, pooling_stride)
    x = CRB(x, 128,
                conv_kernel_size, conv_stride)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(rate=dropout)(x)
    x = DBR(x, 128)
    x = DBR(x, 64)
    outputs = DS(x, num_class)

    model = tf.keras.Model(
        inputs=inputs, outputs=outputs, name="action_classification_192x112_4"
    )

    # model.summary()

    return model