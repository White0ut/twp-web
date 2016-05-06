# Trenary Workflow Project

This is a program intended for use at Western Michigan University by Dr. Robert Trenary. This webapp works in conjunction with a gitolite server with which students are given accounts to. 
Students pull assignments and push their work. Their work is then be pulled by a test package, tested, and reviewed for a final grade. Grades are submitted in a PDF sheet within the students repository. 

The webapp is here to ease the process of viewing the state of the repositories, creating new assignments, and archiving semesters worth of work to "restart" for another semester.

## How to

To run the server, execute the following.
`python run.py`

This runs the server on port `5000`.
To add a user account edit the `config.py` with a new user entry.


## TODO:
- [x] Simple auth for sensitive data.
- [x] List active repositories.
- [ ] List archived courses.
- [ ] Download a students' work for a course.
- [ ] Archive a course.
- [ ] Begin a course.
- [ ] Display an assignment as graded if a file matching \Graded*.pdf\ exists in the repo.
- [ ] Check the environment to ensure that repositories, bakups, etc. are in their expected directories.
- [ ] OAuth

