# ds5100_uts4gf_montecarlo


## Metadata
 My name is Olivia Kantor and this project is a Monte Carlo Simulator. 


## Synopsis

To install:
```pip install https://github.com/olkk9000/ds5100_uts4gf_montecarlo.git```

To import:
```from montecarlo import montecarlo```

Create a dice:
```Die = montecarlo.Die(faces=np.array([4,5,6]))```

Play a game:
```
die_list = [Die1, Die2, Die3]
Game1 = montecarlo.Game(die_list)
Game1.play(times=6)
``` 

Analyze a game:
```Analyzer1 = montecarlo.Analyzer(Game1)
df = Analyzer.combo_count()
print(df)```


## API Description
- Die : Creates the die class which simulates the roll of dice given input faces and weights.
    - change_weight: Changes the weight of a face of the die object. Inputs are face (string or numeric) which is the face where the weight value will change and weight (int, float, or str castable as numeric).
    - roll: Simulates die roll specified number of times. Input is times rolled as int. Output is a list.
    - current_state: Returns copy of the private die data frame. No input. Output is a pandas data frame. 
- Game: Game consists of rolling one or more Die objects one or more times.
    - play: Saves the result of dice rolls to a private data frame. Input is times (how many times the dice should be rolled) as an integer.
    - show_results: Returns copy of the private play data frame. Input is width, which is either "wide" or "narrow", and will specifiy the format of the returned data frame.
- Analyzer: The Analyzer object takes the results of a single game and computes descriptive statistical properities.
    - jackpot: Computes how many times the game resulted in a jackpot. Input is a montecarlo Game object. Returns the number of jackpots as an integer.
    - face_counts_per_roll(): Computes how many times a given face is rolled in each event. No input. Output is a data frame.
    - combo_count: Computes the distinct combinations of faces rolled, along with their counts. No input. Output is a data frame with MultiIndex of distinct combinations and counts.
    - perm_count: Computes the distinct permutations of faces rolled, along with their counts. No input. Output is a data frame with MultiIndex of distinct permutations and counts.






