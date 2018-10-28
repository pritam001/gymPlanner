from collections import OrderedDict


class MuscleGroup:

    # create a muscleGroup class for a particular muscle
    # TODO: use muscle category to manipulate init
    def __init__(self, _name, consequential=[], power=100, recovery=1, imbalanced=False, injured=False):
        self._name = _name
        self.power = power
        self.recovery = recovery
        self.consequential = consequential
        self.imbalanced = imbalanced
        self.injured = injured

    def show_muscle_status(self):
        status = OrderedDict()
        status["_name"] = self._name
        status["power"] = self.power
        status["recovery"] = self.recovery
        status["consequential"] = self.consequential
        status["imbalanced"] = self.imbalanced
        status["injured"] = self.injured
        return status
