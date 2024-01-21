from base.base_test import BaseTest


class TestWorkoutCalc(BaseTest):

    def test_01_calculate_workout_intensity(self):
        self.workout_calc_page.add_intensity()

    def test_02_calculate_workout_using_hansons(self):
        self.workout_calc_page.add_hansons()

    def test_03_calculate_workout_using_mcmillan(self):
        self.workout_calc_page.add_mcmillan()

    def test_04_calculate_workout_using_tinman(self):
        self.workout_calc_page.add_tinman()

    def test_05_calculate_workout_using_palladino(self):
        self.workout_calc_page.add_palladino()
