import Room
import Thing
import BuildItems
import CLI
import os

def main():
  os.system('clear')
# Build room information and connections from data file
  roomList = BuildItems.BuildRooms('roomlist.dat')
# Build a player
  mainPlayer = CLI.NewChar(roomList[0])
# Game Intro
  CLI.PrintHelp()
  CLI.GameIntro()

#Detail starting room.
  mainPlayer.DetailRoom()

#Play Loop
  while True:
    CLI.CLI(mainPlayer,roomList)

if __name__ == "__main__":
  main()

