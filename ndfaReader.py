#!usr/bin/python
#
# ndfaReader.py
#
# Created by John Van Note
# Created on 8/14/12
#
#
#

import sys

def main( argv=sys.argv ):
  if len( argv ) != 2:
    print "Incorrect number of arguments, exiting"
    return
  file = open( argv[1] )
  instructions = list()
  for line in file.readlines():
    instructions.append(line)
  print instructions
  
  create


if __name__ == "__main__":
  main()
