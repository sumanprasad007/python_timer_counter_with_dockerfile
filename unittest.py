import unittest
from countdown_timer import countdown
import io
import sys
import time

class CountdownTestCase(unittest.TestCase):
    def test_countdown(self):
        # Test case 1: Countdown from 5 seconds
        expected_output = ['00:05', '00:04', '00:03', '00:02', '00:01', 'stop']
        captured_output = io.StringIO()
        sys.stdout = captured_output

        countdown(5)
        output = captured_output.getvalue().strip().split('\n')
        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)

        # Test case 2: Countdown from 0 seconds
        expected_output = ['stop']
        captured_output = io.StringIO()
        sys.stdout = captured_output

        countdown(0)
        output = captured_output.getvalue().strip().split('\n')
        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)

        # Test case 3: Countdown from a large number of seconds
        expected_output = ['01:40', '01:39', '01:38', '01:37', '01:36', 'stop']
        captured_output = io.StringIO()
        sys.stdout = captured_output

        countdown(100)
        output = captured_output.getvalue().strip().split('\n')
        sys.stdout = sys.__stdout__

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()


#------------------------------------------------------------------------------------------
# import unittest
# from countdown_timer import countdown

# class CountdownTestCase(unittest.TestCase):
#     def test_countdown(self):
#         # Test case 1: Countdown from 5 seconds
#         # Start the countdown from 5 seconds
#         countdown(5)
#         # Perform your assertions here to validate the output or behavior

#         # Test case 2: Countdown from 0 seconds
#         # Start the countdown from 0 seconds
#         countdown(0)
#         # Perform your assertions here to validate the output or behavior

#         # Test case 3: Countdown from a large number of seconds
#         # Start the countdown from a large number of seconds, e.g., 100
#         countdown(100)
#         # Perform your assertions here to validate the output or behavior

#         # Add more test cases if needed

# if __name__ == '__main__':
#     unittest.main()


#------------------------------------------------------------------------------------------
# import time

# def test_countdown():
#     # Test case 1: Countdown from 5 seconds
#     start_time = time.time()
#     countdown(5)
#     elapsed_time = time.time() - start_time
#     assert elapsed_time >= 5 and elapsed_time < 6, "Test case 1 failed"

#     # Test case 2: Countdown from 0 seconds
#     start_time = time.time()
#     countdown(0)
#     elapsed_time = time.time() - start_time
#     assert elapsed_time < 1, "Test case 2 failed"

#     # Test case 3: Countdown from a large number of seconds
#     start_time = time.time()
#     countdown(100)
#     elapsed_time = time.time() - start_time
#     assert elapsed_time >= 100 and elapsed_time < 101, "Test case 3 failed"

#     # Add more test cases if needed

#     print("All test cases passed")

# test_countdown()
