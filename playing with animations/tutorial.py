from flask import Flask, render_template, url_for
app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
    return render_template('navigationBar.html',css=url_for('static',filename = 'navigationBar.css'))

@app.route("/flipLoading")
def flipLoading():
    return render_template('flipLoading.html',css=url_for('static',filename = 'flipLoading.css'))

@app.route("/glowingText")
def glowingText():
    return render_template('glowingText.html',css= url_for('static',filename = 'glowingText.css') )

@app.route("/gradientText")
def gradientText():
    return render_template('gradientText.html',css= url_for('static',filename = 'gradientText.css') )

@app.route("/loaderAnimation")
def loaderAnimation():
    return render_template('loaderAnimation.html',css= url_for('static',filename = 'loaderAnimation.css') )

@app.route("/typingEffect")
def typingEffect():
    return render_template('typingEffect.html',css= url_for('static',filename = 'typingEffect.css') )

if __name__ == '__main__':
    app.run(debug=True)

