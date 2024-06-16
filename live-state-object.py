def create_live_object(*state_names):
    live_object = {state_name: None for state_name in state_names}

    def set_states(**kwargs):
        for state_name, new_state in kwargs.items():
            if state_name in live_object:
                live_object[state_name] = new_state
            else:
                raise KeyError(f"State '{state_name}' does not exist")

    def reset_states(*state_names):
        for state_name in state_names:
            if state_name in live_object:
                live_object[state_name] = None
            else:
                raise KeyError(f"State '{state_name}' does not exist")

    def get_states(*state_names):
        return {state_name: live_object[state_name] for state_name in state_names if state_name in live_object}

    return set_states, reset_states, get_states

# Create a new live object instance with multiple states
set_states, reset_states, get_states = create_live_object("state1", "state2", "state3")

# Example usage
set_states(state1="Active1", state2="Active2", state3="Active3")

print(get_states("state1", "state2", "state3"))  # Output: {'state1': 'Active1', 'state2': 'Active2', 'state3': 'Active3'}

reset_states("state1", "state2")

print(get_states("state1", "state2", "state3"))  # Output: {'state1': None, 'state2': None, 'state3': 'Active3'}
