from flask import Flask, render_template, url_for
app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return render_template('navigationBar.html')

@app.route("/flipLoading")
def flipLoading():
    return render_template('flipLoading.html')

@app.route("/blendMode")
def blendMode():
    return render_template('blendMode.html')

if __name__ == '__main__':
    app.run(debug=True)

