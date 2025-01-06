Tic Tac Toe

Tic Tac Toe is a two player game which starts with an initial state of an empty 3x3 grid board.
One player select "X", the other player selects "O", and, the players take turns 
marking the empty cells. The win condition of the game is to be the first player to
form a straight line with their markers.

To begin, we enumerate the board as a 9-tuple (nonuple) such that an empty cell is 0,
a cell marked with "X" as 1 and a cell marked with "O" as 2. Next, let us look at an 
example of a win condition to understand the state of the board.

Suppose we enumerate the board such that the numbers below are the index of a 9-tuple.

<table>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
    <td>5</td>
  </tr>
  <tr>
    <td>6</td>
    <td>7</td>
    <td>8</td>
  </tr>
</table>

Then a possible win condition state

<table>
  <tr>
    <td>X</td>
    <td>O</td>
    <td>&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td>O</td>
    <td>X</td>
    <td>O</td>
  </tr>
  <tr>
    <td>X</td>
    <td>&nbsp;&nbsp;</td>
    <td>X</td>
  </tr>
</table>

Can represent as: state = (1, 2, 0, 2, 1, 2, 1, 0, 1)

Now we can attempt to define our set of all possible states. To understand a bit we first need to look at what our 
states at each epoch will look like. S is the set of all possible states and s is our initial state
possible states. As an example, to reach our next state s<sup>'</sup>, the first player "X" makes a move 
and then the second player makes a move. For example, s<sup>'</sup> can look like:


<table>
  <tr>
    <td>X</td>
    <td>&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;</td>
    <td>O</td>
    <td>&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;</td>
  </tr>
</table>

And the subsequent epoch, s<sup>''</sup> can be 

<table>
  <tr>
    <td>X</td>
    <td>&nbsp;&nbsp;</td>
    <td>X</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;</td>
    <td>O</td>
    <td>&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;</td>
    <td>&nbsp;&nbsp;</td>
    <td>O</td>
  </tr>
</table>

Having established what our states are, we can define our Markov Decision Process as a 
class with all possible states.

Naturally, we would need to find out all possible combinations of outcomes. Since we have 
a 9-tuple board with 3 possible markers 0, 1 and 2, we can have a maximum of 3<sup>9</sup>
unique board configurations. However, we also know that some states are not valid. For
example, for some state s<sup>*</sup>

s<sup>*</sup> = (1, 1, 1, 1, 1, 1, 1, 1, 1) &nbsp;&nbsp;is not in S

This is not possible since we earlier defined our next state as when both players have moved. Therefore, if "X" is 
first, then the numbers of "X"s must be more that or equal to the number of "O"s

We can list the conditions of impossible states as:
1. If "X" is first, then the numbers of "X"s must be more that or equal to the number of "O"s
2. If it is "O" turn, then we cannot have more "O"s than "X"s
3. There cannot be two winners at the same time

Next, we need to define our terminal states from our set of all possible states for our policy and value 
iterations. Our terminal states are wherever there is a win, loss or draw.

After having our set of all states and our set containing our terminal states, we need to 
derive our action set. Our action is when we place and "X" on the board. Therefore, for
any given state, our set of possible actions A, is our decision where we place our "X" marker.

<table>
  <tr>
    <td>X</td>
    <td>a<sub>1</sub></td>
    <td>X</td>
  </tr>
  <tr>
    <td>a<sub>2</sub></td>
    <td>O</td>
    <td>a<sub>3</sub></td>
  </tr>
  <tr>
    <td>a<sub>4</sub></td>
    <td>a<sub>5</sub></td>
    <td>O</td>
  </tr>
</table>


Our next step is determining our transition function. In our case, the next state is determined by
what "O" plays after "X" takes action. As an example, if there are 5 empty cells, then
"X" as 5 possible actions and "O" has 4 possible moves for each action of "X", each with 
equal weight.

Our final key points are our reward function our policies. Here, our reward function for our game is simple. We set 
our winning states to 1, our losing states to -1 and all other states to 0. There is one key point that is of 
note, to reduce the computational expense of the Bellman's equation we include a function that 
generates the possible next states from a given state and action and list the set of all states in our json files.
