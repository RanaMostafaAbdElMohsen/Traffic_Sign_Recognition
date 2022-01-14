# RIECNN : Real-time Image Enhanced CNN
This repository is for a research project at Cairo University, computer engineering department.
This paper introduces [RIECNN: real-time image enhanced CNN for traffic sign recognition](https://link.springer.com/content/pdf/10.1007/s00521-021-06762-5.pdf) is published in `Neural Computing and Applications Journal, Springer 2022`. 

## Abstract
Traffic sign recognition plays a crucial role in the development of autonomous cars to reduce the accident rate and promote
road safety. It has been a necessity to address traffic signs that are affected significantly by the environment as well as poor
real-time performance for deep-learning state-of-the-art algorithms. In this paper, we introduce Real-Time Image
Enhanced CNN (RIECNN) for Traffic Sign Recognition. RIECNN is a real-time, novel approach that tackles multiple,
diverse traffic sign datasets, and out-performs the state-of-the-art architectures in terms of recognition rate and execution
time. Experiments are conducted using the German Traffic Sign Benchmark (GTSRB), the Belgium Traffic Sign Clas-
sification (BTSC), and the Croatian Traffic Sign (rMASTIF) benchmark. Experimental results show that our approach has
achieved the highest recognition rate for all Benchmarks, achieving a recognition accuracy of 99.75% for GTSRB, 99.25%
for BTSC and 99.55% for rMASTIF. In terms of latency and meeting the real-time constraint, the pre-processing time and
inference time together do not exceed 1.3 ms per image. Not only have our proposed approach achieved remarkably high
accuracy with real-time performance, but it also demonstrated robustness against traffic sign recognition challenges such as
brightness and contrast variations in the environment.

## Note 
This ReadMe must be updated if any installation requirements or prequisities are needed

## DataSet Links
- German Traffic Sign Recognition Benchmark
	- Training Data Set images with annotations : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip`
	- Testing Data Set's ground truth annotations : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_GT.zip`
	- Testing Data Set images : `https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_Images.zip`

- Belgium Traffic Sign Recognition `https://btsd.ethz.ch/shareddata/`

## Access Ready DataSet .pkl files
You can access German and Belgium train and test `.pkl` files for winning models through this [link](https://drive.google.com/drive/folders/1Dq6b6-6mwbSkg2uZQbqUIwDVF42-qHL-?usp=sharing)

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

## Presentation Link
Presentation Link : [Here](https://docs.google.com/presentation/d/1O_aPwO1tJeqlp8H9RqbSJ8LoRy_o92LyCpXuD8ssBBo/edit?usp=sharing)
