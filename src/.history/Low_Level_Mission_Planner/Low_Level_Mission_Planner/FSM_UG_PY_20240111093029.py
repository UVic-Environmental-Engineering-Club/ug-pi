from random import randint
import time
import sys

State=type("State",(object,), {})

parameter = None
isManControlMode = False

if (len(sys.argv) == 2):
   parameter = sys.argv[1]
   if (parameter == "Man"):
      print("Manual control mode")
      isManControlMode = True
   elif (parameter == "Auto") :
      print("Auto control mode")
      isManControlMode = False
   else:
      sys.exit("Usage: python3 -m FSM_UG_PY.py <Man|Auto>")

# elif (len(sys.argv) == 2):
#    parameter = sys.argv[1]
#    if (parameter != "Auto"):
#       sys.exit("Usage: python3 -m FSM_UG_PY.py <Man|Auto>")
#    else:
else:
   sys.exit("Usage: python3 -m FSM_UG_PY.py <Man|Auto>") 

## parameter = input("Enter a parameter: ")
## print("Entered parameter:", parameter)
 
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
      # self.LightOn = True

##====================================

if __name__ == "__main__":
   ## print("Run Main\n")

   light = Char()

   light.FSM.states["PowerOn"] = PowerOn()
   light.FSM.states["StandBy"] = StandBy()
   light.FSM.states["Dive"] = Dive()
   light.FSM.states["Surface"] = Surface()
   light.FSM.states["PowerOff"] = PowerOff()
   light.FSM.transitions["toPowerOn"] = Transition("PowerOn")
   light.FSM.transitions["toStandBy"] = Transition("StandBy")
   light.FSM.transitions["toDive"] = Transition("Dive")
   light.FSM.transitions["toSurface"] = Transition("Surface")
   light.FSM.transitions["toPowerOff"] = Transition("PowerOff")

   light.FSM.SetState("PowerOn")

   for i in range(20):
      startTime = time.time()
      # print("Time: " + str(time.time()))
      timeInterval = 1
      while (startTime + timeInterval > time.time()):
         pass
      # print("isManControlMode: " + str(~isManControlMode))
      if (parameter != None and not isManControlMode):
         if (randint(0,1)):
            if (light.FSM.curState == light.FSM.states["PowerOn"]):
               light.FSM.Transition("toStandBy")
            elif (light.FSM.curState == light.FSM.states["StandBy"]):
               if (randint(0,1)):
                  light.FSM.Transition("toDive")
               else:
                  light.FSM.Transition("toSurface")
            elif (light.FSM.curState == light.FSM.states["Dive"]):
               if (randint(0,1)):
                  light.FSM.Transition("toStandBy")
               else:
                  light.FSM.Transition("toSurface")
            elif (light.FSM.curState == light.FSM.states["Surface"]):
               if (randint(0,1)):
                  light.FSM.Transition("toDive")
               else:
                  light.FSM.Transition("toStandBy")
         light.FSM.Execute()
      elif (parameter != None and isManControlMode):
         newStateParameter = None
         print("Current state: " + str(light.FSM.curState.__class__.__name__))
         print("Available states from current state ")
         if (light.FSM.curState == light.FSM.states["PowerOn"]):
            print("StandBy")
         elif (light.FSM.curState == light.FSM.states["StandBy"]):
            print("Dive")
            print("Surface")
            print("PowerOff")
         elif (light.FSM.curState == light.FSM.states["Dive"]):
            print("StandBy")
            print("Surface")
            print("PowerOff")
         elif (light.FSM.curState == light.FSM.states["Surface"]):
            print("Dive")
            print("StandBy")
            print("PowerOff")
         while (newStateParameter not in light.FSM.states):
            newStateParameter = input("Enter a state you want to transition to: ")
            print("Entered state: " +  newStateParameter)
            if (newStateParameter in light.FSM.states):
               light.FSM.Transition("to" + newStateParameter)
               light.FSM.Execute()
            else:
               print("state " + str(newStateParameter) + "does not exist")

