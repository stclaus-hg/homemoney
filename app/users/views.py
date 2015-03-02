from app import login_manager, bcrypt, db
from app.users.forms import LoginForm, ProfileForm
from app.users.models import User
from flask import Blueprint, render_template, redirect, url_for, session, g, flash
import config
from flask.ext.login import login_user, login_required, logout_user, current_user

mod = Blueprint('users', __name__, template_folder='templates')  #, url_prefix='/users')


@mod.route('/')
def index():
    return render_template("index.html", title='Welcome')


@mod.route('/login/', methods=[config.Methods.GET, config.Methods.POST])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Welcome to Home Money!')
            return redirect(url_for('users.index'))
        flash('Wrong email or password', "error")
    return render_template("login.html", form=form, title='Sign In')


@mod.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('See you!')
    return redirect(url_for('users.index'))


@mod.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(user=g.user, obj=g.user)
    if form.validate_on_submit():
        g.user.name = form.name.data
        g.user.email = form.email.data
        if form.password.data:
            g.user.password = bcrypt.generate_password_hash(form.password.data)
        db.session.add(g.user)
        db.session.commit()
        flash('Your profile has changed successfully.')
        return redirect(url_for('users.profile'))
    return render_template('profile.html', form=form, title='Me Profile')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@mod.before_request
def before_request():
    g.user = current_user
