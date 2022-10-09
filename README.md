
# Gest-RECOG
This project is all about the different types of gesture recognitions by using machine learning/deep learning algorithams.

<p align="center">
  <img src="https://user-images.githubusercontent.com/72018919/194757500-6738d113-ab3e-4c5f-8233-2088e0704dce.gif" />
</p>

## Abstract
Gest-RECOG demonstrates the fabrication of the own fabricated self-powred sensor and their integration with the different machine learning\deep learning neural networks for classifies the different gestures. We have used numerous algorithms such as unsupervised k-means clusstering and unsupervised k-nearest neibor (KNN), support vector machine (SVM), deep neural network (DNN) and pattern recognition, which gives the classification accuracy of ~97%, ~93%, ~94%, 98%, respectively.
The sensor (W-TENG) is fabricated with the plastic waste material, which can able to carryout numerous biomedical measurements such as arterial pulse , breathing rate , and gait analysis monitoring. Thus, W-TENG integrated with the artificial intellegence has the potential to use in the advanced technological applications such as humonoid robotics, artificial prosthesis, and gesture controlled cars.

## Pre-Requirements
To run this project, you will need to add the following environment variables to your .env file
#Python 3\
#MATLAB\
`
## Libraries
 - [Pandas](https://pandas.pydata.org/)
 - [Numpy](https://numpy.org/)
 - [Matplotlib](https://matplotlib.org/)
 - [Seaborn](https://seaborn.pydata.org/)
 - [Scikit-learn](https://scikit-learn.org/stable/)
 - [Matplotlib](https://matplotlib.org/)
 
## Core Algorithms
The Gest-RECOG has used a wide number of supervised and unsupervised machine learning algorithms for classification, regression, and clustering, including:

#### ⦿k-means clustering
It is a kind of unsurevised machine learning, which is used to observe the seprated classes prevailing in the dataset. k-means clustering does partitions of data in the k distance clusters, these clusters are based on distance of the centroid of a cluster. k-means clustering is an iterative and data-partitioning algorithm where k clusters are defined by centroids.
(https://ieeexplore.ieee.org/document/9072123)

![clusttering](https://user-images.githubusercontent.com/72018919/194757279-e7e5c1b6-d2b4-4829-a433-73554c111feb.png)

#### ⦿DNN (Deep Neural Network)
A deep neural network is a part of artificial intelligence, which is working on the principle of artificial neural networks. It mainly consists of three layers: (i) an input layer to provide the inputs to the model, (ii) a hidden layer for a multilayer stacking and responsible for doing the complex calculations which are tuned by the weights and biases, and (iii) an output layer to provide the output of the model.(https://ieeexplore.ieee.org/document/7867471)

![DNN](https://user-images.githubusercontent.com/72018919/194757302-d9e13ca3-4478-48e5-813c-7d19aa38233a.png)

#### ⦿SVM (Support Vector Machines)
Support vector machine classifier is supervised learning model which used for classification of two or more classes that separate all data points of one class from the data points of another class by creating the hyperplane in an N-dimensional space that best fits to the classification of the data points. These extreme points are called support vectors, and the dimensions are depended on the number of features. SVM perform non-linear classification using the kernel machines for mapping the data into different specs.(https://ieeexplore.ieee.org/document/708428)

![svm](https://user-images.githubusercontent.com/72018919/194757407-7e687b3a-a450-4fe6-a30e-2ebac5b64c51.png)

#### ⦿KNN (k-Nearest Neighbor)
k-nearest neighbor is a classification model in which the distance metric and the number of nearest neighbors is used to classify the data and compute the prediction. The distance matric and nearest neighbours can be altered using KNN.(https://ieeexplore.ieee.org/document/549118)

![knn](https://user-images.githubusercontent.com/72018919/194757448-a58e1fe2-ced8-4583-b6df-0239ff03b3c9.png)

#### ⦿Pattern Recognition
The Pattern Recognition is used for data processing and visualization to train the model using the two-layer feed-forward networks with neurons. The results can be analysed using the confusion matrix and receiver operating characteristic (ROC) curves.(https://ieeexplore.ieee.org/document/9208207)

![pattern](https://user-images.githubusercontent.com/72018919/194757456-73f4185e-dfb2-4b32-b43a-ed830b71ce00.png)

In addition to the machine learning algorithms above, the toolkit also includes a large number of algorithms for preprocessing, feature extraction, and post processing.

## FAQ

#### 1. What is the principle behind the working of the sensor (W-TENG)?

W-TENG is primarily working on the combined principle of contact electrification and electrostatic induction.

#### 2. Which material is used to fabricate the sensor?
Nylon 66 is used to fabricate the sensor (W-TENG), which was recycled from the waste plastic material availabe arround in different forms such as toothbrush bristles, wire ties, nylon fabric/fiber to a name of few. 

#### 3. Is the material compatible with body?
Yes, the material (nylon 66) used in the fabrication of the sensor is fully biomcaopatibale with the body/sking; moreover the gesture monitoring and the biomedical monitoring is carrying out by using non-invasive mode i.e. not penetrated into the body.

#### 4. Is any battery required to operate the sensor?
No, there is not any battery or energy storage device required to operate the sensor; since it is working based on the principle of contact electrification, it uses the our daily activities such as walking, running, speaking, breathing takes as an input stimuli to power the sensor; that is why they are also called as self-powered sensor.

#### 5. What is the durability of the sensor?
The sensor is very much robust, which lasts for a long time.

#### 6. What is the future scope of this sensor?
W-TENG equipped with artificial intelligence provides an effective way to use the waste material for advanced and smart biomedical applications such as artificial prosthesis, humanoid robotics, and internet of medical things (IoMT) to name of few. Which not only helps to reduce the waste materials prevailing in the environment but also provides a key solution for intelligent healthcare monitoring, one of the prime requirements of the time; simultaneously gives impetus to the clean, green and circular economy

## Getting Started
This example demonstrates a few key components/modules for the implimentation of the basic model of machine learning\deep learning algorithms, such as:
►how to load a dataset from a file (e.g., a CSV file)\
►how to split a dataset into a training and test dataset\
►how to set up a new Gesture Recognition Pipeline and add a classification algorithm to the pipeline\
►how to use a training dataset to train a new classification model\
►how to save/load a trained pipeline to/from a file\
►how to use an automatically test dataset to test the accuracy of a classification model\
►how to use a manually test dataset to test the accuracy of a classification model\
►how to print detailed test results, such as precision, recall, and the confusion matrix

## Installation

python 3

```bash
sudo dnf install python3
```
scikit-learn


```bash
pip install -U scikit-learn
```

pandas

```bash
conda install pandas
```

numpy

```bash
pip install numpy

```

seaborn

```bash
pip install seaborn

```

matplotlib

```bash
pip install matplotlib

```

numpy

```bash
pip install numpy

```

## Authors
- [ABnano](https://github.com/ABnano)

## 🚀 About Me
Enthusiastic Learner Stitching the Nanoscience with Machine Learning

