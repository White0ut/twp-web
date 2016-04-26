import os

from twp_app import app

class TwpService():

  def __init__(self):
    self.STUDENTS = 'students'
    self.ASSIGNMENTS = 'assignments'

  def __last_el(self, val):
    val = val.rstrip(os.path.sep)
    v = val.split(os.path.sep)[-1]
    return val.split(os.path.sep)[-1]

  def get_repositories(self):
    repos = {}
    for root, dirs, files in os.walk(app.config['TWP_REPOS']):
      if root == app.config['TWP_REPOS']:
        dirs.remove('gitolite-admin.git')
        for d in dirs:
          repos[d] = {}
          repos[d][self.STUDENTS] = []
          repos[d][self.ASSIGNMENTS] = []
      elif self.__last_el(root) in repos:
        r_el = self.__last_el(root)
        for d in dirs:
          if d.endswith('.git'):
            repos[r_el][self.ASSIGNMENTS].append(d[:-4])
          else:
            repos[r_el][self.STUDENTS].append(d)
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
    return {
      '2015-08-13': {
        'clones': {
          '2230': {
            'a0': [
              'kendrick.d.cline',
              'benjamin.s.smithers'
            ],
            'a1': [
              'jill.t.whoosifer',
              'nancy.m.lilly',
              'bob.j.hogan'
            ],
            'a2': [
              'bob.r.rogers',
              'turd.ferguson'
            ],
            'midterm': [
              'bill.w.johnson'
            ]
          },
          '2240': {
            'a0': [
              'test.a.test',
              'test.b.test'
            ],
            'a1': [
              'test.a.test',
              'test.c.test'
            ],
            'a2': [
              'test.a.test',
              'test.b.test'
            ],
            'a3': [
              'test.a.test',
              'test.b.test'
            ],
            'a4': [
              'test.a.test',
              'test.b.test'
            ],
            'FinalSp15': [
              'test.a.test',
              'test.b.test'
            ]
          }
        },
        'repositories': [
          '2230',
          '2240',
          '5950'
        ],
        'tests': [
          '2230',
          '2240'
        ]
      },
      '2016-08-21': {
        'clones': {
          '2230': {
            'a0': [
              'kendrick.d.cline',
              'benjamin.s.smithers'
            ]
          },
          '2240': {
            'a0': [
              'test.a.test',
              'test.b.test'
            ],
            'a1': [
              'test.a.test',
              'test.c.test'
            ]
          }
        },
        'repositories': [
          '2230',
          '2240',
          '5950'
        ],
        'tests': [
          '2230',
          '2240'
        ]
      }
    }
