from flask.ext.wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email, InputRequired
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, IntegerField, BooleanField

class SignupForm(Form):
    firstname = StringField(u'First Name')
    lastname = StringField(u'Last Name')
    password = PasswordField(u'Password')
    email = StringField(u'Your email address')
    age = StringField(u'Age')
    gender = RadioField(u'Gender', choices=[('Male', 'male'), ('Female', 'female')])
    zipcode = StringField(u'Zip Code (so we can connect you with nearby users!)')
    community = SelectField(u'Cancer Community', choices=[('survivor', 'Survivor'), ('cosurvivor', 'Co-Survivor'), ('metastatic', 'Metastatic')])
    diagnosis = SelectField(u'Cancer Diagnosis', choices=[('none', 'None'),
                                                          ('DCIS', 'Ductal Carcinoma In Situ'),
                                                          ('IDC', 'Invasive Ductal Carcinoma'),
                                                          ('tubular', 'Tubular Carcinoma of the Breast'),
                                                          ('medullary', 'Medullary Carcinoma of the Breast'),
                                                          ('mucinous', 'Mucinous Carcinoma of the Breast'),
                                                          ('papillary', 'Papillary Carcinoma of the Breast'),
                                                            ('cribriform', 'Cribriform Carcinoma of the Breast'),
                                                            ('ILC', 'Invasive Lobular Carcinoma'),
                                                            ('inflammatory', 'Inflammatory Breast Cancer'),
                                                            ('LCIS', 'Lobular Carcinoma In Situ'),
                                                            ('male', 'Male Breast Cancer'),
                                                            ('paget', "Paget's Disease of the Nipple"),
                                                            ('phyllodes', 'Phyllodes Tumors of the Breast'),
                                                            ('metastatic', 'Recurrent & Metastatic Breast Cancer'),

                                                          ])
    bio = StringField(u'Short Bio')

    submit = SubmitField(u'Signup')

class LoginForm(Form):
    email = StringField(u'Your email address', validators=[Email()])
    password = PasswordField(u'Password', validators=[InputRequired()])
    submit = SubmitField(u'Signup')
