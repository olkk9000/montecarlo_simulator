import unittest
import numpy as np
import pandas as pd
from montecarlo import montecarlo

class MontecarloTestSuite(unittest.TestCase):

    def test_1_die(self):
        #check die creates Die Object
        Die = montecarlo.Die(faces=np.array([4,5,6]))

        self.assertTrue(type(Die), 'montecarlo.montecarlo.Die')


    def test_2_change_weight(self):
        #update a weight and see if the new weight is in the dataframe
        face = 4
        weight = 2 
        Die1 = montecarlo.Die(faces=np.array([4,5,6]))
        Die1.change_weight(face=face, weight=weight)
        df1 = Die1.df
        check = df1['weight'][face]

        self.assertEqual(check, weight)


    def test_3_roll(self):
        #roll the dice and make sure result is list length equals times rolled
        times = 2
        Die2 = montecarlo.Die(faces=np.array([4,5,6]))
        roll_result = Die2.roll(times=times)

        self.assertEqual(len(roll_result), times)

    
    def test_4_current_state(self):
        #create die object and check the current state matches input array
        arr = np.array([4,5,6])
        Die3 = montecarlo.Die(faces=arr)
        state = Die3.current_state()

        self.assertEqual(state.shape[0], len(arr))

    def test_5_game(self):
        #test game creates Game object
        test_die = montecarlo.Die(faces=np.array([4,5,6]))
        Game = montecarlo.Game([test_die])

        self.assertTrue(type(Game), 'montecarlo.montecarlo.Game')


    def test_6_play(self):
        #check that play creats dataframe of appropriate length
        times = 2

        Die4a = montecarlo.Die(faces=np.array([4,5,6]))
        Die4b = montecarlo.Die(faces=np.array([4,5,6]))
        Die4c = montecarlo.Die(faces=np.array([4,5,6]))

        Game4 = montecarlo.Game([Die4a, Die4b, Die4c])
        Game4.play(times=times)

        self.assertTrue(Game4.game_df.shape[0] == times)

    def test_7_show_results_wide(self):
        #check that show result wide results in wide format columns

        Die5a = montecarlo.Die(faces=np.array([4,5,6]))
        Die5b = montecarlo.Die(faces=np.array([4,5,6]))
        Die5c = montecarlo.Die(faces=np.array([4,5,6]))
        dlist5 = [Die5a, Die5b, Die5c]

        Game5 = montecarlo.Game(dlist5)
        Game5.play(times=2)

        df5 = Game5.show_results(width="wide")

        self.assertEqual(len(df5.columns), len(dlist5))

    def test_8_analyzer(self):
        #test analyzer creates Analyzer object
        test_die = montecarlo.Die(faces=np.array([4,5,6]))
        test_game = montecarlo.Game([test_die])
        test_analyzer = montecarlo.Analyzer(test_game)

        self.assertTrue(type(test_analyzer), 'montecarlo.montecarlo.Analyzer')

    def test_9_show_results_narrow(self):
        #check that show results narrow results in MultiIndex

        Die6a = montecarlo.Die(faces=np.array([4,5,6]))
        Die6b = montecarlo.Die(faces=np.array([4,5,6]))
        Die6c = montecarlo.Die(faces=np.array([4,5,6]))

        Game6 = montecarlo.Game([Die6a, Die6b, Die6c])
        Game6.play(times=2)

        df6 = Game6.show_results(width="narrow")

        self.assertEqual(df6.index.names, ['roll_number', 'die_number'])

    def test_10_jackpot(self):
        #check that jackpot returns integer value

        Die7a = montecarlo.Die(faces=np.array([1,2]))
        Die7b = montecarlo.Die(faces=np.array([1,2]))
        Die7c = montecarlo.Die(faces=np.array([1,2]))
        dlist7 = [Die7a, Die7b, Die7c]

        Game7 = montecarlo.Game(dlist7)
        Game7.play(times=2)

        ana7 = montecarlo.Analyzer(Game7)

        jackpot7 = ana7.jackpot()
        
        self.assertTrue(type(jackpot7)==int)

    def test_11_face_counts_per_roll(self):
        #check that face count per roll returns appropriate dataframe 
        #format and length matches times rolled

        times=4
        Die8a = montecarlo.Die(faces=np.array([4,5,6]))
        Die8b = montecarlo.Die(faces=np.array([4,5,6]))
        Die8c = montecarlo.Die(faces=np.array([4,5,6]))
        dlist8 = [Die8a, Die8b, Die8c]

        Game8 = montecarlo.Game(dlist8)
        Game8.play(times=times)

        ana8 = montecarlo.Analyzer(Game8)
        df8 = ana8.face_counts_per_roll()

        self.assertTrue((df8.index.name=='roll_number') & (len(df8)==times))

    def test_12_combo_count(self):
        #verify that combo count creates dataframe with combos column and MultiIndex

        Die9a = montecarlo.Die(faces=np.array([4,5,6]))
        Die9b = montecarlo.Die(faces=np.array([4,5,6]))
        Die9c = montecarlo.Die(faces=np.array([4,5,6]))
        dlist9 = [Die9a, Die9b, Die9c]

        Game9 = montecarlo.Game(dlist9)
        Game9.play(times=4)

        ana9 = montecarlo.Analyzer(Game9)
        df9 = ana9.combo_count()

        self.assertTrue((df9.columns == ['combo_counts']) & (isinstance(df9.index, pd.MultiIndex)))


    def test_13_perm_count(self):
        #verify that perm count creates dataframe with perm column and MultiIndex
        Die10a = montecarlo.Die(faces=np.array([4,5,6]))
        Die10b = montecarlo.Die(faces=np.array([4,5,6]))
        Die10c = montecarlo.Die(faces=np.array([4,5,6]))
        dlist10 = [Die10a, Die10b, Die10c]

        Game10 = montecarlo.Game(dlist10)
        Game10.play(times=4)

        ana10 = montecarlo.Analyzer(Game10)
        df10 = ana10.perm_count()

        self.assertTrue((df10.columns == ['perm_counts']) & (isinstance(df10.index, pd.MultiIndex)))

                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
