#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle


# In[2]:


vehcostapp=Flask(__name__)
model=pickle.load(open("vehiclecost.pkl","rb"))


# In[3]:


@vehcostapp.route("/")
def home():
    return render_template("index.html")


# In[ ]:





# In[4]:


@vehcostapp.route("/predict",methods=["post"])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction=model.predict(final_features)
    
    output =round(prediction[0],2)
    
    return render_template("index.html",prediction_text="Bike cost should be $ {}".format(output))


# In[5]:


if __name__=="__main__":
 vehcostapp.run(debug=True)

