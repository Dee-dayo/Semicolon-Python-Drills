def calculate_riders_payment(no_of_deliveries :int) -> int:
    if no_of_deliveries < 50:
        return no_of_deliveries * 160 + 5_000
    if no_of_deliveries <= 59:
        return no_of_deliveries * 200 + 5_000
    if no_of_deliveries <= 69:
        return no_of_deliveries * 250 + 5_000
    if no_of_deliveries <= 100:
        return no_of_deliveries * 500 + 5_000


def calculate_riders_payment_take_two(no_of_deliveries: int) -> int:
    base_payment = 5000
    if no_of_deliveries < 50:
        per_delivery_payment = 160
    elif no_of_deliveries <= 59:
        per_delivery_payment = 200
    elif no_of_deliveries <= 69:
        per_delivery_payment = 250
    elif no_of_deliveries <= 100:
        per_delivery_payment = 500
    else:
        return 0

    return no_of_deliveries * per_delivery_payment + base_payment
