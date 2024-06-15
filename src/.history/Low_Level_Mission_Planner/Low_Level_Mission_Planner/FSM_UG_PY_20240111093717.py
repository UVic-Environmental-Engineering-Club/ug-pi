from random import randint
import time
import sys

State=type("State",(object,), {})

parameter = None
isManControlMode = True
# Assuming that it is always manual control for demonstration. In the future automatic / man fsm interaction will be implemented
 
##====================================

class PowerOn(State):
   def Execute(self):
      print("PowerOn")
      
class StandBy(State):
   def Execute(self):
      print("StandBy") 

class Dive(State):
   def Execute(self):
      print("Dive") 

class Surface(State):
   def Execute(self):
      print("Surface") 

class PowerOff(State):
   def Execute(self):
      print("PowerOff") 
      sys.exit()

##====================================

class Transition(object):
   def __init__(self, toState):
      self.toState = toState

   def Execute(Self):
      print("Transitioning") 

##====================================

class SimpleFSM(object):
   def __init__(self, char):
      self.char = char
      self.states = {}
      self.transitions = {}
      self.curState = None
      self.trans = None

   def SetState(self, stateName):
      self.curState = self.states[stateName]

   def Transition(self, transName):
      self.trans = self.transitions[transName]

   def Execute(self):
      if (self.trans):
         self.trans.Execute()
         self.SetState(self.trans.toState)
         self.trans = None
      self.curState.Execute()


##====================================

class Char(object):
   def __init__(self):
      self.FSM = SimpleFSM(self)
      # self.GliderOn = True

##====================================

if __name__ == "__main__":
   ## print("Run Main\n")

   Glider = Char()

   Glider.FSM.states["PowerOn"] = PowerOn()
   Glider.FSM.states["StandBy"] = StandBy()
   Glider.FSM.states["Dive"] = Dive()
   Glider.FSM.states["Surface"] = Surface()
   Glider.FSM.states["PowerOff"] = PowerOff()
   Glider.FSM.transitions["toPowerOn"] = Transition("PowerOn")
   Glider.FSM.transitions["toStandBy"] = Transition("StandBy")
   Glider.FSM.transitions["toDive"] = Transition("Dive")
   Glider.FSM.transitions["toSurface"] = Transition("Surface")
   Glider.FSM.transitions["toPowerOff"] = Transition("PowerOff")

   Glider.FSM.SetState("PowerOn")

   
   newStateParameter = None
   print("Current state: " + str(Glider.FSM.curState.__class__.__name__))
   print("Available states from current state ")
   if (Glider.FSM.curState == Glider.FSM.states["PowerOn"]):
      print("StandBy")
   elif (Glider.FSM.curState == Glider.FSM.states["StandBy"]):
      print("Dive")
      print("Surface")
      print("PowerOff")
   elif (Glider.FSM.curState == Glider.FSM.states["Dive"]):
      print("StandBy")
      print("Surface")
      print("PowerOff")
   elif (Glider.FSM.curState == Glider.FSM.states["Surface"]):
      print("Dive")
      print("StandBy")
      print("PowerOff")
   while (newStateParameter not in Glider.FSM.states):
      newStateParameter = input("Enter a state you want to transition to: ")
      print("Entered state: " +  newStateParameter)
      if (newStateParameter in Glider.FSM.states):
         Glider.FSM.Transition("to" + newStateParameter)
         Glider.FSM.Execute()
      else:
            print("state " + str(newStateParameter) + "does not exist")

