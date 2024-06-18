def somefunction():
    # Initial attributes setup
    attributes = {"is_closing_tag": False, "waffles": 5}
    init_attributes = attributes.copy()  # Make a copy for resetting
    
    def reset_attributes():
        nonlocal attributes
        attributes.clear()
        attributes.update(init_attributes)
    
    # Print initial attributes
    print("Initial attributes:", attributes)
    
    # Modify attributes
    attributes["waffles"] = 4
    print("Modified attributes:", attributes)
    
    # Reset attributes
    reset_attributes()
    print("Reset attributes:", attributes)

somefunction()
