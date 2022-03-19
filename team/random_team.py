from random import choice

def select_players(players):
  timeA = []
  timeB = []

  while len(timeA) != 5:
    player = choice(players)
    if player not in timeA:
      timeA.append(player)

  while len(timeB) != 5:
    player = choice(players)
    if player not in timeB and player not in timeA:
      timeB.append(player)

  return timeA, timeB


def print_teams(timeA, timeB):
    print("-="*20)
    print("-=-=-=-=TIME A-=-=-=-=")
    for player in timeA:
      print(player)

    print("")

    print("-=-=-=-=TIME B-=-=-=-=")
    for player in timeB:
      print(player) 
