# Nonogram crossover

### Team members:
Omri Ben Akoune - 205858822 </br>
Gal Levy - 206055527</br>

--------
## Overview:
The project solves the nonogram problem using Evolutionary Algorithm. 

#### Game rules:
A nonogram is a type of puzzle that consists of a grid of squares that need to be filled in with black or white colors. </br>
The goal is to use the clues provided to determine which squares should be filled in and which should be left blank so that a hidden image is revealed.  </br>
The clues are provided in the form of numbers that are located on the top of the columns and the left side of the rows. </br> 
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
A good solution is binary metrics which fill all the nonogram constraints. Some nonograms have more than one solution.
_____
## Implementation Details
#### Reading Input
After reading the nonogram from the nonograms_clues JSON (Each object is defined with two properties row_clues and col_clues). </br>
We call to the main function that tries to solve the nonogram using Evolutionary Algorithm.</br>
And at the end of the run, we will get a picture of the solved nonogram. </br>

#### Fitness
For evaluating if the solution is a good solution, we need to check that the matrix we have fulfilled the nonogram clues we got as an input.</br>
In the way we create individual, we assure it will follow all the row constraints, </br> 
Therefore, when evaluating how good an individual is, we need to check if it fulfills the nonogram column clues. 
Our fitness function sums the number of "hits" in every column.

For example, consider the following nonogram:

<img src="examples/Screen Shot 2022-12-24 at 9.51.15.png" alt="Example of nonogram for fitness" style="width: 250px; height:200px;"> </br>
The number of possible hits we have in this nonogram is 26, because there are 26 clauses in all the columns together.

#### Population and Crossover
We try to solve a max problem because our target is to get the fitness value to its maximum value by using `Better_Is_Higer= true` </br>
Our population contains 200 individuals as described in the Sample Space section. </br>

For two individuals we create new two individuals by the NonogramCrossover. </br>
We choose a random crossover point between 1 to N, where N is the size of the column in the nonogram. </br>
We will take from the first parent from column 0 til the crossover point and the rest from the other parent. </br>
And the second child will be the rest of parent 1 and parent 2.
For example, Consider the following Nonogram:</br>

<img src="examples/blank_crossover_example.png" alt="Example of blank crossover" style="width: 200px; height:200px;"> </br>

And for the following two possible parents and crossover in index 3 we will get:</br>

<img src="examples/parents_crossover.png" alt="Example of crossover offspring" style="width: 300px; height:300px;"> 

### Running Nonogram Solver
Our main class is responsible for running the solver.  
For each nonogram that is in the nonograms JSON,  
we will run 5 experiments with the same configuration except for the random seed. </br>

Experiment Configuration:
* N = Best fitness possible 
* POP_SIZE = `N^2`
* MAX_GEN = 200

Moreover, each experiment is saved in our statics, and in the end of the run,  
we show graphs of average fitness and best fitness for each experiment and the shows best Nonogram solution.


# Statistics

In order to test and evaluate our algorithm, we checked the results over 3 nonograms in different sizes:</br>
`5X5` `10X10` `15X15`

To summarize, we saw a direct connection between the nonogram's size and the population size, </br>
meaning as the nonogram's size increased, we needed a bigger population to solve the problem. </br>
In contrast, the number of generations had a smaller effect on how fast we reached the solution. </br>
In most the cases, at some generation, the individuals turned up to be very similar and "got stuck", meaning </br>
their fitness didn't improve. We tried to find a way to choose the best population size - </br>
not too big, but also a size that will give us a solution with the maximal fitness value.
After a few tests, we found that the perfect population size is approximately
the squared value of the number of clues. </br> 
For example, for a nonogram with 20 clues, the approximate size of the population should be ~ 20^2 = 400.   


### Small size nonogram (5X5) results:
In this case, the maximum fitness value is 6.</br>
We ran 30 different experiments, to see how often we reach the perfect fitness. </br> 
The average of the best fitness value over 30 experiments is 5.6. </br> </br>
<img src="statistics/small-size/best_fitness.png" style="width: 400px; height:2--px;"> </br>

We tested how fast we reach the solution over different sizes of population: </br>
Population size = 10: </br></br>
<img src="statistics/small-size/POPULATION SIZE = 10.png" style="width: 400px; height:2--px;"> </br>
</br>

Population size = 40 (ensured we will get the best possible fitness value): </br></br>
<img src="statistics/small-size/POPULATION SIZE = 40.png" style="width: 400px; height:2--px;"> </br>
</br>

Considering this problem is pretty small, there was no need of more than 2-3 generations. 
</br>The final solution: </br></br>
<img src="statistics/small-size/sol.png" alt="image description" style="width: 200px; height:2--px;"> </br>

### Mid size nonogram (10X10) results:
In this case, the maximum fitness value is 26.</br>
We ran 30 different experiments, to see how often we reached the perfect fitness. </br> 
The average of the best fitness value over 30 experiments is 22.8. </br> </br>
<img src="statistics/mid-size/best_fitness.png" style="width: 400px; height:2--px;"> </br>

We tested how fast we reached the solution over different sizes of population: </br>
Population size = 200: </br></br>
<img src="statistics/mid-size/POPULATION SIZE = 200.png" style="width: 400px; height:2--px;"> </br>
</br>

Population size = 1000: </br></br>
<img src="statistics/mid-size/POPULATION SIZE = 1000.png" style="width: 400px; height:2--px;"> </br>
</br>

It's easy to see that in both cases the solution is reached in around 25-30 generations, </br>
but the fitness in the second case is much higher. </br>
The final solution: </br></br>
<img src="statistics/mid-size/sol.png" alt="image description" style="width: 200px; height:2--px;"> </br>

### Large size nonogram (15X15) results:
We ran 30 different experiments, to see how often we reached the perfect fitness. </br> 
The average of the best fitness value over 30 experiments is 56.8. </br> </br>
<img src="statistics/big-size/best_fitness.png" style="width: 400px; height:2--px;"> </br>

We tested how fast we reached the solution over different sizes of population: </br>

Population size = 1000: </br></br>
<img src="statistics/big-size/POPULATION SIZE = 1000.png" style="width: 400px; height:2--px;"> </br>
</br>

Population size = 3500: </br></br>
<img src="statistics/big-size/POPULATION SIZE = 3500.png" style="width: 400px; height:2--px;"> </br>
</br>

The final solution: </br></br>
<img src="statistics/big-size/sol.png" alt="image description" style="width: 200px; height:2--px;"> </br>

