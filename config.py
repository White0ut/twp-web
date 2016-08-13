DEBUG = True

ACCOUNTS = {
	'kendrick': 'cline',
	'scott': 'linder',
	'chris': 'sphinx',
  'robert': 'trenary'
}

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TWP_HOME = os.path.abspath('..')
TWP_BAKUPS = os.path.join(TWP_HOME, 'bak')
TWP_REPOS = os.path.join(TWP_HOME, 'repositories')
TWP_GITOLITE = os.path.join(TWP_HOME, 'gitolite-admin')

THREADS_PER_PAGE = 2

SECRET_KEY = '9A402F81-DDB3-4D40-9027-E2F8E1BC5992'

