[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"
[image2]: ./images/vgg16_model.png "VGG-16 Model Keras Layers"
[image3]: ./images/vgg16_model_draw.png "VGG16 Model Figure"


## Project Overview

Welcome to the Convolutional Neural Networks (CNN) project in the AI Nanodegree! In this project, you will learn how to build a pipeline that can be used within a web or mobile app to process real-world, user-supplied images.  Given an image of a dog, your algorithm will identify an estimate of the canine’s breed.  If supplied an image of a human, the code will identify the resembling dog breed.  

![Sample Output][image1]

Along with exploring state-of-the-art CNN models for classification, you will make important design decisions about the user experience for your app.  Our goal is that by completing this lab, you understand the challenges involved in piecing together a series of models designed to perform various tasks in a data processing pipeline.  Each model has its strengths and weaknesses, and engineering a real-world application often involves solving many problems without a perfect answer.  Your imperfect solution will nonetheless create a fun user experience!


## Project Instructions

### Instructions

1. Clone the repository and navigate to the downloaded folder.
	
	```	
		git clone https://github.com/udacity/dog-project.git
		cd dog-project
	```
2. Download the [dog dataset](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip).  Unzip the folder and place it in the repo, at location `path/to/dog-project/dogImages`. 
3. Download the [human dataset](http://vis-www.cs.umass.edu/lfw/lfw.tgz).  Unzip the folder and place it in the repo, at location `path/to/dog-project/lfw`.  If you are using a Windows machine, you are encouraged to use [7zip](http://www.7-zip.org/) to extract the folder. 
4. Donwload the [VGG-16 bottleneck features](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogVGG16Data.npz) for the dog dataset.  Place it in the repo, at location `path/to/dog-project/bottleneck_features`.
5. Obtain the necessary Python packages, and switch Keras backend to Tensorflow.  
	
	For __Mac/OSX__:
	```
		conda env create -f requirements/aind-dog-mac.yml
		source activate aind-dog
		KERAS_BACKEND=tensorflow python -c "from keras import backend"
	```

	For __Linux__:
	```
		conda env create -f requirements/aind-dog-linux.yml
		source activate aind-dog
		KERAS_BACKEND=tensorflow python -c "from keras import backend"
	```

	For __Windows__:
	```
		conda env create -f requirements/aind-dog-windows.yml
		activate aind-dog
		set KERAS_BACKEND=tensorflow
		python -c "from keras import backend"
	```
6. Open the notebook and follow the instructions.
	
	```
		jupyter notebook dog_app.ipynb
	```

__NOTE:__ While some code has already been implemented to get you started, you will need to implement additional functionality to successfully answer all of the questions included in the notebook. __Unless requested, do not modify code that has already been included.__


## Amazon Web Services

Instead of training your model on a local CPU (or GPU), you could use Amazon Web Services to launch an EC2 GPU instance.  Please refer to the [Udacity instructions](https://classroom.udacity.com/nanodegrees/nd889/parts/16cf5df5-73f0-4afa-93a9-de5974257236/modules/53b2a19e-4e29-4ae7-aaf2-33d195dbdeba/lessons/2df3b94c-4f09-476a-8397-e8841b147f84/project) for setting up a GPU instance for this project.


## Evaluation

Your project will be reviewed by a Udacity reviewer against the CNN project [rubric](#rubric).  Review this rubric thoroughly, and self-evaluate your project before submission.  All criteria found in the rubric must meet specifications for you to pass.


## Project Submission

When you are ready to submit your project, collect the following files and compress them into a single archive for upload:
- The `dog_app.ipynb` file with fully functional code, all code cells executed and displaying output, and all questions answered.
- An HTML or PDF export of the project notebook with the name `report.html` or `report.pdf`.
- Any additional images used for the project that were not supplied to you for the project. __Please do not include the project data sets in the `dogImages/` or `lfw/` folders.  Likewise, please do not include the `bottleneck_features/` folder.__

Alternatively, your submission could consist of the GitHub link to your repository.


<a id='rubric'></a>
## Project Rubric

#### Files Submitted

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| Submission Files      | The submission includes all required files.		|

#### Documentation

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| Comments         		| The submission includes comments that describe the functionality of the code.  	|

#### Step 1: Detect Humans

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| __Question 1:__ Assess the Human Face Detector |  The submission returns the percentage of the first 100 images in the dog and human face datasets with a detected human face.          |
| __Question 2:__ Assess the Human Face Detector |  The submission opines whether Haar cascades for face detection are an appropriate technique for human detection.    |

#### Step 2: Detect Dogs

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| __Question 3:__ Assess the Dog Detector |  The submission returns the percentage of the first 100 images in the dog and human face datasets with a detected dog.          |

#### Step 3: Create a CNN to Classify Dog Breeds (from Scratch)

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| Model Architecture | The submission specifies a CNN architecture. |
| Train the Model | The submission specifies the number of epochs used to train the algorithm. |
| Test the Model | The trained model attains at least 1% accuracy on the test set. |


#### Step 5: Create a CNN to Classify Dog Breeds (using Transfer Learning)

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| Obtain Bottleneck Features | The submission downloads the bottleneck features corresponding to one of the Keras pre-trained models (VGG-19, ResNet-50, Inception, or Xception). |
| Model Architecture | The submission specifies a model architecture.  |
| __Question 5__: Model Architecture | The submission details why the chosen architecture succeeded in the classification task and why earlier attempts were not as successful.  |
| Compile the Model | The submission compiles the architecture by specifying the loss function and optimizer. |
| Train the Model    | The submission uses model checkpointing to train the model and saves the model with the best validation loss. |
| Load the Model with the Best Validation Loss    | The submission loads the model weights that attained the least validation loss. |
| Test the Model    | Accuracy on the test set is 60% or greater. |
| Predict Dog Breed with the Model | The submission includes a function that takes a file path to an image as input and returns the dog breed that is predicted by the CNN. |


#### Step 6: Write your Algorithm

| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| Write your Algorithm   | The submission uses the CNN from Step 5 to detect dog breed.  The submission has different output for each detected image type (dog, human, other) and provides either predicted actual (or resembling) dog breed. |

#### Step 7: Test your Algorithm
| Criteria       		|     Meets Specifications	        			            | 
|:---------------------:|:---------------------------------------------------------:| 
| Test Your Algorithm on Sample Images!   | The submission tests at least 6 images, including at least two human and two dog images. |
| __Question 6__: Test Your Algorithm on Sample Images! | The submission discusses performance of the algorithm and discusses at least three possible points of improvement. |
