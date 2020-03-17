from flask import Flask, render_template, url_for
app = Flask(__name__)




@app.route("/")
@app.route("/flipLoading")
def homeMain():
    return render_template('flipLoading.html')

if __name__ == '__main__':
    app.run(debug=True)

