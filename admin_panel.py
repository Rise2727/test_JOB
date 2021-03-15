from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/')
def index():
    document = open("code.txt")
    content = document.read()


    return content



if __name__ == "__main__":
    app.run(debug=True)
