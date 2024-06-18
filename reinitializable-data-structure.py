def html_attributes_parsing():
    attributes = {"is_closing_tag": False, "waffles": 5}
    init_attributes = attributes.copy() 
        
    
    print("Initial attributes:", attributes)
    
    attributes["waffles"] = 4
    print("Modified attributes:", attributes)
    
    attributes.update(init_attributes)
    print("Reset attributes:", attributes)


html_attributes_parsing()
