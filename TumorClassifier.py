class TumorClassifer:
    """
    This class processes the calculations and data acquired from TumorWeighter and actually applies the weights.
    It also plots the weights.
    """
    def __init__(self, weighter):
        # Store the tumor weighter object
        self.weighter = weighter

        # Retrieve the weights assigned to each tumor property
        self.weights = weighter.get_weights()

        # Retrieve the averages and standard deviation
        stats = weighter.get_stats()
        
        self.malignant_average = stats["malignant_average"]
        self.benign_average = stats["benign_average"]
        
        self.malignant_std = stats["malignant_standarddev"]
        self.benign_std = stats["benign_standarddev"]
