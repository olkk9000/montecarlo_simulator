import numpy as np

class Die:

    def __init__(self, faces: np.array, weight = 1):
        self.faces = faces
        self.weight = weight
        self.df = pd.DataFrame(data={'weight':weight}, index=[faces])

        try:
            len(self.faces) == len(set(self.faces))
        except:
            ValueError("All faces values must be distinct")

    def check_df(self):
        return self.df
