def boolean_toggle():
	global booleanstate
	if 'booleanstate' not in globals():
		booleanstate = False
		print("test")
	booleanstate = not booleanstate
	return booleanstate
    
    
print(boolean_toggle())
print(boolean_toggle())