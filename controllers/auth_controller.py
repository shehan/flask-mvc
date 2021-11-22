from flask import current_app
from flask import flash, redirect, render_template, url_for
from flask_login import login_user, current_user, logout_user

from forms.login_form import LoginForm
from models.User import User


def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')


def logout():
    logout_user()
    flash("You Have Been Logged Out!")
    return redirect(url_for('routes.login'))


def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes_auth.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.exists(current_app.session, form.email.data)
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                flash("Login Successful!!")
                return redirect(url_for('routes_auth.dashboard'))
            else:
                flash("Incorrect password.")
        else:
            flash("User does not exist.")
    else:
        flash_errors(form)
    return render_template('login.html', form=form)
