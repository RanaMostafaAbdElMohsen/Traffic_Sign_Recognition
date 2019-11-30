# Traffic_Sign_Recognition_Detection
This repository is for a research project at Cairo University, computer engineering department.

## Note 
This ReadMe must be updated if any installation requirements or prequisities are needed

## DataSet Links
- German Traffic Sign Recognition Benchmark
	- Training Data Set with annotations : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip`
	- Testing Data Set with ground truth annotations : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_GT.zip`

## Installation Requirements
- Clone Project Repo through ssh link using credentials
- Git pull to get most `up-to-date master`
- Set up `Virtual Env` locally or through `Google Collab`
- `pip install -r requirements.txt` for python package installation
- Move DataSet Directory to be `Source_Code/DataSet` folder for consistency

## Before Pushing Code
- Dont forget to update ``requirements.txt`` with new package dependencies using `pip freeze > requirements.txt`
- Create a ``new Branch`` with task description
- Open a PR after commit

## TODO Tasks
- Feature Extraction
	- Segmentation (Rana Mostafa)
	- HSV (Reem AbdElSalam)
- DataSet_Preparation
- Models (Training + Testing)
- Accuracy
- Future Work

## Future Work 
- Trying different data set other German Traffic Sign Recognition Benchmark such as:
	- German Traffic Sign Detection Benchmark
	- DFG traffic sign dataset
- Data Augmentation
- Bounding boxes with background
- Multiple object detection at same image
- More specific categories
- Trying other models

