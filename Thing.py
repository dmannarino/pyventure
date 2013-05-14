import Room
import sys
import os

class Thing:
  def __init__(self):
    self.name = 'default thing name'

class Player(Thing):
  def __init__(self):
    self.name = 'default name'
    self.inventory = []
  def __init__(self,name,descrip,currentRoom):
    self.name = name
    self.inventory = []
    self.currentRoom = currentRoom
    self.descrip = descrip
    self.health = 10

  def DetailSelf(self):
    print(self.name + ': ' + self.descrip)
    print('You feel like ', + str(self.health), + ' bucks!')

  def ShowInventory(self):
    print('\n','You rummage through your belongings and find:')
    for item in self.inventory:
      print('  ' + item.name + ' - ' + item.descrip)
    print('\n')

  def DetailRoom(self):
    print('\nYou\'re in ' + self.currentRoom.name + ': ')
    print('   ' + self.currentRoom.descrip)
    print('\nItems in this room: ')
    for item in self.currentRoom.inventory:
      print ('  ' + item.name + ' - ' + item.descrip + '\n')
    debug = False
    if debug:
      print('N: ' + self.currentRoom.n)
      print('W: ' + self.currentRoom.w)
      print('S: ' + self.currentRoom.s)
      print('E: ' + self.currentRoom.e)
      print('U: ' + self.currentRoom.u)
      print('D: ' + self.currentRoom.d)
      print(' ')

  def Go(self,direc,roomList):
    if direc == 'north' and self.currentRoom.n != 'FORBID':
      self.currentRoom = Room.GetRoom(self.currentRoom.n,roomList)
      self.DetailRoom()
      return
    if direc == 'west' and self.currentRoom.w != 'FORBID':
      self.currentRoom = Room.GetRoom(self.currentRoom.w,roomList)
      self.DetailRoom()
      return
    if direc == 'east' and self.currentRoom.e != 'FORBID':
      self.currentRoom = Room.GetRoom(self.currentRoom.e,roomList)
      self.DetailRoom()
      return
    if direc == 'south' and self.currentRoom.s != 'FORBID':
      self.currentRoom = Room.GetRoom(self.currentRoom.s,roomList)
      self.DetailRoom()
      return
    if direc == 'up' and self.currentRoom.u != 'FORBID':
      self.currentRoom = Room.GetRoom(self.currentRoom.u,roomList)
      self.DetailRoom()
      return
    if direc == 'down' and self.currentRoom.d != 'FORBID':
      self.currentRoom = Room.GetRoom(self.currentRoom.d,roomList)
      self.DetailRoom()
      return
    else:
      print('The way is shut.\n')

  def GetItem(self,itemName):
    i = 0  
    if len(self.inventory) >= 2:
      print('Your pockets are full.')
      return
    for item in self.currentRoom.inventory:
      if itemName == item.name:
        self.inventory.append(self.currentRoom.inventory.pop(i))
        print('You took the ' + item.name + '.')
        return
      i = i + 1
    print('There is no ' + itemName + ' here.')

  def DropItem(self,itemName):
    i = 0   
    for item in self.inventory:
      if itemName == item.name:
        self.currentRoom.inventory.append(self.inventory.pop(i))
        print('You dropped the ' + item.name + '.')
        return
      i = i + 1
    print('You look but cant find a ' + itemName + '.')

  def EatItem(self,itemName):
    i = 0   
    for item in self.inventory:
      if itemName == item.name and item.nutr_value > 0:
        self.health += item.nutr_value
        self.inventory.pop(i)
        print('You consumed the ' + itemName + '.')
        print('Yummy? You feel like ' + str(self.health) + ' bucks!')
        return
      elif itemName == item.name and item.nutr_value == 0:
        print('I wouldn\'t eat that. It looks...moist.')
        return
      if itemName == item.name and item.nutr_value < 0:
        self.health += item.nutr_value
        self.inventory.pop(i)
        print('Oh geez...you consumed all of the ' + itemName + '.')
        print('You don\'t feel so well. You vomit for ' + str(-item.nutr_value) + ' minutes!')
        return
      i = i + 1
    print('You can\'t find a ' + itemName + ' in your inventory.')

  def Attrition(self):
    self.health -= 1
    if self.health <= 0:
      self.IsDead()
    elif self.health % 5 == 0:
      if self.health == 15:
        print('You\'re feeling a bit winded.')
      elif self.health == 10:
        print('You are exhausted and hurting.')
      elif self.health == 5:
        print('Jesus, STOP THE PAIN')

  def IsDead(self):
    os.system('clear')
    print('You are DEAD! Dead, dead, dead.')
    print(self.name + ' - ' + self.descrip + ' - Health =' + str(self.health))
    print('Someone rummages through your pockets and finds:')
    for item in self.inventory:
      print('  ' + item.name + ' - ' + item.descrip)
    sys.exit(0)

######################
# Item Class
######################
class Item(Thing):
  def __init__(self):
    self.name = 'default item'
  def __init__(self,name,descrip,nutr_value):
    self.name = name
    self.descrip = descrip
    self.nutr_value = nutr_value

def PrintItems(someItems):
  for item in someItems:
    if item is not []:
      print(item.name)
