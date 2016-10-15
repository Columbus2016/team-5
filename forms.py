from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(Form):
    firstname = TextField(u'First Name', validators=[Required()])
    lastname = TextField(u'Last Name', validators=[Required()])
    password = PasswordField(u'Password', validators=[Required()])
    email = TextField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday', validators=[Required()])
    gender = RadioField(u'Gender', choices=[('Male', 'male'), ('Female', 'female')], validators=[Required()])
    zipcode = IntegerField(u'Zip Code (so we can connect you with nearby users!)', validators=[Required()])
    community = SelectField(u'Cancer Community', choices=[('Survivor', 'survivor'), ('Co-Survivor', 'cosurvivor'), ('Metastatic', 'metastatic')])

    sample_file = FileField(u'Upload a Profile Picture!')

    eula = BooleanField(u'I agree to let my personal data be released for research purposes',
                        validators=[Required('You must agree to not agree!')])

    submit = SubmitField(u'Signup')

class LoginForm(Form):
    email = TextField(u'Your email address', validators=[Email()])
    password = PasswordField(u'Password', validators=[Required()])
    submit = SubmitField(u'Signup')
