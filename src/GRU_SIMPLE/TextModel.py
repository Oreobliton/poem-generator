
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time

class TextModel(tf.keras.Model):
  def __init__(self, vocab_size, embedding_dim, rnn_units):
    super().__init__(self)
    self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim) # Input layer
    self.gru = tf.keras.layers.GRU(rnn_units,                       # GRU is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    self.dense = tf.keras.layers.Dense(vocab_size)                  # Output layer

  def call(self, inputs, states=None, return_state=False, training=False):  # need to overload this for our special network :D
    x = inputs 
    x = self.embedding(x, training=training)
    if states is None:
        states = self.gru.get_initial_state(x)
    x, states = self.gru(x, initial_state=states, training=training)
    x = self.dense(x, training=training)

    if return_state:
      return x, states
    else:
      return x