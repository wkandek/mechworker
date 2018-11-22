#!/usr/bin/env python

#
# fills in a form page
#
import mechanize
import csv
import time
import sys
import threading
import urllib2


def worker():
  """thread worker function"""
  rc = {}

  # prepares the form, ignore robots.txt and use a browser that is known
  br = mechanize.Browser()
  br.set_handle_robots(False)
  br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

  # loop over file

  with open(mname, 'rb') as csvfile:
    freader = csv.reader(csvfile, delimiter=',', quotechar='|')
    mine = 100
    maxe = 0
    total = 0
    count = 0
    for row in freader:
      start = time.time()
      try:
        br.open(formsurl)
        response = br.response()
        br.select_form(predicate=select_form)
        br.form['FirstName'] = row[0] 
        br.form['LastName'] = row[1] 
        br.form['Email'] = row[2] 
        try:
          br.submit()
        except: 
          pass
      except urllib2.HTTPError, e:
        response = e
      end = time.time()
      elapsed = end-start
      total += elapsed
      mine = min( mine, elapsed )
      maxe = max( maxe, elapsed )
      count += 1
      if response.code in rc:
        rc[response.code] += 1
      else:
        rc[response.code] = 1
      print row[2], response.code, elapsed 
      # time.sleep(1)
    print total/count, mine, maxe
    for i in rc:
      print i, rc[i]
  return

def select_form(form):
  return form.attrs.get('action', None) == '/cgi-bin/ignore.cgi'

# the LP to fill in
formsurl = 'http://example.com/mw.html'


if len(sys.argv) > 2:
  conc = int(sys.argv[1])
  mname = sys.argv[2]
  if len(sys.argv) == 4:
    formsurl = sys.argv[3]
  print formsurl
  print time.strftime("%Y-%m-%d %H:%M")

  threads = []
  for i in range(conc):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

  print time.strftime("%Y-%m-%d %H:%M")
else:
  print "threads mailfilename optional: url"



