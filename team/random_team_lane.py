from random import choice


def select_team_lane(players):
  lanes = ('TOP', 'JG', 'MID', 'ADC', 'SUP')
  timeA = {}
  timeB = {}
  i, j = 0, 0

  while len(timeA) != 5:
    player = choice(players)
    if player not in timeA.values():
      timeA[lanes[i]] = player
      i += 1

  while len(timeB) != 5:
    player = choice(players)
    if player not in timeB.values() and player not in timeA.values():
      timeB[lanes[j]] = player
      j += 1

  return timeA, timeB



def print_team_lanes(timeA, timeB):
    print("-="*20)
    print("-=-=-=-=TIME A-=-=-=-=")
    for item in timeA.items():
      print(f"{item[1]} - {item[0]}")

    print("")

    print("-=-=-=-=TIME B-=-=-=-=")
    for item in timeB.items():
      print(f"{item[1]} - {item[0]}")
