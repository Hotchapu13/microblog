from flask import render_template, flash, redirect  # type: ignore
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
