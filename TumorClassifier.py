class TumorClassifer:
    """
    This class processes the calculations and data acquired from TumorWeighter and actually applies the weights.
    It also plots the weights"""
    def __init__(self, weighter):
        self.weighter = weighter