from flask import Flask, render_template, request, url_for

app = Flask("my_first_app")

@app.route("/")
def say_hello():
  return render_template("index.html") #change filename for future pages

@app.route("/<name>")
def say_hello_to(name):
  return render_template("hello.html", user=name)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values["name"]

  return render_template("feedback.html", form_data=data)

app.run(debug=True)
