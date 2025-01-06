Tic Tac Toe

Tic Tac Toe is a two player game which starts with an empty state 3x3 grid board.
One player select "X" and the other player selects "O", and, the players take turns 
marking the empty cells. The win condition of the game is to be the first player to
form a straight line with their markers.

To begin, we enumerate the board as a 9-tuple (nonuple) such that an empty cell is 0,
a cell marked with "X" as 1 and a cell marked with "O" as 2. Next, let us look at an 
example of a win condition to understand the state of the board.

Suppose we enumerate the board such that the numbers below are the index of a 9-tuple.
0  1  2
3  4  5
6  7  8
Then a possible win condition state
X  O  .
O  X  O
X  .  X
Can represent as: state = (1, 2, 0, 2, 1, 2, 1, 0, 1)

Now we can attempt to define our set of all possible state. To understand a bit we first
need to look at what our state will looks like. S<sub>0</sub> is our initial state.
To reach our next state S<sub>1</sub>, the first player "X" makes a move and then the 
second player makes a move. For example, S<sub>1</sub> can look like:
X  .  .  or   X  .  .
.  O  .       .  .  .
.  .  .       .  O  .
Therefore, we can define our Markov Decision Process as a class with all possible states.

Naturally, we would need to find out all possible combinations of outcomes. Since we have 
a 9-tuple board with 3 possible markers 0, 1 and 2, we can have a maximum of 3<sup>9</sup>
unique board configurations. However, we also know that some states are not valid. For
example, the state (1, 1, 1, 1, 1, 1, 1, 1, 1) is not possible since we earlier defined 
our next state as when both players have moved. Therefore, if "X" is first, then the
numbers of "X"s must be more that or equal to the number of "O"s

The list of impossible states are:
1. If "X" is first, then the numbers of "X"s must be more that or equal to the number of "O"s
2. If it is "O" turn, then we cannot have more "O"s than "X"s
3. There cannot be two winners at the same time

Next, we need to define our terminal states from our set of all possible states. This is 
used in the policy and value iterations. Our terminal states are where there is a win,
loss or draw.

After having our set of all states and our set containing our terminal states, we need to 
derive our action set. Our action is when we place and "X" on the board. Therefore, for
any given state, our set of possible actions is our decision where we place our "X" marker.

Our next step is determining our transition function. Since the next state is determined by
what "O" plays after "X" takes action. As an example, if there are 6 empty cells, then
"X" as 6 possible actions and "O" has 5 possible moves for each action of "X", each with 
equal weight.

Next, our reward function for our game is simple. We set our winning states to 1, our 
losing states to -1 and all other states to 0

And finally for our game, to reduce the computational expense of the Bellman's equation 
we include a function that generates the possible next states from a given state and 
action and list the set of all states in our json files.
