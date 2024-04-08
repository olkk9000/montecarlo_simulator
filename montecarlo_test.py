from montecarlo import montecarlo
import numpy as np

#testing
# Die1 = montecarlo.Die(faces=np.array([4,5,6]))
# Die2 = montecarlo.Die(faces=np.array([4,5,6]))
# Die3 = montecarlo.Die(faces=np.array([4,5,6]))

# dlist = [Die1, Die2, Die3]

# Game1 = montecarlo.Game(dlist)

# Game1.play(times=6)

# ana1 = montecarlo.Analyzer(Game1)
# # print(ana1.jackpot())

# print(ana1.combo_count())
# #print(ana1.perm_count())


Die1 = montecarlo.Die(faces=np.array([1,2,3]))
Die1.change_weight(1, weight="10")
print(Die1.current_state())

