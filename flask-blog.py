from importlib.resources import contents
from forms import RegistrationForm,LoginForm
from flask import Flask,render_template,url_for
app = Flask(__name__)

app.config['SECRET_KEY'] ='4db77598290f06523456cafce29ac3d9'


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog posts 1',
        'content':'First Post Content',
        'Date Posted': 'April 20th,2015'
    },
        {
        'author': 'Edah Schoffieldr',
        'title': 'Blog post 2',
        'content':'Second Post Content Post Content',
        'Date Posted': 'April 20th,2015'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title = "about")

@app.route("/contact_us/")
def contact_us():
     return "<h1> Contact us page </h1>"
 
@app.route("/register/")
def register():
    form = RegistrationForm()
    return render_template("register.html",title = "Registration", form=form)

@app.route("/login/")
def login():
    form = RegistrationForm()
    return render_template("register.html",title = "login", form=form)


if __name__ == "__main__":
    app.run(debug=True)