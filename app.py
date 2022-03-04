#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)


# In[2]:


from flask import render_template, request
import joblib
                    
@app.route("/", methods =["GET","POST"])
def index ():
    
    if request.method =="POST":
        dividend = request.form.get("dividend")
        netg = request.form.get("netg")
        shareg = request.form.get("shareg")
        dividend = float (dividend)
        netg = float (netg)
        shareg = float (shareg)
        print(dividend, netg, shareg) 
        
        model1 = joblib.load("Equity_DT")
        pred1 = model1.predict([[dividend, netg, shareg]])
        s1 = "The Class of the Equity base on Decision Tree model is : " + str(pred1)          
  
        model2 = joblib.load("Equity_Reg")
        pred2 = model2.predict([[dividend, netg, shareg]])
        s2 = "The Class of the Equity base on Linear Regression model is : " + str(pred2)  
        
        model3 = joblib.load("Equity_NN")
        pred3 = model3.predict([[dividend, netg, shareg]])
        s3 = "The Class of the Equity base on Neural Network model is : " + str(pred3)  
        
        return(render_template("index.html", result1 =s1, result2 = s2,result3 =s3))
    else:
        return(render_template("index.html", result1 ="2", result2 ="2",result3 ="2"))


# In[ ]:


if __name__== "__main__":
    app.run()


# In[ ]:




