from flask import Blueprint, request, render_template, \
flash, g, session, redirect, url_for, jsonify

from twp_app import app, twp_service

@app.route('/')
def index():
  entries = [
    {
      'title': 'CS2240',
      'text': '20 students'
    },
    {
      'title': 'CS2230',
      'text': '35 students'
    }
  ]
  bakups = twp_service.get_bakups()
  repos = twp_service.get_repositories()
  return render_template('index.html', entries = entries, bakups = bakups, repos = repos)

@app.route('/add', methods=['POST'])
def add_entry():
  if not session.get('logged_in'):
    abort(401)
  flash('New entry was successfully posted')
  return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  logged_in = None
  if request.method == 'POST':
    # check username/password
    for username, password in app.config['ACCOUNTS'].iteritems():
      if request.form['username'] == username:
        if request.form['password'] == password:
          logged_in = True
          break
        else:
          logged_in = False
      else:
        logged_in = False

  # ensure we return the correct value
  if logged_in:
      session['logged_in'] = True
      flash('Successfully logged in!')
      return redirect(url_for('index'))
  elif logged_in is False:
    error = 'Invalid credentials'

  return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('You were logged out')
  return redirect(url_for('index'))
