from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('RFC.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        gender_Male =(request.form['gender_Male'])
        if(gender_Male == 'male'):
                gender_Male = 1
                 
        
        else:
            gender_Male = 0
            
        
        age = int(request.form['age'])
        
        hypertension = (request.form['hypertension'])           
        if(hypertension =='yes'):
                hypertension =1
        
        elif(hypertension == 'no'):
            hypertension =0
        
        heart_disease = (request.form['heart_disease'])
        if(heart_disease =='yes'):
           heart_disease =1
        
        elif(heart_disease == 'no'):
            heart_disease =0
         
            
        ever_married  = (request.form['ever_married'])
        if(ever_married =='yes'):
           ever_married =1
        
        elif(ever_married == 'no'):
            ever_married =0
            
        Residence_type = (request.form['Residence_type'])
        if(Residence_type =='Urban'):
           Residence_type =1
        
        elif(Residence_type == 'Rural'):
            Residence_type =0
        
        
        
        avg_glucose_level = float(request.form['avg_glucose_level'])
        
        bmi = float(request.form['bmi'])
       
        work_type=request.form['work_type']
        if(work_type=='Private'):
                work_type_Never_worked =0
                work_type_Private= 1
                work_type_Self_employed= 0
                work_type_children= 0
        if(work_type=='Self_employed'):
            work_type_Never_worked =0
            work_type_Private =0
            work_type_Self_employed= 1
            work_type_children= 0     
        
        if(work_type=='Never_worked'):
            work_type_Never_worked =1
            work_type_Private =0
            work_type_Self_employed= 0
            work_type_children= 0   
        if(work_type=='children'):
            work_type_Never_worked =0
            work_type_Private =0
            work_type_Self_employed= 0
            work_type_children= 1
        
        else:
            work_type_Never_worked =0
            work_type_Private =0
            work_type_Self_employed= 0
            work_type_children= 0
            
        smoking_status = request.form['smoking_status']           
        if(smoking_status=='never_smoked'):
            smoking_status_never_smoked =1
            smoking_status_smokes =0
            
        elif(smoking_status=='smokes'):
            smoking_status_never_smoked =0
            smoking_status_smokes =1
            
        else:
            smoking_status_never_smoked =0
            smoking_status_smokes =0
            
            
        prediction = model.predict([[age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,gender_Male,work_type_Never_worked,work_type_Private,work_type_Self_employed,work_type_children,smoking_status_never_smoked,smoking_status_smokes]])
       
        if prediction == 0:
            return render_template('index.html',prediction_text="You do not have possibility of brain stroke")
        else:
            return render_template('index.html',prediction_text="Please take care of your health you have possibility of Brain Stroke")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


