# ASL Sign Language Detection Using CNN

## Introduction
This project is an implementation of a Convolutional Neural Network (CNN) using TensorFlow and Keras to detect American Sign Language (ASL) letters. The project includes creating a custom dataset, training a CNN model, and developing a real-time detection application.

## Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

### Clone the Repository
```bash
git clone https://github.com/CBJdereal/SignLanguageDetectionCNN.git
cd SignLanguageDetectionCNN
```

### Install Required Libraries
Create a [`requirements.txt`](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/requirements.txt) file in the `src` directory with the following contents:
```
tensorflow
keras
opencv-contrib-python
split-folders
```

Install the libraries using pip:
```bash
pip install -r ./src/requirements.txt
```

## Dataset Preparation

### Collecting Data
Run [`collectdata.py`](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/collectdata.py) to collect images for the dataset. This script initializes your webcam and allows you to capture images of ASL signs, saving them in a structured directory format (`SignImage48x48`) with subfolders for each letter and a special folder for variable background images (`blank`).
```bash
python ./src/collectdata.py
```

### Data Splitting
After collecting the data, use [`split.py`](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/split.py) to divide the dataset into training and validation sets.
```bash
python ./src/split.py
```

## Model Training

### Setup Google Colab
Upload the Jupyter notebook [`trainmodel.ipynb`](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/trainmodel.ipynb) to Google Colab and follow the instructions to mount your Google Drive for model saving and dataset access.

### Run Training
Execute the cells in the notebook to train the model. The notebook includes detailed steps for configuring the model, initiating training, and monitoring performance metrics like accuracy and loss.

### Epoch Accuracy 
![image](https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/0114274b-6a6a-474f-a23d-03df3aeebdf4)

### Epoch Loss
![image](https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/6e54fbee-ad35-4cdc-b781-160802d0c5b4)


### Model Export
After training, the model is saved as [JSON](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/signlanguagedetectionmodel48x48.json) and [`.h5`](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/signlanguagedetectionmodel48x48.h5) files, which you should download to your project directory from your Google Drive.

## Real-Time Detection

### Setup Detection Script
Modify [`realtimedetection.py`](https://github.com/CBJdereal/SignLanguageDetectionCNN/blob/main/src/realtimedetection.py) to update the model path and ensure all paths are correctly set relative to your project structure.
```bash
python ./src/realtimedetection.py
```

### Run Detection
Execute the detection script to start real-time sign language detection using your webcam.

## Troubleshooting
If you encounter issues, you may need to adjust TensorFlow and Keras versions. Here are the versions that were found to be compatible:
- TensorFlow: 2.12
- Keras: Version corresponding to TensorFlow 2.12 compatibility

## Expected Output
<img src="https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/3b8248e3-7b19-4036-a69d-3fe0e6299927" alt="Image 1" width="400" height="300">

<img src="https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/90e9d997-c99a-451d-a5bd-bee4803fcb6b" alt="Image 2" width="400" height="300">

<img src="https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/114df18b-73b5-4ef6-905b-0135b15e0937" alt="Image 3" width="400" height="300">

<img src="https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/f1885853-b2ba-4b47-9a5c-96d56ae50472" alt="Image 4" width="400" height="300">

<img src="https://github.com/CBJdereal/SignLanguageDetectionCNN/assets/64748236/4ff4ebbf-0d6d-4499-b85b-dc1464736ae7" alt="Image 5" width="400" height="300">



