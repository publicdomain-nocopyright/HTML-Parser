def toggle():
    yield state
    state = ''
    print("test")
print("ok")
toggle()