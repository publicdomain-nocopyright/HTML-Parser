def somefunction():
    attributes =  {"is_closing_tag": False, "waffles": 5}
    initattributes = attributes.copy()  
    def resetAttributes():
        nonlocal attributes, initattributes 
        attributes = initattributes.copy() 

    print(attributes)
    attributes["waffles"] = 4
    print("init:" + str(initattributes))
    print(attributes)
    resetAttributes()
    print("this suppose to be 5")
    print(attributes)

somefunction()