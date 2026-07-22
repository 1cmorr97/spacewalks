from eva_data_analysis2 import text_to_duration


def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 11
    print("hi")
    # input_value = "10:00"
    # test_result = text_to_duration(input_value) == 10
    # print(f"text_to_duration('10:00) == 10? {test_result}")


test_text_to_duration_integer()
