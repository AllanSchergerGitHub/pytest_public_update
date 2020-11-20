from src import main_prod


def integration_test(val):
    val2 = 3
    test_from_method = main_prod.mandatory_method(val2)
    test2_from_method = main_prod.optional_method(val)
    return test_from_method, test2_from_method


def test_setup_integration_test():
    test_this = integration_test(1)

    print("test_this =", test_this[1])
    assert test_this[1] == 1
