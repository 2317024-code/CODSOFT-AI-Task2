# Tic-Tac-Toe with AI

## Project Overview

This project implements a Tic-Tac-Toe game in Python where a human player competes against an AI opponent using the Minimax algorithm with alpha-beta pruning for optimal moves.

Language: Python

Algorithm: Minimax with alpha-beta pruning

## Features:
- Interactive command-line Tic-Tac-Toe game
- Human player (X) vs. AI player (O)
- AI makes optimal moves to either win or force a draw
- Input validation for player moves
- Clear display of the game board

## Prerequisites
- Python 3.9 installed
- No external libraries required (uses only the built-in math module)

# How It Works

## Board Representation:
- The game board is a list of 9 elements, initialized with empty spaces (" ").
- Positions are numbered 1 to 9 (left to right, top to bottom).

## Game Logic:
- Players take turns: human plays as X, AI plays as O.
- The human inputs a move by entering a number (1-9).
- The AI uses the Minimax algorithm with alpha-beta pruning to determine the best move.

## Minimax Algorithm:
- Evaluates all possible moves recursively.
- Scores: +1 for AI win, -1 for human win, 0 for a draw.
- Alpha-beta pruning optimizes the search by eliminating branches that won't affect the final decision.

## Game Flow:
- Displays the board after each move.
- Checks for a win or draw after each turn.
- Ends the game when there’s a winner or the board is full.

## Play the Game:
- Follow the prompt to enter your move (1-9).
- The AI will respond with its move.
- Continue until there’s a winner or a draw.

## Code Structure
- board: A list representing the 3x3 Tic-Tac-Toe grid.
- printboard(board): Displays the current state of the board.
- checkwin(board): Checks for a winner by evaluating rows, columns, and diagonals.
- isfull(board): Checks if the board is full (draw condition).
- minmax(board, dep, alp, bet, ismax): Implements the Minimax algorithm with alpha-beta pruning.
- best_move(board): Determines the AI’s optimal move.
- play_game(): Main game loop handling player input and AI moves.
