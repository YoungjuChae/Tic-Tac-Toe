# Author: Youngju Chae
# Text based Tic-Tac-Toe game

# Importing necessary module
import random
from art import logo
import os

# Creating necessary variable
clear = lambda: os.system('clear')

# Decide the letter of player and computer
def getLetter():
  player_letter = input('Do you want to be X or O?\n ').upper()
  if player_letter == 'X':
    return ['X','O']
  else:
    return ['O', 'X']

# Randomly determine who goes first
def goesFirst():
  first = random.choice([1,2])
  if first == 1:
    return 'player'
  else:
    return 'computer'

# Get the player's next move
def getPlayerMove(board):
  move = ' '
  # Check if move is a valid input
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not spaceFree(board, int(move)):
    move = input('What is your next move? (1-9)\n ')
  return int(move) 

# Determine the computer's next move 
def getComputerMove(board, letters):
  # Check if computer can win this turn
  for x in range(1,10):
    copy = copyBoard(board)
    if spaceFree(copy, x):
      makeMove(copy, x, letters[1])
      if isWinner(copy, letters[1]):
        return x
  # Check if opponent (player) can win this turn and if so block 
  for x in range(1,10):
    copy = copyBoard(board)
    if spaceFree(copy, x):
      makeMove(copy, x, letters[0])
      if isWinner(copy, letters[0]):
        return x

  # Pick the best next move (Corners)
  empty_list = []
  for x in [1,3,7,9]:
    if spaceFree(board, x):
      empty_list.append(x)
  if len(empty_list) != 0:
    move = random.choice(empty_list)
    return move
  # Pick the best next move (Middle)
  if spaceFree(board, 5):
    return 5
  # Pick the best next move (The Rest)
  for x in [2,4,6,8]:
    if spaceFree(board, x):
      empty_list.append(x)
  if len(empty_list) != 0:
    move = random.choice(empty_list)
    return move

# Draw Tic-Tac-Toe board in text format
def drawBoard(board):
  print(board[7] + '|' + board[8] + '|' + board[9])
  print('-+-+-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-+-+-')
  print(board[1] + '|' + board[2] + '|' + board[3])

# Determine the winner
def isWinner(board, letter):
  return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[7] == letter and board[4] == letter and board[1] == letter) or (board[8] == letter and board[5] == letter and board[2] == letter) or (board[9] == letter and board[6] == letter and board[3] == letter) or (board[7] == letter and board[5] == letter and board[3] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter)

# Make a move on the board
def makeMove(board, move, letter):
  board[move] = letter

# Determine if board is full or not
def fullBoard(board):
  for x in range(1,10):
    if board[x]  == ' ':
      return False
  return True

# Copy the current board
def copyBoard(board):
  boardCopy = []
  for x in board:
    boardCopy.append(x)
  return boardCopy

# Determine if empty space is available or not
def spaceFree(board, letter):
  return board[letter] == ' '

# Run the game
def playGame():
  print(logo)
  board = [' '] * 10
  playing = True
  print('Welcome to Tic-Tac-Toe!')
  letters = getLetter()
  turn = goesFirst() 
  if turn == 'player':
    print('You will go first.')
  else:
    print('The computer will go first.')
  while playing:
    if turn == 'player':
      drawBoard(board)
      move = getPlayerMove(board)
      makeMove(board, move, letters[0])
      turn = 'computer'
      if isWinner(board, letters[0]):
        drawBoard(board)
        print('You won!')
        playing = False
      elif fullBoard(board):
        drawBoard(board)
        print('You tied!')
        playing = False
    else:
      move = getComputerMove(board, letters)
      makeMove(board, move, letters[1])
      turn = 'player'
      if isWinner(board, letters[1]):
        drawBoard(board)
        print('The computer has beaten you! You lose.')
        playing = False
      elif fullBoard(board):
        drawBoard(board)
        print('You tied!')
        playing = False

# Give the option to play the game again
while input('Do you want to play Tic-Tac-Toe? (y)es or (n)o? ') == 'y':
  clear()
  playGame()
