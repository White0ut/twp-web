class TwpService():

  def __init__(self):
    pass

  def get_repositories(self):
    return {
      '2250': [
        'kendrick.d.cline',
        'david.t.montgomery',
        'adam.l.banks'
      ],
      '2230': [
        'test.a.test',
        'test.b.test',
        'test.c.test',
        'test.d.test'
      ]
    }

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