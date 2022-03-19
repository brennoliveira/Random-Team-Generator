
def edit_players(players):
  qtd = int(input('quantidade de trocas: '))


  for i in range(qtd):
    print("-="*20)
    print(f"ESCOLHA O PLAYER: {i+1}ª TROCA")
    for player in players:
      index = players.index(player)
      print(f"{index + 1} - {player} ")

    old_player = int(input("\nQual posição: "))

    try:
      new_player = str(input('nick para add: '))
      players[old_player - 1] = new_player

    except:
      print("-="*20)
      print("INDEX OUT OF RANGE!")
      print("-="*20)
      break

  print("-="*20)
  print(f"PLAYERS ADICIONADOS: \n {players} ")

  return players



# def edit_players(players):
#   qtd = int(input('quantidade para trocar: '))

# for _ in range(qtd):
#   old_player = str(input('nick para excluir: '))

#   if old_player in players:
#         new_player = input('nick para add: ')
#         for i in range(len(players)):
#           if players[i] == old_player:
#             players[i] = new_player   

#   else:
#     print(f"player {old_player} not found")
#     # print("-="*20)
#     # print(f"PLAYERS ADICIONADOSs: \n {players} ")


# print("-="*20)
# print(f"PLAYERS ADICIONADOS: \n {players} ")

# return players


