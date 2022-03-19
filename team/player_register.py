def register_players():
  players = []

  for i in range(10):
    nick = input(f"{i+1}º Nick: ")
    players.append(nick)
    
  print("-="*20)
  print(f"PLAYERS ADICIONADOS: \n{players} ")

  return players
  