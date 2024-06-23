# Toggle must be aware of its value in the context instead of being global variable. If a different function call, it should reset itself. It should be unique to each function.
# toggle() - returns False or True depending if used before in the context.
def togglere():
    state = True
    while True:
        yield state
        state = not state

# Using the generator
toggle_gen = togglere()

# First call to get initial state
print(next(toggle_gen))  # Output: True

# Subsequent calls to toggle state
print(next(toggle_gen))  # Output: False
print(next(toggle_gen))  # Output: True


def toggle():
    # Initialize a variable to keep track of state
    state = False
    
    def inner():
        nonlocal state  # Use nonlocal to modify the state variable in the enclosing scope
        state = not state  # Toggle the state (True becomes False, False becomes True)
        return state  # Return the toggled state
    
    return inner  # Return the inner function

# Example usage:
toggle_func = toggle()

print("----")
print(toggle_func())  # First call, returns True



def ter():
    print(toggle_func())  # Second call, returns False
    print(toggle_func())  # Third call, returns True
ter()
print(toggle_func())  # Third call, returns True