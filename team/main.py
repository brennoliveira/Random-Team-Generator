import random_team, random_team_lane, player_register, edit_players

print("ADICIONE OS PLAYERS")
players = player_register.register_players()

while True:
  print("-="*20)
  print("1 - time aleatório \n2 - time e lane aleatórios \n3 - editar players \n9 - parar")
  option = int(input("opção: "))

  if option == 1:
    timeA, timeB = random_team.select_players(players)

    random_team.print_teams(timeA, timeB)

  if option == 2:
    timeA, timeB = random_team_lane.select_team_lane(players)

    random_team_lane.print_team_lanes(timeA, timeB)

  if option == 3:
    # players = edit_players.edit_players(players)
    players = edit_players.edit_players(players)

  if option == 9:
    break
