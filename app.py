from flask import Flask, render_template, jsonify

app = Flask(__name__)

List_of_walkers = [{
  "name": "manu",
  "id": "12345",
  "ability": "ice",
  "weapon": "spear"
}, {
  "name": "sussu",
  "id": "1234",
  "ability": "water",
  "weapon": "water gun"
}, {
  "name": "abhi",
  "id": "123",
  "ability": "cola",
  "weapon": "bow"
}, {
  "name": "rupa",
  "id": "12",
  "weapon": "knife"
}, {
  "name": "bangaram",
  "id": "1",
  "ability": "chicken",
  "weapon": "hands"
}]


@app.route("/")
def hello_world():
  return render_template("home.html",
                         owner="Whitewalker",
                         list_of_walkers=List_of_walkers)

@app.route("/api/json")
def list_walkers():
  return jsonify(List_of_walkers)


# bootstrap link =  " https://getbootstrap.com/docs/5.3/getting-started/introduction/ "

# html beginner = " https://htmldog.com/guides/html/beginner/ "

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
