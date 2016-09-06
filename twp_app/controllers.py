import os
from flask import Blueprint, request, render_template, \
flash, g, session, redirect, url_for, jsonify, send_file, abort
from twp_app import app, service, emails, config_parser
import subprocess

twp_service = service.TwpService()
email_service = emails.EmailService()

@app.route('/')
def index():
  bakups = twp_service.get_bakups()
  repos = twp_service.get_repositories()
  conf = config_parser.ConfigParser().get_conf()
  return render_template('index.html', bakups = bakups, repos = repos, conf = conf)

#
# download
# This endpoint exposes the files in the downloadable/ directory.
#
@app.route('/download', defaults={'filename', ''})
@app.route('/download/<path:filename>')
def download(filename):
  if '..' in filename or filename.startswith('/'):
    abort(404)
  print app.config['BASE_DIR']
  return send_file(os.path.join(app.config['BASE_DIR'], 'downloadable/', filename))

#
# sync_pubs
# This endpoint accepts credentials to the email service to scrape user keys
# sent via email.
#
@app.route('/sync-pubs', methods=['POST'])
def sync_pubs():
  email_service.scrape_email(request.form['username'], request.form['password'])
  return ('', 204)

#
# Update config options
# These routes expose API's to update config entries
#
@app.route('/api/conf/update_status', methods=['POST'])
def update_status():
  course = request.form['course']
  assignment = request.form['assignment']
  status = request.form['status']
  opened = True if status == 'open' else False

  parser = config_parser.ConfigParser()
  parser.update_assignment(course, assignment, opened)
  parser.dump()
  return ('', 204)

@app.route('/api/conf/assignment', methods=['POST'])
def create_assignment():
  course = request.form['course']
  assignment = request.form['assignment']

  parser = config_parser.ConfigParser()
  parser.create_assignment(course, assignment)
  parser.dump()
  return ('', 204)

@app.route('/api/conf/ta', methods=['POST'])
def create_ta():
  ta = request.form['ta']

  parser = config_parser.ConfigParser()
  parser.add_ta(ta)
  parser.dump()
  return ('', 204)

@app.route('/api/conf/prof', methods=['POST'])
def create_prof():
  prof = request.form['prof']

  parser = config_parser.ConfigParser()
  parser.add_prof(prof)
  parser.dump()
  return ('', 204)

#
# Login and logout routes
#
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
