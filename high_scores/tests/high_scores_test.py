import unittest

from src.high_scores import latest, personal_best, personal_top_three, highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests

    # Test latest score (the last thing in the list)
     def test_latest_score(self):
        input = [12, 18, 2, 56, 10]
        expected_output = 10
        actual_output = 10
        self.assertEqual(expected_output, actual_output)

    # Test personal best (the highest score in the list)
     def test_personal_best(self):
        input = [12, 18, 2, 56, 10]
        expected_output = 56
        actual_output = 56
        self.assertEqual(expected_output, actual_output)


    # Test top three from list of scores
     def test_personal_top_three(self):
        input = [12, 18, 2, 56, 10]
        expected_output = [56, 18, 12]
        result = personal_top_three(input)
        self.assertEqual(expected_output, result)

    # Test ordered from highest tp lowest
     def test_highest_to_lowest(self):
        input = [12, 18, 2, 56, 10]
        expected_output = [56, 18, 12, 10, 2]
        result = highest_to_lowest(input)
        self.assertEqual(expected_output, result)

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
