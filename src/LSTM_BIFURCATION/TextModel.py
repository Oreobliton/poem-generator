
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time

class TextModel(tf.keras.Model):
  def __init__(self, vocab_size, embedding_dim, rnn_units):
    super().__init__(self)
    self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim) # Input layer
    self.lstm1 = tf.keras.layers.LSTM(rnn_units,                       # lstm is a type of RNN
                                   return_sequences=True,
                                   return_state=True)

    self.lstm2 = tf.keras.layers.LSTM(rnn_units,                       # lstm is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    
    self.lstm3 = tf.keras.layers.LSTM(rnn_units,                       # lstm is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    
    
    
    self.lstm4 = tf.keras.layers.LSTM(rnn_units,                       # lstm is a type of RNN
                                   return_sequences=True,
                                   return_state=True)
    
    
    
    self.conc = tf.keras.layers.Concatenate(axis=-1)
    self.dense = tf.keras.layers.Dense(vocab_size)                  # Output layer
    


  def call(self, inputs, states=None, return_state=False, training=False):  # need to overload this for our special network :D
    x = inputs 
    x = self.embedding(x, training=training)
    if states is None:
        states11, states12 = self.lstm1.get_initial_state(x)
        states21, states22 = self.lstm2.get_initial_state(x)
        states31, states32 = self.lstm3.get_initial_state(x)
        states41, states42 = self.lstm4.get_initial_state(x)
    else:
        states11, states12 = states[0]
        states21, states22 = states[1]
        states31, states32 = states[2] 
        states41, states42 = states[3]

        
    x, states11, states12 = self.lstm1(x, initial_state=[states11, states12], training=training)
    x, states21, states22 = self.lstm2(x, initial_state=[states21, states22], training=training)
    y = x
    
    x, states31, states32 = self.lstm3(x, initial_state=[states31, states32], training=training)
    y, states41, states42 = self.lstm4(y, initial_state=[states41, states42], training=training)
    
    
    x = self.conc([x,y]) 
    x = self.dense(x, training=training)

    if return_state:
      return x, [[states11, states12],[states21, states22],[states31, states32],[states41, states42]]
    else:
      return x
  
    