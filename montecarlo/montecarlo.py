import numpy as np
import pandas as pd

class Die:

    def __init__(self, faces: np.array, weight = 1):
        self.faces = faces
        self.weight = weight
        self.df = pd.DataFrame(data={'weight':weight}, index=[faces])

        try:
            len(self.faces) == len(set(self.faces))
        except:
            ValueError("All faces values must be distinct")

    def current_state(self):
        return self.df
