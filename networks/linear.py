import tensorflow as tf
import numpy as np

class LinearModel(object):
    def __init__(self, 
                 sess,
                 num_features,
                 name = "BinaryLinear"):

        self.sess = sess

        with tf.variable_scope(name):

            # Initialize input and weights
            self.inputs = tf.placeholder(tf.float32, shape=[1, num_features],
                    name="inputs")
            self.w = tf.Variable(tf.random_normal([num_features, 1]), 
                    name="weights")
            self.b = tf.Variable(tf.random_normal([1]), name="bias")

            # Create the linear model
            self.model = tf.nn.bias_add(tf.matmul(self.inputs, self.w), self.b)

    def calc_action(self, observation):
        """
        Evaluate the policy for a given observation.

        Returns a binary action.
        """
        pred_value = self.model.eval({self.inputs: observation}, session=self.sess)
        return int(pred_value < 0)
