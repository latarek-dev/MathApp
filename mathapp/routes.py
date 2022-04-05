from typing import Optional

from mathapp import app
from flask import render_template, redirect, url_for, flash, request
from mathapp.models import User, Exercise
from mathapp.forms import RegisterForm, LoginForm, A, B, C, D, Exercise_from_db
from mathapp import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/study', methods=['GET', 'POST'])
@login_required
def study_page():
    exercises = Exercise_from_db.exercises
    exercise1 = exercises[0]
    exercise2 = exercises[1]
    exercise3 = exercises[2]
    exercise4 = exercises[3]
    form1 = A()
    form2 = B()
    form3 = C()
    form4 = D()
    if form1.validate_on_submit():
        if form1.b1.data == exercise1.correct_answer:
            flash(f"Dobrze! {form1.b1.data} to jest prawidłowa odpowiedź!", category="success")
            current_user.add_points(exercise1)
        else:
            flash(f"Niestety {form1.b1.data} to nieprawidłowa odpowiedź. Spróbuj jeszcze raz.", category="danger")

    if form2.validate_on_submit():
        if form2.b2.data == exercise2.correct_answer:
            flash(f"Dobrze! {form2.b2.data} to jest prawidłowa odpowiedź!", category="success")
            current_user.add_points(exercise2)
        else:
            flash(f"Niestety {form2.b2.data} to nieprawidłowa odpowiedź. Spróbuj jeszcze raz.", category="danger")

    if form3.validate_on_submit():
        if form3.b3.data == exercise3.correct_answer:
            flash(f"Dobrze! {form3.b3.data} to jest prawidłowa odpowiedź!", category="success")
            current_user.add_points(exercise3)
        else:
            flash(f"Niestety {form3.b3.data} to nieprawidłowa odpowiedź. Spróbuj jeszcze raz.", category="danger")

    if form4.validate_on_submit():
        if form4.b4.data == exercise4.correct_answer:
            flash(f"Dobrze! {form4.b4.data} to jest prawidłowa odpowiedź!", category="success")
            current_user.add_points(exercise4)
        else:
            flash(f"Niestety {form4.b4.data} to nieprawidłowa odpowiedź. Spróbuj jeszcze raz.", category="danger")

    return render_template('study.html', form1=form1, form2=form2, form3=form3, form4=form4, exercise1=exercise1, exercise2=exercise2, exercise3=exercise3, exercise4=exercise4)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('study_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are now logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('study_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('home_page'))
