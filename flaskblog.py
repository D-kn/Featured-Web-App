from flask import Flask, render_template, url_for, flash, redirect  
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'd8937da7edc9c7452ae99bdcaec96e88'


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
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title="about")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password': #just for a fake log in
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
