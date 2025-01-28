from flask import render_template, flash, redirect, url_for, request  # type: ignore
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user  # type: ignore
from app.models import User  # type: ignore
from urllib.parse import urlparse  # type: ignore


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        },
        {
            'author': {'username': 'James'},
            'body': 'Learning to create flask applications!'
        },
        {
            'author': {'username': 'Tricia'},
            'body': 'Tight deadlines ahead bro!'
        },
        {
            'author': {'username': 'Peter'},
            'body': 'Steph and Lebron are goat !'
        },
        {
            'author': {'username': 'Liz'},
            'body': 'Ronaldo and Messi are goat!'
        },
        {
            'author': {'username': 'Haaland'},
            'body': 'I need some oil for my baby!'
        },
        {
            'author': {'username': 'Anne'},
            'body': 'give me some words to use today!'
        },
        {
            'author': {'username': 'Paul'},
            'body': 'Great game yesterday!'
        },
        {
            'author': {'username': 'Grace'},
            'body': 'Assure me!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # handle the situation where an already logged in user navigates to the login url
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    # check if the form was submitted (POST request) and fields passed validation
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        # retrieve the page user tried to access before being prompted to sign in
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()

    # check if the form was submitted (POST request) and fields passed validation
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
