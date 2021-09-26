from flask import Flask, render_template, request
from flask_cors import cross_origin
import requests
import pickle

app = Flask(__name__)
model = pickle.load(open('forest.pkl','rb'))

@app.route('/',methods=['GET'])
@cross_origin()
def Home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        #Elevation
        Elevation = int(request.form['Elevation'])

        #Aspect
        Aspect = int(request.form['Aspect'])

        #Slope
        Slope = int(request.form['Slope'])

        #Distance to Hydrology
        Distance_To_Hydrology = int(request.form['Distance_To_Hydrology'])

        #Horizontal Distance to Roadways
        Horizontal_Distance_To_Roadways = int(request.form['Horizontal_Distance_To_Roadways'])

        #Hillshade Noon
        Hillshade_Noon = int(request.form['Hillshade_Noon'])

        #Hillshade_3pm
        Hillshade_3pm = int(request.form['Hillshade_3pm'])

        #Horizontal Distance to Firepoints
        Horizontal_Distance_To_Fire_Points = int(request.form['Horizontal_Distance_To_Fire_Points'])

        #Wilderness Area
        Wilderness_Area = request.form['Wilderness_Area']

        if Wilderness_Area == 'Rawah Wilderness Area':
            Wilderness_Area1 = 1
            Wilderness_Area2 = 0
            Wilderness_Area3 = 0
            Wilderness_Area4 = 0
        elif Wilderness_Area == 'Neota Wilderness Area':
            Wilderness_Area1 = 0
            Wilderness_Area2 = 1
            Wilderness_Area3 = 0
            Wilderness_Area4 = 0
        elif Wilderness_Area == 'Comanche Peak Wilderness Area':
            Wilderness_Area1 = 0
            Wilderness_Area2 = 0
            Wilderness_Area3 = 1
            Wilderness_Area4 = 0
        elif Wilderness_Area == 'Cache la Poudre Wilderness Area':
            Wilderness_Area1 = 0
            Wilderness_Area2 = 0
            Wilderness_Area3 = 0
            Wilderness_Area4 = 1

        #Soil Types
        Soil_Type = request.form['Soil_Type']

        if Soil_Type == 'Type1':
            Soil_Type1 = 1
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type2':
            Soil_Type1 = 0
            Soil_Type2 = 1
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type3':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 1
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type4':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 1
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type5':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 1
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type6':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 1
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type9':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 1
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type10':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 1
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type11':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 1
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type12':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 1
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type13':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 1
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type16':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 1
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type17':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 1
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type18':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 1
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type19':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 1
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type20':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 1
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type22':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 1
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type23':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 1
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type24':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 1
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type26':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 1
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type27':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 1
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type29':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 1
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type30':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 1
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type31':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 1
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type32':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 1
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type33':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 1
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type34':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 1
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type35':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 1
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type38':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 1
            Soil_Type39 = 0
            Soil_Type40 = 0

        elif Soil_Type == 'Type39':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 1
            Soil_Type40 = 0

        elif Soil_Type == 'Type40':
            Soil_Type1 = 0
            Soil_Type2 = 0
            Soil_Type3 = 0
            Soil_Type4 = 0
            Soil_Type5 = 0
            Soil_Type6 = 0
            Soil_Type9 = 0
            Soil_Type10 = 0
            Soil_Type11 = 0
            Soil_Type12 = 0
            Soil_Type13 = 0
            Soil_Type16 = 0
            Soil_Type17 = 0
            Soil_Type18 = 0
            Soil_Type19 = 0
            Soil_Type20 = 0
            Soil_Type22 = 0
            Soil_Type23 = 0
            Soil_Type24 = 0
            Soil_Type26 = 0
            Soil_Type27 = 0
            Soil_Type29 = 0
            Soil_Type30 = 0
            Soil_Type31 = 0
            Soil_Type32 = 0
            Soil_Type33 = 0
            Soil_Type34 = 0
            Soil_Type35 = 0
            Soil_Type38 = 0
            Soil_Type39 = 0
            Soil_Type40 = 1

        features = [[Elevation,
                 Aspect,
                 Slope,
                 Distance_To_Hydrology,
                 Horizontal_Distance_To_Roadways,
                 Hillshade_Noon,
                 Hillshade_3pm,
                 Horizontal_Distance_To_Fire_Points,
                 Wilderness_Area1,
                 Wilderness_Area2,
                 Wilderness_Area3,
                 Wilderness_Area4,
                 Soil_Type1,
                 Soil_Type2,
                 Soil_Type3,
                 Soil_Type4,
                 Soil_Type5,
                 Soil_Type6,
                 Soil_Type9,
                 Soil_Type10,
                 Soil_Type11,
                 Soil_Type12,
                 Soil_Type13,
                 Soil_Type16,
                 Soil_Type17,
                 Soil_Type18,
                 Soil_Type19,
                 Soil_Type20,
                 Soil_Type22,
                 Soil_Type23,
                 Soil_Type24,
                 Soil_Type26,
                 Soil_Type27,
                 Soil_Type29,
                 Soil_Type30,
                 Soil_Type31,
                 Soil_Type32,
                 Soil_Type33,
                 Soil_Type34,
                 Soil_Type35,
                 Soil_Type38,
                 Soil_Type39,
                 Soil_Type40]]

        prediction = model.predict(features)
        result = prediction[0]

        return render_template('home.html',prediction_text='Type of Forest Cover: {}'.format(result))

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
