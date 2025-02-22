"""
    - Call by value and call by reference in python.

        Call by Value:
            In languages that support call by value, a function gets a copy of the variable's value.
            Changes inside the function do not affect the original variable.
            In Python, immutable objects (e.g., int, float, str, tuple) behave similarly to call by value because
            their values cannot be changed in place.


        Call by Reference:
            In languages that support call by reference, a function receives a reference to the original variable.
            Changes made inside the function affect the original variable.
            In Python, mutable objects (e.g., list, dict, set) behave similarly to call by reference because
            they can be modified in place.

    - How is work static method in python?
"""

def modify(x):
    x[1] = 10  # This changes the local copy, not the original variable

class testOop:

    @staticmethod
    def modify(x):
        print("modify method which is staticmethod is executed...!")
        x = 10


integer_variable = 5 # immutable like int, str, float, tuple ...
list_variable = [1, 0, 5, 6] # mutable like list
test_oop = testOop()
# ------------------------------------------------------------------------------------------

# Output: 5 (Original variable remains unchanged)
# test_oop.modify(a)
# print(integer_variable)  # Output: 5 (Original variable remains unchanged)

test_oop.modify(list_variable)
print(list_variable) # not changed in staticmethod.

modify(list_variable)
print(list_variable) # changed because the list in python is mutable.
