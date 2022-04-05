from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, FieldList, FormField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, InputRequired

from mathapp import db
from mathapp.models import User, Exercise
from wtforms_alchemy import model_form_factory, ModelForm


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

"""
class B(FlaskForm):
    b1 = StringField("B1 Label")
    b2 = StringField("B2 Label")


class A(FlaskForm):
    a1 = StringField("A1 Label")
    a2 = FieldList(FormField(B), min_entries=3)
    s = SubmitField("Submit Field")


class FirstQuestion(FlaskForm):
    quiz1 = RadioField("Pytanie pierwsze", choices=['Opcja 1', 'Opcja 2'])
    quiz2 = RadioField("Pytanie pierwsze", choices=['Odpowiedź 1', 'Odpowiedź 2'])


class CopyQuestions(FlaskForm):
    reapeatQuestion = FieldList(FormField(FirstQuestion), min_entries=3)
    submit1 = SubmitField("Submit Field")
"""


class Exercise_from_db():
    exercises = Exercise.query.all()


class A(FlaskForm):
    list = []
    for exercise in Exercise_from_db.exercises:
        list.append(exercise.answer_A)
        list.append(exercise.answer_B)
        list.append(exercise.answer_C)
        list.append(exercise.answer_D)
    b1 = RadioField("Pytanie pierwsze", choices=list[0:4])
    s1 = SubmitField("Potwierdź")


class B(FlaskForm):
    list = []
    for exercise in Exercise_from_db.exercises:
        list.append(exercise.answer_A)
        list.append(exercise.answer_B)
        list.append(exercise.answer_C)
        list.append(exercise.answer_D)
    b2 = RadioField("Pytanie drugie", choices=list[4:8])
    s2 = SubmitField("Potwierdź")


class C(FlaskForm):
    list = []
    for exercise in Exercise_from_db.exercises:
        list.append(exercise.answer_A)
        list.append(exercise.answer_B)
        list.append(exercise.answer_C)
        list.append(exercise.answer_D)
    b3 = RadioField("Pytanie drugie", choices=list[8:12])
    s3 = SubmitField("Potwierdź")


class D(FlaskForm):
    list = []
    for exercise in Exercise_from_db.exercises:
        list.append(exercise.answer_A)
        list.append(exercise.answer_B)
        list.append(exercise.answer_C)
        list.append(exercise.answer_D)
    b4 = RadioField("Pytanie drugie", choices=list[12:16])
    s4 = SubmitField("Potwierdź")