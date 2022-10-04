import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image

data, label = fetch_openml("mnist_784", version=1, return_X_y=True)

xtrain, xtest, ytrain, ytest = train_test_split(data, label, train_size=7000, test_size=3000)
clf = LogisticRegression()
clf.fit(xtrain, ytrain)

def poor(img):
    image = Image.open(img) #Image storage
    bwimg = image.convert(mode="L") #Convert to black/white
    resized = bwimg.resize((28, 28), Image.ANTIALIAS) #Resizing the image
    pixelfilter = 20 #Pixel check density (smaller=more precise)
    minimum = np.percentile(resized, pixelfilter) #Used to compute the n-th percentile
    scaling = np.clip(resized-minimum, 0, 255) #Limiting values
    maximum = np.max(resized) #Checking maximum value
    inptoarray = np.asarray(scaling)/maximum #Converting input to an array
    arraytoimg = np.array(inptoarray).reshape(1, 784) #Converting that array back to image
    final = clf.predict(arraytoimg) #Final prediction
    return final[0]