def boolean_toggle():
	global booleanstate
	if 'booleanstate' not in globals():
		booleanstate = False
	booleanstate = not booleanstate
	return booleanstate
    
toggle = boolean_toggle()
print(toggle)
toggle = boolean_toggle()
print(toggle)

# Generator and yield method is better, allowing for intercepting
# if two different functions use booleanstate variable
# One can toggle the previous to false, leading to unintended problems.