import fileinput
import email
import mimetypes
import getpass, imaplib
import json
import traceback
import os
import sys
import subprocess
from twp_app import app


# userName = raw_input('Enter your GMail username: ')
# passwd = getpass.getpass('Enter your password for {}: '.format(userName))

class EmailService():

  def __init__(self):
    self.CONFNAME = os.path.join(app.config['TWP_GITOLITE'], 'conf/')

  def scrape_email(self, userName, passwd):
    studentsLine = []
    confname = self.CONFNAME

    if userName == "trenarycs224@gmail.com":
      print "making lists for 2240"
      confname+="2240.conf"
      classNum = "@2240 = "
      #studentsLine.append("@2240 = ")
    
    elif userName == "trenarycs223@gmail.com":
      print "Making lists for 2230"
      confname+="2230.conf"
      classNum = "@2230 = "
      #studentsLine.apppend("@2230 = ")
    
    elif userName == "trenarycs595@gmail.com":
      print "Making list for 5950"
      confname += "5950.conf"
      classNum = "@5950 = "
      #studentsLine.append("@5950 = ")
    
    else:
      print "I don't recall that email, try again?"
      exit()
    
    try:
      imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
      typ, accountDetails = imapSession.login(userName, passwd)
      if typ != 'OK':
        print 'Not able to sign in!'
        raise
    
      #print out all the gmail boxes
      #print json.dumps(imapSession.list(),indent=4)
    
      #Get all emails from the "KEYS" label
      label = "KEYS"#raw_input('Enter label from to select mail from:')
    
      imapSession.select(label.strip())
      typ, data = imapSession.search(None, 'ALL')
      if typ != 'OK':
        print 'Error searching Inbox.'
        raise
    
    
      # Iterating over all emails
      for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print 'Error fetching mail.'
            raise
    
        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
    
        #Check if any attachments at all
        if mail.get_content_maintype() != 'multipart':
          continue
    
        stuName,stuEmail = email.utils.parseaddr(mail['From'])
    
    
        #strip first part of email address
        emailName = stuEmail.split('@')[0]
    
        #if it's not a wmu email go to the next one
        if stuEmail.split('@')[1] != "wmich.edu":
            continue
    
        print "Getting mail from "+stuName
    
        for part in mail.walk():
          if part.get_content_maintype() == 'multipart':
              # print part.as_string()
              continue
          if part.get('Content-Disposition') is None:
              # print part.as_string()
              continue
          fileName = part.get_filename()
    
          if bool(fileName):
    
            fileName, fileExtension = os.path.splitext(fileName)
            print "filename:{} ext{}".format(fileName,fileExtension)
            #make sure no one sent us their private key
            if fileExtension != ".pub":
                continue
    
            #write the file
            print "[{}]: mv {} -> keydir/{}".format(emailName,fileName,emailName+'.pub')
            keydir = os.path.join(app.config['TWP_GITOLITE'], 'keydir/', emailName+'.pub')
            fp = open(keydir, 'wb')
    
    
            #add them to the students list
            studentsLine.append(emailName+' ')
    
            print "{} added to email list".format(emailName)
    
    
            fp.write(part.get_payload(decode=True))
            fp.close()

      self._prep_repo()
      #get uniq
      classConf = open(confname,"w+")

      studentsLine = list(set(studentsLine))
      classConf.write(classNum+" ".join(studentsLine)+"\n")
      classConf.close()

      self._push_repo()

      imapSession.close()
      imapSession.logout()
    except Exception as e:
      raise e

  def _prep_repo(self):
    p = subprocess.Popen(['git', 'fetch', '-a'], cwd=app.config['TWP_GITOLITE'])
    p.wait()
    p = subprocess.Popen(['git', 'rebase', 'origin', 'master'], cwd=app.config['TWP_GITOLITE'])
    p.wait()

  def _push_repo(self):
    subprocess.call([os.path.join(app.config['TWP_GITOLITE'], 'update.sh')], cwd=app.config['TWP_GITOLITE'])
