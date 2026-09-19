# README

Forgive my Haiku

we will be dicussing now

the minmax system

### minmax:

so the minmax algorythm, what is it.

Basically, it assumes both players are perfect, you take a state(s) and then play it

the player 1(system) wants to play the best possible move for himself(maximiser)
the player 2(adversarial) wants to play the worst possible move for player 1(minimiser)

the system anylyses all possible moves, and gives a score to each branch(how will be given later), the branch with the best score is played.

A branch goes like this:
Player 1 anylizes that

Player 2 anylizes that

Player 1 anylizes that

the score is highest through analysis

and picks best move

and picks worst move

and picks best move

okay, you may not get it but the point is during analysis(player 1 is analysing for both sides) player 1 anylises best and 2 worst.

### scoring

scoring is simple, you tell if the move is a win loss or draw and return it, if the maximiser sees a win they return, if minizer sees a loss they return, if they dont see one of their side they will take a draw.