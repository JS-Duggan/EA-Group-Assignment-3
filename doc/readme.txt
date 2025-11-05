# How to run

## Exercise 1
Run
```bash
python3 final/code/exercise-1/task1.py
```
The data_ex1 folder contains all the raw data for IOHanalyzer


## Exercise 2
To run the GSEMO algorithm, run
```bash
python3 final/code/exercise-2/run_gsemo.py --budget 10_000
```
To plot the trade-offs of the first run for the GSEMO algorithm, ensure the title on line 22 specifies a budget of 10,000 then run
```bash
python3 final/code/exercise-2/plot_tradeoffs.py
```


## Exercise 3
To run the signal objective instance method, use:
```bash
python3 final/code/exercise-3/run_single_instance.py 
```

To run the multi objective instance method, use:
```bash
python3 final/code/exercise-3/run_multi_instance.py 
```


## Exercise 4
To run the algorithms from Exercise 1, change the budget on line 187 in final/code/exercise-2/task1.py from 10,000 to 100,000 then run
```bash
python3 final/code/exercise-1/task1.py
```

To run the GSEMO algorithm from Exercise 2, run
```bash
python3 final/code/exercise-2/run_gsemo.py --budget 100_000
```
To plot the trade-offs of the first run for the GSEMO algorithm, change the title on line 22 to specify a budget of 100,000 then run
```bash
python3 final/code/exercise-2/plot_tradeoffs.py
```

To run the signal objective instance method from Exercise 3, change the budget on line 163 in final/code/exercise-3/single_multiple_objective_ea.py from 10,000 to 100,000 then run
```bash
python3 final/code/exercise-3/run_single_instance.py 
```

To run the multi objective instance method from Exercise 3, change the budget on line 193 in final/code/exercise-3/single_multiple_objective_ea.py from 10,000 to 100,000 then run
```bash
python3 final/code/exercise-3/run_multi_instance.py 
```
