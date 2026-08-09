def calculate_discount(price, discount_percent):
    """Applies a discount percentage to a price."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price - (price * discount_percent / 100)


def is_valid_email(email):
    """Very basic email format check."""
    return "@" in email and "." in email.split("@")[-1]