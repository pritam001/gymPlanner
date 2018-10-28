from muscle import MuscleGroup


class Body:

    def __init__(self):
        self.muscles = self.generate_default_body()

    def generate_default_body(self):
        default_body = self.add_all_muscles(["Shoulders", "Chest"])
        return default_body

    def show_body_status(self):
        muscles = self.muscles
        status = list(map(lambda x: x.show_muscle_status(), muscles))
        return status

    @staticmethod
    def add_all_muscles(muscle_list):
        muscles = []
        for m in muscle_list:
            muscle = MuscleGroup(m)
            muscles.append(muscle)
        return muscles


