def create_live_object():
    live_object = {"state": None}

    def set_state(new_state):
        live_object["state"] = new_state

    def reset_state():
        live_object["state"] = None

    def get_state():
        return live_object["state"]

    return set_state, reset_state, get_state

# Create a new live object instance
set_state, reset_state, get_state = create_live_object()

# Example usage
set_state("Active")
print(get_state())  # Output: Active

reset_state()
print(get_state())  # Output: None
