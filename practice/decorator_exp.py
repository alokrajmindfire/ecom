# A function that extends the behaviour of another function w/0 modifing the base function 
# pass the base function as an argument to the decorator
def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("Hello there!.")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("Fudge added!.")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_creame(flavor):
    print(f"Here is your {flavor} ice-cream")
    
    
get_ice_creame("Vanilla")