from flask import Flask,render_template,request,url_for
import pickle,joblib
import pandas as pd 
app=Flask(__name__)

model = pickle.load(open("Scaler2.pkl", "rb"))
ct=joblib.load('feature_values')


@app.route('/')
def home():
    return render_template("home.html")
@app.route('/pred')
def pred():
    return render_template("index.html")

@app.route('/output', methods=["POST"])
 
def output():

  age=request.form["a"]
  gender=request.form["b"]
  country=request.form["c"]
  state=request.form["d"]
  self_employed=request.form["e"]
  family_history=request.form["f"]
  work_interfere= request.form["g"]
  no_employees=request.form["h"]
  remote_work=request.form["i"]
  tech_company=request.form["j"]
  benefits=request.form["k"]
  care_options=request.form["l"]
  wellness_program =request.form["m"]
  seek_help=request.form["n"]
  anonymity= request.form["o"]
  leave=request.form["p"]
  mental_health_consequence=request.form["q"]
  phys_health_consequence = request.form["r"]
  coworkers=request.form["s"]
  supervisor= request.form["t"]
  mental_health_interview=request.form["u"]
  phys_health_interview= request. form[ "v"]
  mental_vs_physical=request.form["w"]
  obs_consequence=request.form["x"]
  comments = request.form["y"]
  data = [[age,gender, country, state, self_employed, family_history,work_interfere,no_employees, remote_work, 
           tech_company, benefits, care_options, wellness_program,seek_help,anonymity, leave, 
          mental_health_consequence,phys_health_consequence, coworkers, supervisor,
          mental_health_interview,phys_health_interview, mental_vs_physical,obs_consequence, comments]]
  feature_cols=['Age', 'Gender', 'Country', 'State', 'self_employed', 'family_history'
              ,'work_interfere','no_employees', 'remote_work', 'tech_company',
              'benefits', 'care_options', 'wellness_program', 'seek_help',
              'anonymity', 'Leave', 'mental_health_consequence',
              'phys_health_consequence', 'coworkers', 'supervisor', 
              'mental_health_interview', 'phys_health_interview',
              'mental_vs_physical', 'obs_consequence', 'comments']

  #pred=model.predict(ct.transform(pd.DataFrame(data,columns=feature_cols)))
  #pred=model.predict(ct.transform(pd.DataFrame(data)))
  pred = model.predict(data)
  pred = pred[0]
  if pred:
       return render_template("output.html",y="This person requires mental health treatment ")
  else: 
       return render_template("output.html",y="This person doesn't require mental health treatment")
  

if __name__ =="__main__":
   app.run(debug=True)