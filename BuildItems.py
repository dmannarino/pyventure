import csv
import Thing
import Room

def BuildItems(filename):
  reader=csv.reader( open(filename), delimiter = '/')
  i = 0
  itemList = []
  for row in reader:
    nextItem = Thing.Item( str(row[0]), str(row[1]), str(12) )
    itemList = itemList + [nextItem]
  return itemList

def BuildRooms(filename):
  reader=csv.reader( open(filename), delimiter = '/')
  i = 0
  roomList = []
  for row in reader:
    if row != []:

      nextRoom = Room.Room( str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      n = len(row)
      while n > 9:
        parsedThing = str(row[n-1]).split(':')
        if parsedThing[0] == 'Item':
          nextRoom.inventory.append(Thing.Item( parsedThing[1], parsedThing[2], int(parsedThing[3])  ))
        n = n - 1
# Debug lines
#      if i == 0:
#        nextRoom.inventory.append( Thing.Player('Kyle',nextRoom) )
#        i = 1
# End Debug
      roomList = roomList + [nextRoom]
  return roomList
