from flask import Flask,render_template,request
import pickle 
import numpy as np
model=pickle.load(open('result.pkl','rb'))

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST'])
def login():
    c1=request.form['c1']
    c2=request.form['c2']
    c3=request.form['c3']
    c4=request.form['c4']
    c5=request.form['c5']
    c6=request.form['c6']
    c7=request.form['c7']
    c8=request.form['c8']
    c9=request.form['c9']
    c10=request.form['c10']
    c11=request.form['c11']
    c12=request.form['c12']
    c13=request.form['c13']
    c14=request.form['c14']
    c15=request.form['c15']
    c16=request.form['c16']
    c17=request.form['c17']
    c18=request.form['c18']
    c19=request.form['c19']
    c20=request.form['c20']
    c21=request.form['c21']
    c22=request.form['c22']
    c23=request.form['c23']
    c24=request.form['c24']
    c25=request.form['c25']
    c26=request.form['c26']
    c27=request.form['c27']
    c28=request.form['c28']
    c29=request.form['c29']
    c30=request.form['c30']
    result=[[int(c1),int(c2),int(c3),int(c4),int(c5),int(c6),int(c7),int(c8),int(c9),int(c10),int(c11),int(c12),int(c13),int(c14),int(c15),int(c16),int(c17),int(c18),int(c19),int(c20),int(c21),int(c22),int(c23),int(c24),int(c25),int(c26),int(c27),int(c28),int(c29),int(c30)]]
    y_pred=model.predict(result)
    print(y_pred)
    if y_pred==[1]:
        return render_template("index.html",showcase="This is a Legitimate Website")
    elif y_pred==[-1]:
        return render_template("index.html",showcase="This is a Phishing Website")
    elif y_pred==[0]:
        return render_template("index.html",showcase="This is a Suspicious Website")
    else:
        return render_template("index.html",showcase="This is a Phishing Website")

if __name__=='__main__':
    app.run(debug=True)