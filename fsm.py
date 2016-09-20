#!usr/bin/python
#
# fsm.py
#
# Created by John Van Note
# Created on 8/10/12
#
# Finite State Machine data structure attempt
#
#

def FSM:

  def __init__( self ):
    return

  # @param alphabet is a list of all symbols in fsm
  def __init__( self, alphabet ):
    self.alpha = alphabet
    return

  # @param states is the list of states
  def __init__( self, alphabet, states ):
    self.alpha = alphabet
    self.states = states
    return

  # @param start is an integer detailing the start state, defaults to 0
  def __init__( self, alphabet, states, transFunc ):
    self.alpha = alphabet
    self.states = states 
    self.tf = transFuction
    return


def State:
  self.st = False
  self.acc = False  

  def __init__( self ):
    return

  def __init__( self, index ):
    self.index = index
    return

  def __init__( self, index, start ):
    self.index = index
    self.st = start
    return

  def __init__( self, index, start, accepting ):
    self.index = index
    self.st = start
    self.acc = accepting
    return

def TransitionFunction:
  def
