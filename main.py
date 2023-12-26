suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[self.rank]

  def __str__(self):
    return f'{self.rank} of {self.suit}'



class Deck:
  def __init__(self):
    self.new_deck = []
    for suit in suits:
      for rank in ranks:
        self.new_deck.append(Card(suit, rank))

  def shuffle_deck(self):
    random.shuffle(self.new_deck)

  def remove_one_card(self):
    return self.new_deck.pop()



class Player:
  def __init__(self, name):
    self.name = name
    self.player_cards = []

  def add_cards(self, card):
    if type(card) == type([]):
      self.player_cards.extend(card)
    else:
      self.player_cards.append(card)

  def remove_cards(self):
    return self.player_cards.pop()

  def __str__(self):
    return f'{self.name} has {len(self.player_cards)} cards'

def game_play():

  player1_name = input('please provide the name of player1')
  player1 = Player(player1_name)
  player2_name = input('please provide the name of player2')
  player2 = Player(player2_name)

  cards_deck = Deck()
  cards_deck.shuffle_deck()


  for i in range(26):
    player1.add_cards(cards_deck.remove_one_card())
    player2.add_cards(cards_deck.remove_one_card())

  game_over = False


  round = 0

  while not game_over:

    round += 1
    print(f'Round {round}')
    # check if players have cards to play
    if len(player1.player_cards) == 0:
      print("player1 doesn't have enough cards to play")
      game_over = True
      break

    elif len(player2.player_cards) == 0:
      print("player2 doesn't have enough cards to play")
      game_over = True
      break

    #check if at war
    at_war = False

    #setup players card collection on table
    player1_cards_on_table = []
    player1_cards_on_table.append(player1.remove_cards())
    player2_cards_on_table = []
    player2_cards_on_table.append(player2.remove_cards())

    # compare players cards and one of the players will win
    if player1_cards_on_table[-1].value > player2_cards_on_table[-1].value:
      player1.add_cards(player1_cards_on_table)
      player1.add_cards(player2_cards_on_table)

    elif player2_cards_on_table[-1].value > player1_cards_on_table[-1].value:
      player2.add_cards(player1_cards_on_table)
      player2.add_cards(player2_cards_on_table)

    else:
      at_war = True

    while at_war:

      if player1_cards_on_table[-1].value > player2_cards_on_table[-1].value:
        player1.add_cards(player1_cards_on_table)
        player1.add_cards(player2_cards_on_table)
        at_war = False

      elif player2_cards_on_table[-1].value > player1_cards_on_table[-1].value:
        player2.add_cards(player1_cards_on_table)
        player2.add_cards(player2_cards_on_table)
        at_war = False

      else:
        print("WAR!!!")

        if len(player1.player_cards) < 5:
          print("player1 doesn't have enough cards to join the war!")
          game_over = True
          break

        elif len(player2.player_cards) < 5:
          print("player2 doesn't have enough cards to join the war!")
          game_over = True
          break

        else:
          for j in range(5):
            player1_cards_on_table.append(player1.remove_cards())
            player2_cards_on_table.append(player2.remove_cards())

game_play()