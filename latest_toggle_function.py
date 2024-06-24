import inspect

def toggle():
    # Initialize global variables if they don't exist
    if 'toggle_count' not in globals():
        globals()['toggle_count'] = 0
        globals()['last_caller'] = None
    
    # Get the name of the function calling toggle()
    caller_frame = inspect.currentframe().f_back
    caller_name = caller_frame.f_code.co_name
    
    # Reset toggle count if called from a different context
    if globals()['toggle_count'] > 0 and caller_name != globals()['last_caller']:
        globals()['toggle_count'] = 0
    
    # Increment the toggle count
    globals()['toggle_count'] += 1
    globals()['last_caller'] = caller_name
    
    return globals()['toggle_count']

# Example usage:
def example_function():
    print(toggle())  # Output: 1
    print(toggle())  # Output: 2
    print(toggle())  # Output: 3

example_function()
print(toggle())  # Output: 1 (reset because called outside example_function)
print(toggle())  # Output: 2
