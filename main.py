from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')
port = 5000


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port, debug=True)