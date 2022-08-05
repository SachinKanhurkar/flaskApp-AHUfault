from flask import Flask, request, render_template
import pandas as pd
#from sklearn import preprocessing
#from sklearn.preprocessing import StandardScaler 
import joblib


# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("finalized_model_AHUFault.pkl")
        
        # Get values through input bars
        AHU_SAT = request.form.get("AHU: Supply Air Temperature")
        AHU_SATP = request.form.get("AHU: Supply Air Temperature Set Point")
        AHU_OAT = request.form.get("AHU: Outdoor Air Temperature")
        AHU_MAT = request.form.get("AHU: Mixed Air Temperature")
        AHU_RAT = request.form.get("AHU: Return Air Temperature")
        AHU_SAF = request.form.get("AHU: Supply Air Fan Status")
        AHU_RAFS = request.form.get("AHU: Return Air Fan Status")
        AHU_SAFSCS = request.form.get("AHU: Supply Air Fan Speed Control Signal")
        AHU_RAFSCS = request.form.get("AHU: Return Air Fan Speed Control Signal")
        AHU_OADCS = request.form.get("AHU: Outdoor Air Damper Control Signal")
        AHU_RADCS = request.form.get("AHU: Return Air Damper Control Signal")
        AHU_CCVCS = request.form.get("AHU: Cooling Coil Valve Control Signal")
        AHU_HCVCS= request.form.get("AHU: Heating Coil Valve Control Signal")
        AHU_SADSPSP = request.form.get("AHU: Supply Air Duct Static Pressure Set Point")
        AHU_SADSP = request.form.get("AHU: Supply Air Duct Static Pressure")
        AHU_Occ = request.form.get("Occupancy Mode Indicator")

        l1= ['AHU: Supply Air Temperature',
         'AHU: Supply Air Temperature Set Point',
         'AHU: Outdoor Air Temperature',
         'AHU: Mixed Air Temperature',
         'AHU: Return Air Temperature', 
         'AHU: Supply Air Fan Status',
         'AHU: Return Air Fan Status',
         'AHU: Supply Air Fan Speed Control Signal',
         'AHU: Return Air Fan Speed Control Signal',
         'AHU: Outdoor Air Damper Control Signal  ',
         'AHU: Return Air Damper Control Signal',
         'AHU: Cooling Coil Valve Control Signal',
         'AHU: Heating Coil Valve Control Signal',
         'AHU: Supply Air Duct Static Pressure Set Point',
         'AHU: Supply Air Duct Static Pressure',
         'Occupancy Mode Indicator']
        # Put inputs to dataframe       

        X = pd.DataFrame([[AHU_SAT , AHU_SATP , AHU_OAT ,AHU_MAT , AHU_RAT , AHU_SAF ,AHU_RAFS , AHU_SAFSCS ,AHU_RAFSCS , AHU_OADCS ,
        AHU_RADCS ,
        AHU_CCVCS ,
        AHU_HCVCS,
        AHU_SADSPSP ,
        AHU_SADSP, AHU_Occ ]], columns =l1)

        print (X)        
        n = len(l1)
        print(n)
        arr = X.values        
        X_arr = arr[:,0:n]
        print(X_arr)
        # Get prediction
        #feature Scaling  
   
        #st_x= StandardScaler()    
        #X_t= st_x.fit_transform(X_arr) 
        #print(X_t)
        prediction = clf.predict(X_arr)[0]
        print(prediction)
        
    else:
        prediction = ""
    if prediction==1:    
        return render_template("website.html", output_text ="Status: AHU is in fauly mode.")
    else:
        return render_template("website.html", output_text =" Status: AHU is working in good condition.")

# Running the app
if __name__ == '__main__':
    app.run(debug = True)