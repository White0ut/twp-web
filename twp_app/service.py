import os
import datetime

from twp_app import app

class TwpService():

  def __init__(self):
    self.STUDENTS = 'students'
    self.ASSIGNMENTS = 'assignments'

  def _walklevel(self, some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
      num_sep_this = root.count(os.path.sep)
      depth = num_sep_this - num_sep
      yield root, dirs, files, depth
      if num_sep + level <= num_sep_this:
        del dirs[:]

  def _last_el(self, val):
    val = val.rstrip(os.path.sep)
    v = val.split(os.path.sep)[-1]
    return val.split(os.path.sep)[-1]

  def get_repositories(self):
    repos = {}
    for root, dirs, files in os.walk(app.config['TWP_REPOS']):
      root_el = self._last_el(root)
      if root == app.config['TWP_REPOS']:
        dirs.remove('gitolite-admin.git')
        for d in dirs:
          repos[d] = {}
          repos[d][self.STUDENTS] = []
          repos[d][self.ASSIGNMENTS] = []
      elif root_el in repos:
        for d in dirs:
          if d.endswith('.git'):
            repos[root_el][self.ASSIGNMENTS].append(d[:-4])
          else:
            repos[root_el][self.STUDENTS].append(d)
        del dirs[:]

      # Remove .git directories because we are not interested in their contents
      nd = []
      for directory in dirs:
        if directory.endswith('.git'):
          nd.append(directory)
      for n in nd:
        dirs.remove(n)

    return repos

  def get_bakups(self):
    bakups = {}
    if not os.path.isdir(app.config['TWP_BAKUPS']):
      return bakups

    for root, dirs, files, depth in self._walklevel(app.config['TWP_BAKUPS'], level=3):
      if depth is 0 or depth is 1:
        for d in dirs:
          bakups[d] = {}
      else:
        for f in files:
          bakups[f] = []
    return bakups

  def archive_course(self, course):
    pass

