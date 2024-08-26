import os
from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from forms import Register, Login
from blueprint import user_blueprint

@user_blueprint.route('/profile')
@login_required
def profile():
    return render_template('users/profile.html')