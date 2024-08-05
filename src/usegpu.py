import tensorflow as tf

# Print TensorFlow version and number of GPUs available
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Set up GPU memory growth and default device
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # Set memory growth to prevent TensorFlow from allocating all GPU memory at once
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        
        # Set GPU as the default device
        tf.config.set_visible_devices(gpus[0], 'GPU')
        print("GPU is set as the default device.")
    except RuntimeError as e:
        print(e)
else:
    print("No GPU available.")

# Example TensorFlow operation to verify GPU usage
with tf.device('/GPU:0'):
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
    c = tf.matmul(a, b)
    print(c)
