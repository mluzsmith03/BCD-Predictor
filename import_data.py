import os

#This is an import file, we're essentially just importing and separating the data
filename = "wdbc.data"

import pandas as pd
def import_data(filename):
    # Check if dataset exists
    if not os.path.isfile(filename):
        raise FileNotFoundError("Dataset file not found.")
        
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            #the following data contains the mean for each tumor
            values = line.strip().split(",")
            id = int(values[0])
            #note that this only returns the mean data
            #all of our calculations will these values only
            data[id] = {
                "Diagnosis": values[1],
                "Radius": float(values[2]),
                "Texture": float(values[3]),
                "Perimeter": float(values[4]),
                "Area": float(values[5]),
                "Smoothness": float(values[6]),
                "Compactness": float(values[7]),
                "Concavity": float(values[8]),
                "Concave Points": float(values[9]),
                "Symmetry": float(values[10]),
                "Fractal Dimension": float(values[11])
            }
    
    return data
