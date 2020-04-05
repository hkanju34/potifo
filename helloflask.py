from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/<string:page_name>')
def htm_page(page_name):
    return render_template(page_name)

def write_data(data):
	with open("database.txt", mode="a") as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f"\n{email},{subject},{message},")

def write_csv(data):
	with open("database.csv", "a", newline = '') as database2:
		
		fieldnames = ['email','subject','message']
		writer = csv.DictWriter(database2, fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerow(data)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		write_csv(data)
		return redirect("/thanks.html")
	else:
		return "something wrong with the form!"
    