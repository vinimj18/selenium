# Pytest file names should start with 'test_'
# Test methods should also start with 'test_'

def test_say_hello():
    print("Hello")


def test_say_hi():
    print("Hi")


# Run tests in the console:
# py.test - Run the tests showing how many passed or failed with no other info
# -v - verbose mode, shows more info on the tests
# -s - shows the final result from each test module
