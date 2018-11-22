#!/usr/bin/env python

#
#
import sys

if len(sys.argv) == 4:
  one = int(sys.argv[1])
  two = int(sys.argv[2])
  domain = sys.argv[3]
#  from = min( one, two )
#  to = max( one, two )

  file = open( "mails.csv", "w" )
  for i in range (one,two):
    file.write( 'U' )
    file.write(str(i))
    file.write( ',Userslastname,' )
    file.write( 'U' )
    file.write(str(i))
    file.write( '@' )
    file.write( domain )
    file.write( '\n' )

  file.close
else:
  print '3 args required - from and to , domain'

