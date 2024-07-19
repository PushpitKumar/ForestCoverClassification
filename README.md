## Table of Contents
* Overview/Problem Statement
* Dataset
* File Structure
* Major Packages/Libraries Used
* Installation/Working Environment
* Building the Web App
* App Implementation
* Drawbacks and Future Scope

### 1. Overview/Problem Statement
* Ever wondered how different type of trees grow in which environment? With annual surge in deforestation, knowing the forest cover is beneficial for saving the environment.
* For this problem, classification algorithms such as Logistic Regression, KNN and RandomForest were implemented. RandomForest performed the best!

### 2. Dataset
* This dataset contains tree observations from four areas of the Roosevelt National Forest in Colorado. All observations are cartographic variables (no remote sensing) from 30 meter x 30 meter sections of forest. There are over half a million measurements total!
* This dataset includes information on tree type, shadow coverage, distance to nearby landmarks (roads etcetera), soil type, and local topography.
* CoverType is the target variable and has a total of 7 different tree types namely, Aspen, Cottonwood/Willow, Douglas/Fir, Krummholz, LodgePole Pine, Ponderosa Pine and Spruce/Fir.
* The dataset is available on Kaggle and the link is provided below.
* [Dateset Link](https://www.kaggle.com/datasets/uciml/forest-cover-type-dataset/data)

### 3. File Structure
```
├── static
│   ├── forest.jpg
├── templates
    ├── home.html
├── .gitattributes
├── Notebook.ipynb
├── README.md
├── app.py
├── forest.pkl
├── requirements.txt
```

### 4. Major Packages/Libraries Used
* pandas 
* numpy
* sci-kit learn
* matplotlib
* seaborn
* Flask
* gunicorn

### 5. Installation/Working Environment
Follow the instructions if you want to run the app from your local computer.
* The app is written using **Python 3.9.5**. You can download it from [here](https://www.python.org/downloads/).You can also download **Anaconda** which is a distribution of python from [here](https://www.anaconda.com/products/individual). I would recommend downloading anaconda since it is very useful as it comes with a lot of python libraries, Jupyter and Spyder IDE.
* Once you are done with the installation, you can clone this repository to your computer and install the required packages and libraries using the following line of code through the command prompt where your local environment is setup.
```
pip install -r requirements.txt
```
### 6. Building the Web App
* The web-app was developed using flask micro web framework which is written in python, suitable for small scale projects such as this one. For more information you can check the offical flask website by clicking [here](https://flask.palletsprojects.com/en/2.0.x/)
* Basic HTML was needed for designing the web-app and to make sure it was responsive to user inputs. 

### 7. App Implementation  
* The app asks for user to enter the forest observations recorded by officials in Roosevelt National Park, Colorado, which included features such as Elevation, Aspect, Slope, Hillshade etc. Based on these inputs, the type of tree gets classified.

<img width="936" alt="Screenshot 2024-07-20 011710" src="https://github.com/user-attachments/assets/d1377d54-f3a4-4bce-92d8-4c503c374912">
<img width="938" alt="Screenshot 2024-07-20 012025" src="https://github.com/user-attachments/assets/174ec187-cecc-475b-aa79-f843083e34e2">

### 8. Drawbacks and Future Scope
* Although the web app has been successfully developed, I'm unable to deploy it on Heroku as they have removed free tier support.
* Complete removal of outliers has shown to yield best results and same can be implemented in this problem.
