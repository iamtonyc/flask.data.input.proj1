from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	name="Sam"
	age=94
	return render_template('index.html', name=name, age=age)

@app.route("/register", methods=['POST','GET'])
def register():
	if request.method=='POST':
		first_name=request.form['first_name']
		last_name=request.form['last_name']
		gender=request.form['gender']
		country=request.form['country']
		career=request.form['career']
		return render_template('user_details.html', first_name=first_name, last_name=last_name, gender=gender, country=country, career=career)
	else:
		return render_template('register.html')

if __name__ == "__main__":
    app.run()