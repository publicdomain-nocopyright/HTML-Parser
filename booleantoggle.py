def boolean_toggle():
	global booleanstate
	if 'booleanstate' not in globals():
		booleanstate = False
	booleanstate = not booleanstate
	return booleanstate
    
    
print(toggle = boolean_toggle())
print(toggle = boolean_toggle())