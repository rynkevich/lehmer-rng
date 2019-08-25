def read_positive_integer_from_keyboard(name, validator=lambda x: True, error_message=None):
    return read_from_keyboard(name, int, lambda x: x > 0 and validator(x),
                              error_message=error_message if error_message else f'{name} must be a positive integer')


def read_from_keyboard(name, type_constructor, validator=lambda x: True, error_message=None):
    result = None
    is_valid = False
    while not is_valid:
        raw_input = input(f'{name}: ')
        result = safe_cast(raw_input, type_constructor)
        is_valid = result is not None and validator(result)
        if not is_valid:
            if error_message is not None:
                print(error_message)
    return result


def safe_cast(value, type_constructor, default=None):
    try:
        return type_constructor(value)
    except (ValueError, TypeError):
        return default
