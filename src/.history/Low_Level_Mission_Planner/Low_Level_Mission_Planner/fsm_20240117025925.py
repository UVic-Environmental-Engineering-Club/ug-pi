"""
      Written by David Kim. A basic FSM for demonstration purpose.
      TODO:
      Solid FSM with graph data strcuture need to be implemented.
      There should be a better way to configure FSM structure.
      Higher level automatic FSM controller (maybe PID?) need to be implemented.
      Destroy
"""

from random import randint
import time
import sys
import math

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

   def Execute(self):
      print("Transitioning") 

##====================================

class SimpleFSM(object):
   def __init__(self, char):
      self.char = char
      self.states = {}
      self.transitions = {}
      self.availableTrans = None
      self.curState = None
      self.trans = None

   def SetState(self, stateName):
      self.curState = self.states[stateName]

   def Transition(self, transName):
      if (transName in ["toDive", "toSurface"]):
         startTime = time.time()
         timeInterval = 0.5
         i = 0
         while i <= 10:
            while (startTime + timeInterval > time.time()):
               pass
            print("Rotating status: " + "{:10.4f}".format(100 * math.sin(i*math.pi/ (10 * 2))) + "%")
            i += 1
      self.trans = self.transitions[transName]

   def Execute(self):
      if (self.trans):
         self.trans.Execute()
         self.SetState(self.trans.toState)
         self.trans = None
      self.curState.Execute()


##====================================

class CreateFSM(object):
   def __init__(self):
      self.FSM = SimpleFSM(self)


##====================================

class CreateAndRunFSM(object):
   def __init__(self):
      self.newStateParameter = None
      self.Glider = CreateFSM()
   
      # Configure states as an instant
      self.Glider.FSM.states["PowerOn"] = PowerOn()
      self.Glider.FSM.states["StandBy"] = StandBy()
      self.Glider.FSM.states["Dive"] = Dive()
      self.Glider.FSM.states["Surface"] = Surface()
      self.Glider.FSM.states["PowerOff"] = PowerOff()
      
      # Configure availabe transitions
      self.Glider.FSM.states["PowerOn"].availableTrans = ["toStandBy"]
      self.Glider.FSM.states["StandBy"].availableTrans = ["toDive", "toSurface", "toPowerOff"]
      self.Glider.FSM.states["Dive"].availableTrans = ["toStandBy", "toSurface"]
      self.Glider.FSM.states["Surface"].availableTrans = ["toDive", "toStandBy", "toPowerOff"]
      
      # Configure transitions
      self.Glider.FSM.transitions["toPowerOn"] = Transition("PowerOn")
      self.Glider.FSM.transitions["toStandBy"] = Transition("StandBy")
      self.Glider.FSM.transitions["toDive"] = Transition("Dive")
      self.Glider.FSM.transitions["toSurface"] = Transition("Surface")
      self.Glider.FSM.transitions["toPowerOff"] = Transition("PowerOff")

      self.Glider.FSM.SetState("PowerOn")

      

   def ReportAndTransition(self):
      print("Current state: " + str(self.Glider.FSM.curState.__class__.__name__))
      print("Available transition from current state ")

      print (self.Glider.FSM.curState.availableTrans)
      # this is lazy method of showing available transition from the current state. Implement graph for FSM data structure to make it more resilient. - David
      # if (self.Glider.FSM.curState == self.Glider.FSM.states["PowerOn"]):
      #    print("StandBy")
      # elif (self.Glider.FSM.curState == self.Glider.FSM.states["StandBy"]):
      #    print("Dive")
      #    print("Surface")
      #    print("PowerOff")
      #    print (self.Glider.FSM.states["StandBy"].availableTrans )
      # elif (self.Glider.FSM.curState == self.Glider.FSM.states["Dive"]):
      #    print("StandBy")
      #    print("Surface")
      #    print("PowerOff")
      # elif (self.Glider.FSM.curState == self.Glider.FSM.states["Surface"]):
      #    print("Dive")
      #    print("StandBy")
      #    print("PowerOff")
      if (self.Glider.FSM.curState.__class__.__name__ in ["Dive", "Surface"]):
         print("=====Debug=====")
         startTime = time.time()
         timeInterval = 1
         while (startTime + timeInterval > time.time()):
            pass
         if (randint(0,1)):
            if (self.Glider.FSM.curState == Dive):
               self.Glider.FSM.Transition("toSurface")
            elif(self.Glider.FSM.curState == Surface):
               self.Glider.FSM.Transition("toDive")
         self.Glider.FSM.Execute()
      else:
         self.newStateParameter = input("Enter a transition you want to take: ")
         print("Entered state: " +  self.newStateParameter)

         if (self.newStateParameter.strip() in self.Glider.FSM.curState.availableTrans):
            self.Glider.FSM.Transition(self.newStateParameter)
            self.Glider.FSM.Execute()
         else:
            print("====Error: state " + str(self.newStateParameter) + "does not exist====")


