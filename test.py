import os
import time

from countdown_timer import countdown

def test_countdown(capsys):
    # Set timer for 3 seconds
    num = 3
    countdown(num)
    # Check that the timer printed the correct output
    captured = capsys.readouterr()
    assert captured.out == "00:03\r00:02\r00:01\rstop\n"
    
def test_environment_variable(capsys):
    # Set environment variable to 10 seconds
    os.environ['TIMER_SECONDS'] = '10'
    # Run countdown function with environment variable
    exec(open('countdown_timer.py').read())
    
    # Check that the timer printed the correct output
    captured = capsys.readouterr()
    assert "stop\n" in captured.out
    assert "Successfully, run the timer🎉" in captured.out
