class TumorClassifier:
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
        """
        This method calculates the weighted score of the tumor by using the measurements and their weights.
        """
        total_score = 0

        categories = [
            "Radius", "Texture", "Perimeter", "Area", "Smoothness", "Compactness", "Concavity",
            "Concave Points", "Symmetry", "Fractal Dimension"
        ]
        # Obtaining the tumor values in order
        tumor_values = []
        for category in categories:
            tumor_values.append(tumor_data.get(category))

        # Obtaining the weight values in order
        weight_values = []
        for category in categories:
            weight_values.append(self.weights.get(category)) 
        # Loop through each tumor measurement and using the zip function to pair the category, measurement
        # values, and weights together.
        
        for category, value, weight in zip( categories, tumor_values, weight_values):
            std = standarddevs[category]
                
            # Avoid division by zero
            if std != 0:
                difference = (value - averages[category]) / std

                # Apply the user-defined weight
                total_score += weight * (difference ** 2)

        return total_score
