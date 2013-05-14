# This file contains the command handling.
import sys
import Thing
import os

#CLI handles the user input from the terminal.
def CLI(mainPlayer,roomList):
  playerInput = input('Command: ')
  parsedCommands = playerInput.split()
  if len(parsedCommands) > 0:
    if parsedCommands[0] == 'detail':
      os.system('clear')
      mainPlayer.DetailRoom()
#       print '\n', mainPlayer.currentRoom.descrip 
    elif parsedCommands[0] == 'inventory':
      mainPlayer.ShowInventory()
    elif parsedCommands[0] == 'go' and len(parsedCommands) == 2:
      os.system('clear')
      mainPlayer.Go(parsedCommands[1],roomList)
      mainPlayer.Attrition()
#      mainPlayer.DetailRoom()
    elif parsedCommands[0] == 'get' and len(parsedCommands) == 2:
      mainPlayer.GetItem(parsedCommands[1])
      mainPlayer.Attrition()
    elif parsedCommands[0] == 'drop' and len(parsedCommands) == 2:
      mainPlayer.DropItem(parsedCommands[1])
    elif parsedCommands[0] == 'eat' and len(parsedCommands) == 2:
      mainPlayer.EatItem(parsedCommands[1])
    elif parsedCommands[0] == 'stat': 
      mainPlayer.DetailSelf()
    elif parsedCommands[0] == 'quit':
      sys.exit(0)
    elif parsedCommands[0] == 'help':
      PrintHelp()
    else:
      allcommand = ''
      for word in parsedCommands:
        allcommand += ' ' + word
      os.system('clear')
      print('You try to' + allcommand + ', but get confused and freudian.')
      mainPlayer.DetailRoom()
      mainPlayer.Attrition()

def NewChar(startRoom):
  os.system('clear')
  name = input('What is your name? ')
  descrip = input('Describe thyself: ')
  return Thing.Player(name,descrip,startRoom)

def GameIntro():
  print('\nYou are standing in your living room, with no recollection as to how you\'ve arrived at your current destination. However, you find your surroundings familiar; this is Kyle and Emily\'s house. You feel very weak. Silence surrounds you -- there are no voices in the streets, or noises from the attached townhouses in the complex. You have nothing in your pockets or on your person, and you are getting hungry. Cold kisses your exposed skin and you know you must move. Take what you can and leave.')

def PrintHelp():
  os.system('clear')  
  print('Commands: \n  detail\n  stat\n  go north (west,south,east,up,down)\n  get item\n  drop item\n  eat item\n  help\n  quit' )



