# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time
from TextModel import *


##########CONFIGURER ICI : 
CORPUS_PATH = "../../data/Corpus_POETRY.txt"
SEQ_LENGTH = 100
EPOCHS = 20
##########




path_to_file = CORPUS_PATH
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))

example_texts = ['abcdefg', 'xyz']

seq_length = SEQ_LENGTH
examples_per_epoch = len(text)//(seq_length+1)

# bunch of cool conversion functions
ids_from_chars = preprocessing.StringLookup(
    vocabulary=list(vocab), mask_token=None)
chars_from_ids = tf.keras.layers.experimental.preprocessing.StringLookup(
    vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None)
def text_from_ids(ids):
  return tf.strings.reduce_join(chars_from_ids(ids), axis=-1)


# function that allows the generation the input and target data!
def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text

all_ids = ids_from_chars(tf.strings.unicode_split(text, 'UTF-8')) # text vector
ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids) # stream of characters indices

sequences = ids_dataset.batch(seq_length+1,drop_remainder = True)

dataset = sequences.map(split_input_target)


# Batch size
BATCH_SIZE = 64

# Buffer size to shuffle the dataset
# (TF data is designed to work with possibly infinite sequences,
# so it doesn't attempt to shuffle the entire sequence in memory. Instead,
# it maintains a buffer in which it shuffles elements).
BUFFER_SIZE = 10000

dataset = (
    dataset
    .shuffle(BUFFER_SIZE)
    .batch(BATCH_SIZE, drop_remainder=True)
    .prefetch(tf.data.experimental.AUTOTUNE))

# Length of the vocabulary in chars
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024

# Bring the model in
model = TextModel(
    # Be sure the vocabulary size matches the `StringLookup` layers.
    vocab_size=len(ids_from_chars.get_vocabulary()),
    embedding_dim=embedding_dim,
    rnn_units=rnn_units)

# Directory where the checkpoints will be saved
checkpoint_dir = './training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)


loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True) # our model returns logits
model.compile(optimizer='adam', loss=loss)
history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])

model.save("Poem_generator")

