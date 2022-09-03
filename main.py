from flask import Flask, render_template, request, url_for, flash, get_flashed_messages
from flask_bootstrap import Bootstrap
from morse import encryption_to_morse, decryption_to_english
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRETKEY")
Bootstrap(app)


@app.route('/', methods=["POST", "GET"])
def home():
    return render_template('index.html')


@app.route('/photography', methods=["POST", "GET"])
def photography():
    return render_template('photography.html')


@app.route('/videography', methods=["POST", "GET"])
def videography():
    return render_template('videography.html')


@app.route('/music', methods=["POST", "GET"])
def music():
    return render_template('music.html')


@app.route('/project', methods=["POST", "GET"])
def project():
    return render_template('project.html')


@app.route('/decryption', methods=["POST", "GET"])
def decryption():
    if request.method == "POST":
        decrypted_data = ""
        data = request.form["decrypted_data"]
        print(data)
        decrypted_data = decryption_to_english(data)
        return render_template('project.html', decryption=True, data=decrypted_data)


@app.route('/encryption', methods=["POST", "GET"])
def encryption():
    if request.method == "GET":

        pass
    else:
        encrypted_data = ""
        data = request.form["encrypted_data"]
        print(data)
        encrypted_data = encryption_to_morse(data)
        print(encrypted_data)

        return render_template('project.html', decryption=False, data=encrypted_data)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
