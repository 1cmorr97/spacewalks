from eva_data_analysis2 import (
    text_to_duration,
    calculate_crew_size
)
import pytest

'''
I need to review how to use pytest, it could save me a ton of time in the future
I couldn't keep up with his typing today though
Can have it send to email?
'''

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10
    # input_value = "10:00"
    # test_result = text_to_duration(input_value) == 10
    # print(f"text_to_duration('10:00) == 10? {test_result}")


def test_text_to_dur_irr():
    assert text_to_duration()


# you can use a decorator, or just use a loop
# can make a dictionary of all the data you would want to use,
# then have each decorator pull out the relevant data for the function
@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2)
    ]
)
def test_calculate_crew_size(input_value, expected_result):
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result
