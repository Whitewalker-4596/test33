from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("home.html")


# bootstrap link =  " https://getbootstrap.com/docs/5.3/getting-started/introduction/ "

# html beginner = " https://htmldog.com/guides/html/beginner/ "


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
