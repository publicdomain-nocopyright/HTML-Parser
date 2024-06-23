# Toggle must be aware of its value in the context instead of global variable. If a different function call, it should reset itself. It should be unique to each function.

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
    pass
