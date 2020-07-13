# Traffic_Sign_Recognition
This repository is for a research project at Cairo University, computer engineering department.

## Note 
This ReadMe must be updated if any installation requirements or prequisities are needed

## DataSet Links
- German Traffic Sign Recognition Benchmark
	- Training Data Set images with annotations : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip`
	- Testing Data Set's ground truth annotations : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_GT.zip`
	- Testing Data Set images : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_Images.zip`

- Belgium Traffic Sign Recognition `https://btsd.ethz.ch/shareddata/`

## Installation Requirements
- Clone Project Repo through ssh link using credentials
- Git pull to get most `up-to-date master`
- Set up `Virtual Env` locally or through `Google Collab`
- `pip install -r requirements.txt` for python package installation
- Move DataSet Directory to be `Source_Code/DataSet` folder for consistency
	- Training Data_Set to be : ``Source_Code/DataSet/Training_DataSet``
	- Testing Data_Set to be : ``Source_Code/DataSet/Testing_DataSet``
	- Please ignore .txt files in each directory : made only to commit both folders
- For `Belgium` DataSet Move DataSet to be in `Source_Code/DataSet`
	- Belgium Training Data_Set to be : ``Source_Code/DataSet/BelgiumTSC_Training/Training``
	- Belgium Testing Data_Set to be : ``Source_Code/DataSet/BelgiumTSC_Testing/Testing``
	- Please remove readMe.txt files inside ``Training`` and ``Testing`` Folders or else loading will ``fail``
- Move pkl files to `Source_Code/Model/Processed_DataSet` folder for consistency
	- `TrainDataSet.pkl` and `TestDataSet.pkl` files
	
## Before Pushing Code
- Dont forget to update ``requirements.txt`` with new package dependencies using `pip freeze > requirements.txt`
- Create a ``new Branch`` with task description
- Open a `PR` after commit

## Presentation Link
Presentation Link : `https://docs.google.com/presentation/d/1O_aPwO1tJeqlp8H9RqbSJ8LoRy_o92LyCpXuD8ssBBo/edit?usp=sharing`
