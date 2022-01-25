from keras import *

def build_model(self):
    model = Sequential()
    model.add(Dense(24,input_dim=self.state_size, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(self.action_size, activation='softmax'))
    return model
    