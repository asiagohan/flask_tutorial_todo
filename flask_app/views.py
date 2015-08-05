from flask import render_template, flash, redirect, url_for, request

from flask_app import app
from .forms import TodoForm

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = TodoForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        detail = form.detail.data
        flash('title:{title}, detail:{detail}'.format(title=title, detail=detail))
        return redirect(url_for('register'))

    return render_template('register.html',
                           form=form)


