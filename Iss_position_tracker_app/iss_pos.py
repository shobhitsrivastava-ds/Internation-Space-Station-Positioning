from flask import Flask,render_template,redirect,url_for,request
import wed
import requests

app=Flask(__name__,template_folder='template')

@app.route("/")
def home():
	return(render_template("home.html"))

@app.route("/form",methods=["POST","GET"])
def form():
	return(render_template("form.html"))

@app.route("/about",methods=["POST","GET"])
def about():
	return(render_template("about.html"))

#@app.route("/success")
#def success(data):
#	return(render_template("success.html",data=data))

def find_data():
		url = "http://api.open-notify.org/iss-now.json"
		data = requests.get(url).json()
		lat=data["iss_position"]["latitude"]
		lon=data["iss_position"]["longitude"]		
		return(lon,lat)

@app.route("/weather",methods=["GET","POST"])
def weather():
	if(request.method=="POST"):
		lon,lat = find_data()
	return render_template("success.html",lon=lon,lat=lat)


if __name__=="__main__":
	app.run(debug=True)

"""app1=wea(str(city))
		data = app1.find_data()
	return render_template("success.html",data=data)"""