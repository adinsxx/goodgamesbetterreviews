from flask import Flask, send_from_directory, send_file

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/getbanana")
def getbanana():
    return "http://humphris.com.au/wp-content/uploads/2015/06/Banana-Pisang-Ceylan.jpg"
@app.route("/getbread")
def getbread():
    return "https://images.heb.com/is/image/HEBGrocery/prd-small/h-e-b-bakery-asiago-cheese-bread-scratch-made-001121246.jpg"

if __name__ == "__main__":
    app.run(debug=True)