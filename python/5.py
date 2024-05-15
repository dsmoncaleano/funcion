def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


string = "1234abcd"
print(f"Original String: {string}")
print(f"Reversed String: {reverse_string(string)}")