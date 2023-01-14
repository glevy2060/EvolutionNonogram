# Nonogram crossover

### Team members:
Omri Ben Akoune - 205858822 </br>
Gal Levy - 206055527</br>

--------
## Overview:
The project solves the nonogram problem using Evolutionary Algorithm. 

#### Game rules:
A nonogram is a type of puzzle that consists of a grid of squares that need to be filled in with black or white colors. </br>
The goal is to use the clues provided to determine which squares should be filled in and which should be left blank, so that a hidden image is revealed.  </br>
The clues are provided in the form of numbers that are located on the top of the columns and on the left side of the rows. </br> 
These numbers indicate how many consecutive squares in that row or column should be filled in. </br>
For example, if the top of a column has the number "3," that means that there are three consecutive squares in that column that need to be filled in. </br>
Solving a nonogram requires logical thinking and a methodical approach to determine the correct placement of the colored squares.

#### Problem definition:
We would like to find a solution to a given nonogram, using the clues given to us.

#### Sample space:
All the possible binary metrics which gives a valid solution to the row clues. </br>
For example, for a certain row, which it's clues are [2,3] for a row in size of 8 these are the possible options:

<img src="examples/2_3_Example.png" alt="Example of [2,3]" style="width: 400px; height:200px;"> </br>
We choose one row representation randomly, and do it for every row.

#### A good solution definition:
A good solution is a binary metrics which fills all the nonogram constrains. Some nonograms have more than one solution.

_____
## Implementation Details
#### Reading Input
After reading the nonogram from the nonograms_clues JSON (Each object defined with two properties row_clues and col_clues). </br>
We call to the main function that try to solve the nonogram using Evolutionary Algorithm.</br>
And in the end of the run we will get a picture of the solved nonogram. </br>

#### Fitness
For evaluating if solution is a good solution, we need to check that the metrix we have fulfilled the nonogram clues we got as an input.</br>
In the way we create individual we assure it will follow all the row constraints, </br> 
Therefor, when evaluating how good individual is, we need to check if it fulfills the nonogram column clues. 
Our fitness function sums the number of "hits" in every column.

For example, consider the following nonogram:

<img src="examples/Screen Shot 2022-12-24 at 9.51.15.png" alt="Example of nonogram for fitness" style="width: 250px; height:200px;"> </br>
The number of hits we have in this nonogram is 26, because there are 26 clauses in all the columns together.

#### Population and Crossover
We try to solve a max problem, because our target is to get the fitness value to it maximum value by using `Better_Is_Higer= true` </br>
Our population contains 200 individuals as described in the Sample Space section. </br>

For two individuals we create new individual by the NonogramCrossover. </br>
We choose a random crossover point between 1 to N , where N is the size of the column in the nonogram. </br>
We will take from the first parent from column 0 til the crossover point and the rest from the other parent. </br>
And te second child will be the rest of parent 1 and parent 2.
For example,Consider the following Nonogram:</br>

<img src="examples/blank_crossover_example.png" alt="Example of blank crossover" style="width: 200px; height:200px;"> </br>

And for the following two possible parents and crossover in index 3 we will get:</br>

<img src="examples/parents_crossover.png" alt="Example of crossover offspring" style="width: 300px; height:300px;"> 

### Running Nonogram Solver
Our main class is responsible for running the solver.  
For each nonogram that is in the nonograms json,  
we will run 5 experiments with the same configuration expect of the random seed. </br>

Experiment Configuration:
* N = size of the Nonogram
* POP_SIZE = N * 10 
* MAX_GEN = 200  

Moreover, each experiment is saved in our statics and in the end of the run,  
we show graphs of average fitness and best fitness for each experiment and the shows best Nonogram solution.