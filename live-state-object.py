def create_live_object():
    live_object = {"state": None}

    def set_state(new_state):
        live_object["state"] = new_state

    def reset_state():
        live_object["state"] = None

    def get_state():
        return live_object["state"]

    return set_state, reset_state, get_state

# Create first live object instance
set_state1, reset_state1, get_state1 = create_live_object()

# Create second live object instance
set_state2, reset_state2, get_state2 = create_live_object()

# Example usage
set_state1("Active")
set_state2("Inactive")

print(get_state1())  # Output: Active
print(get_state2())  # Output: Inactive

reset_state1()
print(get_state1())  # Output: None
print(get_state2())  # Output: Inactive
