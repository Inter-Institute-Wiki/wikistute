from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/institutes")
def institutes():
	return render_template("institutes.html")

@app.route("/contribute")
def contribute():
	return render_template("contribute.html")

@app.route("/iisertvm")
def iisertvm():
	return render_template("iisers/iisertvm.html")

app.run(debug=True)