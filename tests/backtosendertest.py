from drills.backtosenderlogistics import calculate_riders_payment, calculate_riders_payment_take_two


def test_function_can_calculate_riders_pay():
    assert calculate_riders_payment(25) == 9_000


def test_function_can_calculate_riders_pay2():
    assert calculate_riders_payment(55) == 16_000


def test_function_can_calculate_riders_pay3():
    assert calculate_riders_payment(62) == 20_500


def test_function_can_calculate_riders_pay4():
    assert calculate_riders_payment(80) == 45_000

def test_function_can_calculate_riders_pay5():
    assert calculate_riders_payment_take_two(25) == 9_000