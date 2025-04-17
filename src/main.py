# Develop a simple contact form application with input fields for Name, Email, and Message. The submitted data should be securely stored in a database. Ensure the implementation follows best practices for backend development, including data validation and error handling.


from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = "secret key"


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    recaptcha = RecaptchaField()


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("nm")
        return redirect(url_for("success", name=user))


def contact():
    form = ContactForm()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
