import numpy as np
import pandas as pd
import random

class Die:
    """
    PURPOSE: Create the die class which simulates the roll of dice given input faces and weights
    """
    def __init__(self, faces, weight = 1):
        """
        PURPOSE: create die object and save dataframe of faces and weights
        
        INPUT:
        faces - NumPy array. Array dtype can be strings or numeric. Array values must be distinct.
        weight - numeric. Default to 1 for each face value. 

        OUTPUT: None 
        """
        self.faces = faces
        self.weight = weight
        self.df = pd.DataFrame(data={'weight':weight}, index=[faces])
        
        if not isinstance(faces, np.ndarray):
            raise TypeError("faces must be an np.array")

        if len(self.faces) != len(set(self.faces)):
            raise ValueError("All faces values must be distinct")

    def change_weight(self, face, weight):
        """
        PURPOSE: Changes the weight of one face of the die object.

        INPUT:
        face - string or numeric. Face value where weight will be changed.
        weight - int, float, or str castable as numeric.  

        OUTPUT: None
        """
        if face not in self.faces:
            raise IndexError(f"{face} not in faces index")
        
        if type(weight)==str:
            if weight.isnumeric():
                weight = int(weight)
            else:
                raise TypeError("Weight must be int or float")
            
        if not (isinstance(weight, int) or isinstance(weight, float)):
            raise TypeError("Weight must be int or float")

        self.df.loc[face,'weight'] = weight

    def roll(self, times=1):
        """
        PURPOSE: Simulates die roll specified number of times.

        INPUT: times - int

        OUTPUT: list 
        """
        face_list = list(self.df.index)
        weight_list = self.df['weight'].to_list()

        result_list = []
        for i in range(times):
            result = random.choices(face_list, weights=weight_list, k=1)
            clean_result = result[0][0]
            result_list.append(clean_result)
        
        return result_list

    def current_state(self):
        """
        PURPOSE: Returns copy of the private die data frame.

        INPUT: None 

        OUTPUT: Data frame
        """
        return self.df

class Game:
    """PURPOSE: Game consists of rolling one or more Die objects one or more times."""

    def __init__(self, die_list):
        """
        PURPOSE: initalize Game object

        INPUT: 
        die_list - list that contains one or more similar Die Object. Each Die object should have same number of sides and associated faces. Dies may have unique weights.
        
        OUTPUT: Most recent play.
        """
        self.die_list = die_list

    def play(self, times):
        """
        PURPOSE: saves the result of dice rolls to a private data frame

        INPUT: 
        times - int. How many times the dice should be rolled. 
        
        OUTPUT: None
        """
        die_result = {}
        roll_number = np.arange(1, times+1)
        for counter, d in enumerate(self.die_list):
            rolls = d.roll(times)
            die_result[counter] = rolls
            

        game_df = pd.DataFrame(die_result, index=roll_number)
        game_df.index.name = "roll_number"
        self.game_df = game_df

    def show_results(self, width):
        """
        PURPOSE: returns copy of the private play data frame.

        INPUT: 
        width - str value "narrow" or "wide". Specifies format of returned data frame. 
        
        OUTPUT: Data frame.
        """
        if width == "wide":
            return self.game_df
        if width == "narrow":
            narrow = self.game_df.stack()
            narrow = narrow.rename_axis(index=["roll_number", "die_number"])
            return narrow
        else:
            raise ValueError("For argument 'weight', pass string 'wide' or 'narrow' in lower case")

class Analyzer:
    """PURPOSE: Analyze Object takes the results of a singel game and computes descriptive statistical properities."""

    def __init__(self, game):
        """ 
        PURPOSE: initalizes Analyzer Object.

        INPUT: montecarlo Game Object.

        OUTPUT: None.
        """
        self.game = game

        if not isinstance(game, Game):
            raise TypeError("Game must be a montecarlo Game class object")
    
    def jackpot(self):
        """ 
        PURPOSE: computes how many times the game resulted in a jackpot.

        INPUT: montecarlo Game Object.

        OUTPUT: int - number of jackpots.
        """
        df = self.game.game_df
        jackpot = 0
        
        roll_list = df.apply(lambda x: [x[c] for c in df.columns], axis=1)

        for l in roll_list.to_list():
            if len(set(l)) == 1:
                jackpot += 1
        
        return jackpot

    def face_counts_per_roll(self):
        """ 
        PURPOSE: Computes how many times a given face is rolled in each event.

        INPUT: None.

        OUTPUT: Data frame.
        """
        df1 = self.game.game_df

        #creating frequency count of each roll
        df1['roll_list'] = df1.apply(lambda x: [x[c] for c in df1.columns], axis=1)
        df1['freq'] = df1['roll_list'].apply(lambda x: {i:x.count(i) for i in set(x)})
        freqs = df1['freq'].to_list()
        roll_number = df1.index

        #creating and cleaning new dataframe
        df2 = pd.DataFrame(freqs, index=roll_number)
        df2 = df2.fillna('0')
        df2 = df2.astype(int)

        return df2

    def combo_count(self):
        """ 
        PURPOSE: Computes the distinct combinations of faces rolled, along with their counts.

        INPUT: None.

        OUTPUT: Data frame with MultiIndex of distinct combinations and counts.
        """
        df3 = self.game.game_df.copy()

        ### sorted list are order independent 
        df3['roll_list'] = df3.apply(lambda x: [x[c] for c in df3.columns], axis=1)
        df3['roll_list_ind'] = df3['roll_list'].apply(lambda x: sorted(x))

        #cleaning and creating multi-index df
        combo = pd.DataFrame(df3["roll_list_ind"].to_list())
        combo_cols = combo.columns.to_list()
        combo = combo.groupby(by=combo_cols).size()
        combo = combo.to_frame(name = "combo_counts")

        return combo


    def perm_count(self):
        """ 
        PURPOSE: Computes the distinct permutations of faces rolled, along with their counts.

        INPUT: None.

        OUTPUT: Data frame with MultiIndex of distinct permutations and counts.
        """
        df4 = self.game.game_df.copy()

        df4_cols = df4.columns.to_list()
        perm = df4.groupby(by=df4_cols).size()
        perm = perm.to_frame(name="perm_counts")

        return perm




        

