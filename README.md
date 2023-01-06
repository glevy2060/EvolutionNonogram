# Nonogram crossover

### Team members:
Omri Ben Akoune - 205858822 </br>
Gal Levy - 206055527</br>

--------
## Overview:
The project solves the nonogram problem using Evolutionary Algorithm. 

#### Game rules:
A nonogram is a type of puzzle that consists of a grid of squares that need to be filled in with black or white colors. The goal is to use the clues provided to determine which squares should be filled in and which should be left blank, so that a hidden image is revealed. The clues are provided in the form of numbers that are located on the top of the columns and on the left side of the rows. These numbers indicate how many consecutive squares in that row or column should be filled in. For example, if the top of a column has the number "3," that means that there are three consecutive squares in that column that need to be filled in. Solving a nonogram requires logical thinking and a methodical approach to determine the correct placement of the colored squares.

#### Problem definition:
We would like to find a solution to a given nonogram, using the clues given to us.

#### Sample space:
All the possible binary metrics which gives a valid solution to the row clues.
for example, for a certain row, which it's clues are [3,2,6] these are the options:


<img src="../../../../../var/folders/4p/c3_9s80j3fsc1_gj0wn52pr80000gr/T/TemporaryItems/NSIRD_screencaptureui_SppDbT/Screen Shot 2023-01-06 at 13.27.24.png" alt="image description" style="width: 400px; height:2--px;"> </br>
we choose one row representation randomly, and do it for every row. 

#### A good solution definition:
A good solution is a binary metrics which fills all the nonogram constrains. Some nonograms have more than one solution.

_____
## Implementation Details

for evaluating if solution is a good solution, we need to check that the metrix we have fulfilled the nonogram clues we got as an input.
In the way we create individual we assure it will follow all the row constraints, 
therefor, when evaluatin how good individual is, we need to check if it fulfilles the nonogram column clues. 
Our fitness function sums the number of "hits" in every column 
