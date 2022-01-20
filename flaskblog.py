from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Rolvy Dicken', 
        'title': 'Before you die',
        'content': 'First post content',
        'date_posted': 'Junuary 20, 2022'
    }, 
    {
        'author': 'Dimitch Grace', 
        'title': 'How to start your year',
        'content': 'Second post content',
        'date_posted': 'Junuary 1, 2022'
    }
]


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)



@app.route("/about")
def hello():
    return render_template('about.html', posts=posts, title="about")


if __name__ == '__main__':
    app.run(debug=True)
