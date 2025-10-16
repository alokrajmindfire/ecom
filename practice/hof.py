# HOF - a function that either : 
    # 1. accepts a function as an argument
    # 2. or return a function
#  In python function are trated as object


def loud(text):
    return text.upper()
def quite(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)


def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(10)
if __name__ == '__main__':
    hello(quite)
    print(divide(6))
    
    
# generator function
# generates values on-the-fly, it stores information
# they are lazy
def my_gen():
    for i in range(50000):
        yield i
        
        
gene = my_gen()

print(next(gene))
print(next(gene))

for i in gene:
    print(i)