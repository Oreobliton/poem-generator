
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time

class TextModel(tf.keras.Model):
  def __init__(self, vocab_size, embedding_dim, rnn_units):
    super().__init__(self)
    self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim) # Input layer
    self.gru1 = tf.keras.layers.GRU(rnn_units,                       # GRU is a type of RNN
                                   return_sequences=True,
                                   return_state=True)

    self.gru2 = tf.keras.layers.GRU(rnn_units,                       # GRU is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    
    self.gru3 = tf.keras.layers.GRU(rnn_units,                       # GRU is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    
    self.gru4 = tf.keras.layers.GRU(rnn_units,                       # GRU is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    
    self.conc = tf.keras.layers.Concatenate(axis=-1)
    self.dense = tf.keras.layers.Dense(vocab_size)                  # Output layer
    


  def call(self, inputs, states=None, return_state=False, training=False):  # need to overload this for our special network :D
    x = inputs 
    x = self.embedding(x, training=training)
    if states is None:
        states1 = self.gru1.get_initial_state(x)
        states2 = self.gru2.get_initial_state(x)
        states3 = self.gru3.get_initial_state(x)
        states4 = self.gru4.get_initial_state(x)
    else:
        states1 = states[0]
        states2 = states[1]
        states3 = states[2]   
        states4 = states[3] 
        
    x, states1 = self.gru1(x, initial_state=states1, training=training)
    x, states2 = self.gru2(x, initial_state=states2, training=training)
    y = x
    
    x, states3 = self.gru3(x, initial_state=states3, training=training)
    y, states4 = self.gru4(y, initial_state=states4, training=training)
    
    
    x = self.conc([x,y]) 
    x = self.dense(x, training=training)

    if return_state:
      return x, [states1, states2, states3, states4]
    else:
      return x
  
    