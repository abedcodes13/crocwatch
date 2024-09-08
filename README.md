*** Croc Watch Project Diagram ***

https://lucid.app/lucidspark/3d376ec2-bb38-4ae0-9b21-a70fd7b0d287/edit?invitationId=inv_9bed6156-f234-4642-9ce5-cdfde7248add

![Screenshot 2024-09-07 232616](https://github.com/user-attachments/assets/9b0a2e2b-e1a3-4b4c-8ea8-40f51c8393b4)

# crocwatch

Crocodile Zone Classification
This project aims to build a machine learning model to classify crocodile sightings into two categories: Management Zone and Outside Management Zone. By using features like species, size, position, and the date of sighting, the model helps predict the zone where the crocodile was spotted.

Overview
The project uses a dataset containing crocodile sightings and their attributes to train a classification model. The goal is to assist in better managing crocodile populations and enhance public safety by accurately predicting whether a sighting occurs in a regulated Management Zone or an Outside Management Zone.

Approach
The classification model is built using a Random Forest Classifier, which is trained on the dataset to predict the zone based on several input features. After training, the model is evaluated using metrics like accuracy and a confusion matrix to determine its effectiveness in predicting the correct zones.

Key Features
Species: Information about the crocodile species.
Size: The length of the crocodile.
Position: The location where the crocodile was sighted (e.g., mid-stream, shallow water).
Date of Sighting: The time at which the crocodile was spotted.
Zone: The target class—either Management Zone or Outside Management Zone.
Outcome
The model successfully classifies most sightings, though some misclassifications occur between zones. The confusion matrix is used to evaluate the accuracy of the model, showing where improvements can be made. This project serves as a step towards better monitoring and management of crocodile populations in key zones.
