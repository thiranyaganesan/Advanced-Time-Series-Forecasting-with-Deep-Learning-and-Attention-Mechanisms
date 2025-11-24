import pandas as pd
import numpy as np

def load_and_preprocess(path):
    df = pd.read_csv(path)
    return df