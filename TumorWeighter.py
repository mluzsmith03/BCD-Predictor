
from import_data import import_data

class TumorWeighter:
    """
    In this class, we are allowing the user to define weights for each property.
    """
    def __init__(self, filename):
        self.__data = import_data(filename) #all of them will be private so they can't be modified
        self.__weights = {}
        self.__malignant_average = {}
        self.__benign_average = {}
        self.__malignant_standarddev = {}
        self.__benign_standarddev = {}
        #get a copy instead in TumorClassifer

    
def get_weights(self):
    categories = [
        "Radius", "Texture", "Perimeter", "Area", "Smoothness", "Compactness", "Concavity", "Concave Points",
        "Symmetry", "Fractal Dimension"
    ]

    while True:
        self.weights = {}
        total_weight = 0 #starting value for summing the weights

        for category in categories:
            self.weights[category] = float(input(f"Enter weight for {category} (0.99 = 99%, ensure they add to 100): "))

            if self.weights[category] < 0 or self.weights[category] > 1:
                print("Weights must be between 0 and 1. Please try again.")
                break

            total_weight = total_weight + self.weights[category]

        else:
            if abs(total_weight - 1.0) > 1e-6:
                print("The values do not sum to 100%. Please try again.")
                continue

            print("The weights are as follows:", self.weights)
            choice = input("Are these correct? [Y/N]: ")

            if choice.upper() == "Y":
                return self.weights
            else:
                print("Please input your weights again.")


def normalize_data(self):
    #we're going to calculate the mean for the malignant and benign values separately
    #first we need to find the malignant values in import_data
    self.malignant_data = {}
    self.benign_data = {}
    self.malignant_average = {} #these are the averages for each category, ids not necessary
    self.benign_average = {}

    self.malignant_standarddev = {}
    self.benign_standarddev = {}

    for tumor_id, properties in self.data.items():
        if properties["Diagnosis"] == "M":
                self.malignant_data[tumor_id] = properties
        else:
            self.benign_data[tumor_id] = properties

    num_malignant = len(self.malignant_data)
    num_benign = len(self.benign_data)

    categories = [
        "Radius", "Texture", "Perimeter", "Area", "Smoothness", "Compactness", "Concavity", "Concave Points",
        "Symmetry", "Fractal Dimension"
        ]

    #the following gives us the average malignant and benign values so we can compare the data to it
    for category in categories:
        self.malignant_average[category] = sum(properties[category] for properties in self.malignant_data.values())/num_malignant
        self.benign_average[category] = sum(properties[category] for properties in self.benign_data.values())/num_benign

    for category in categories:
        self.malignant_standarddev[category] = (sum((properties[category] - self.malignant_average[category])**2
                                               for properties in self.malignant_data.values())/num_malignant)**0.5
        self.benign_standarddev[category] = (sum((properties[category] - self.benign_average[category])**2
                                               for properties in self.benign_data.values())/num_benign)**0.5

    return self.malignant_average, self.benign_average, self.malignant_standarddev, self.benign_standarddev

def get_stats(self): #this is for the class TumorWeighter to have access to copies of the data
    return {"malignant_average": self.__malignant_average.copy(), "benign_average": self.__benign_average.copy(), 
            "malignant_standarddev": self.__malignant_standarddev.copy(), "benign_standarddev": self.__benign_standarddev.copy()
            }
