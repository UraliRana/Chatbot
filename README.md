# Chatbot

The project is named "RNN based conversational agent" and the goal of the project is to develop an intelligent Chabot that can generate answers to user's requirements in text form. The team used a generative based conversation agent using the seq2seq model, which is developed using Recurrent Neural Network(RNN). The model is trained on two datasets, which are dialogues from movies. The team used an augmentation method to improve the performance by replacing words with synonyms. The model was developed using TensorFlow and Keras with an attention mechanism.
Libraries used :
Numpy
OS
NLTK
Tokenizer
Tensorflow
Keras
MatplotLib
Steps for Execution:

To begin the project, I first imported the dataset and assigned variables to it using the os library.
Data Preprocessing: Pre-processing consists of three main components which are tokenization, dictionary mapping, and zero paddings.
Create a Embedding Layer:The recurrent neural network can not support integer tokens so using embedding layer every integer token mapped into the vector of floating value which is in -1 to 1 value. So, the words have similar semantic meanings which mapped with their vector. Here, the embedding size is 150 and the input size is the number of words which is 1000. Several steps are dependent on the maximum tokens of the dataset. With the use of Keras API, The task of embedding layer performed using the ”Embedding” function at encoder and decoder part both sides.
Create a Encoder: In these projects, 3 Layers of GRU cells created and network implemented using Keras API. The state size of GRU cells is 256.
Create a Decoder: The decoder takes two inputs. First, it needs the ”thought vector” produced by the encoder which summarizes the contents of the input-text. A decoder implementation of 3 layers GRU cells and dense layer used a linear function instead of softmax function
There were two activation functions used:
for Hidden layers : 'Tanh'
for Final Layer/ Output layer : 'softmax' for giving the output
To compile the model we used 'RMSprop' as an optimizer, 'sparse_softmax_cross_entropy_with_logits' as Loss Function and metric used was 'Accuracy'.

The Model created was trained for 35 epochs which gave an Accuracy of around 95% reducing the Loss Function to 0.7.
Accuracy and loss for Training Data:
Epoch 1/35
2289/2289 [==============================] - 20s 9ms/sample - loss: 3.4037 - sparse_categorical_accuracy: 0.5646 - val_loss: 2.7940 - val_sparse_categorical_accuracy: 0.6341
Epoch 2/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 2.6184 - sparse_categorical_accuracy: 0.6335 - val_loss: 2.2452 - val_sparse_categorical_accuracy: 0.6685
Epoch 3/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 2.1214 - sparse_categorical_accuracy: 0.6743 - val_loss: 2.3229 - val_sparse_categorical_accuracy: 0.6612
Epoch 4/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 2.0165 - sparse_categorical_accuracy: 0.6829 - val_loss: 2.0896 - val_sparse_categorical_accuracy: 0.6793
Epoch 5/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.9072 - sparse_categorical_accuracy: 0.6868 - val_loss: 2.0116 - val_sparse_categorical_accuracy: 0.6793
Epoch 6/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.8232 - sparse_categorical_accuracy: 0.6928 - val_loss: 2.0062 - val_sparse_categorical_accuracy: 0.6848
Epoch 7/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.7798 - sparse_categorical_accuracy: 0.6919 - val_loss: 1.9801 - val_sparse_categorical_accuracy: 0.6993
Epoch 8/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.6768 - sparse_categorical_accuracy: 0.7010 - val_loss: 2.1055 - val_sparse_categorical_accuracy: 0.6884
Epoch 9/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.6036 - sparse_categorical_accuracy: 0.7048 - val_loss: 1.9605 - val_sparse_categorical_accuracy: 0.6975
Epoch 10/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.5165 - sparse_categorical_accuracy: 0.7108 - val_loss: 1.9712 - val_sparse_categorical_accuracy: 0.6938
Epoch 11/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.4286 - sparse_categorical_accuracy: 0.7172 - val_loss: 1.8832 - val_sparse_categorical_accuracy: 0.7065
Epoch 12/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.3335 - sparse_categorical_accuracy: 0.7267 - val_loss: 2.0642 - val_sparse_categorical_accuracy: 0.6975
Epoch 13/35
2289/2289 [==============================] - 16s 7ms/sample - loss: 1.2412 - sparse_categorical_accuracy: 0.7375 - val_loss: 1.8703 - val_sparse_categorical_accuracy: 0.7011
