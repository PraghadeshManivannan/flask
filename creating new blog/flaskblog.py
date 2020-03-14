from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Jarvis',
        'title': 'Day 1',
        'content': 'Flask tutorial - Part 1',
        'date_posted': 'March 13, 2020'
    },
    {
        'author': 'Jarvis',
        'title': 'Day 2',
        'content': 'Flask tutorial - Part 2',
        'date_posted': 'March 14, 2020'
    }
]

post = {
        'name':'Praghadesh',
        'title':'A dirty nerd', 
        'description':'The nerd who is being attracted towards nature and adventure'
    }

blog = {
        'name':'Flask',
        'title':'Flask- Web framework', 
        'description':'The python framework which is used to develop, design the website and also the lighter framework in python.'
    }

@app.route("/")
def homeMain():
    return render_template('homeMain.html', blog=blog,title ='Main')

@app.route("/home")
def home():
    return render_template('home.html', posts=posts,title ='Home')


@app.route("/about")
def about():
    return render_template('about.html',post=post, title='About')


if __name__ == '__main__':
    app.run(debug=True)
