# Statistics

In order to test and evaluate our algorithm, we checked the results over 3 nonograms in different sizes:</br>
`5X5` `10X10` `15X15`

To summarize, we saw a direct connection between the nonogram's size and the population size, </br>
meaning as the nonogram's size increased, we needed a bigger population to solve the problem. </br>
In contrast, the number of generations had a smaller effect on how fast we reached the solution. </br>
In most of the cases, at some generation the individuals turned up to be very similar and "got stuck", meaning </br>
their fitness didn't improve. We tried to find a way to choose the best population size - </br>
not to big, but also a size which will give us a solution with the maximal fitness value.
After a few tests, we found that the perfect population size, is approximately
the squared value of the number of clues. </br> 
For example, for a nonogram with 20 clues, the approximate size of population should be ~ 20^2 = 400.   


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

