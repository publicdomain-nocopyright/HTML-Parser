def attributes_parsing():
    attributes = {"is_closing_tag": False, "waffles": 5}
    init_attributes = attributes.copy() 
    
    def reset_attributes():
        nonlocal attributes
        attributes.update(init_attributes)
    
    print("Initial attributes:", attributes)
    
    attributes["waffles"] = 4
    print("Modified attributes:", attributes)
    
    reset_attributes()
    print("Reset attributes:", attributes)


attributes_parsing()
