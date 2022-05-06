from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from company.models import Details


class RegisterForm(FlaskForm):

    def validate_email_address(self, email_address_to_check):
        email_id = Details.query.filter_by(email_id=email_address_to_check.data).first()
        if email_id:
            raise ValidationError('Email Address already exists! Please try a different email address')


    emp_id = IntegerField(label='employee id', validators=[DataRequired()])
    password: PasswordField = PasswordField(label='Password', validators=[DataRequired(),Length(min=6)])
    confirm_password: PasswordField = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    name = StringField(label='Employee Name', validators=[DataRequired(),Length(min=3, max=30)])
    email_address = StringField(label='Email', validators=[DataRequired(),Email()])
    address = StringField(label='Address', validators=[DataRequired(),Length(min=10, max=50)])
    location = StringField(label='Location', validators=[DataRequired(),Length(min=5, max=20)])
    ph_no = IntegerField(label='Phone Number', validators=[DataRequired()])
    designation = StringField(label='Designation', validators=[DataRequired(),Length(min=3, max=15)])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    emp_id = IntegerField(label='Employee ID', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=6)])
    designation = StringField(label='Designation', validators=[DataRequired()])
    location = StringField(label='Location', validators=[DataRequired(),Length(min=5, max=20)])
    submit = SubmitField(label='Sign in')