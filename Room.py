class Room:
  def __init__(self):
    self.descrip = 'default'
    self.inventory = []
  def __init__(self,ID,n,w,s,e,u,d,name,description):
    self.ID = ID
    self.name = name
    self.descrip = description
    self.n = n
    self.w = w
    self.s = s
    self.e = e
    self.u = u
    self.d = d
    self.inventory = []

def PrintRooms(someRooms):
  for room in someRooms:
    print(room.name)
  print ('\n')

def GetRoom(roomID,roomList):
  for room in roomList:
    if roomID == room.ID:
      return room
  print('\n*Error no room found*\n')
