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

    def apply_weights(self, tumor_data, averages, standarddevs):
        total_score = 0

        # Loop through each tumor measurement
        for category, value in tumor_data.items():
            if category in self.weights:
                std = standarddevs[category]
                
                # Avoid division by zero
                if std != 0:
                    difference = (value - averages[category]) / std

                    # Apply the user-defined weight
                    total_score += self.weights[category] * (difference ** 2)

        return total_score
