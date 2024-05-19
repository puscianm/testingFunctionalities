"""
In this module we test decorators
"""
def myDecorator(func):
    """
    This decorator prints the name of the function that is being used.
    """

    def wrapper(*args, **kwargs):
        print(f"Function activated: {func.__name__}")

        resultOfFunction = func(*args, **kwargs)

        return resultOfFunction
    
    return wrapper

def decoratorValidatingAddition(func):
    """
    Whis decorator validates whether arguments are correct.

    Possible additional features:
    * Validating whether result is correct.
    """

    def wrapper(*args, **kwargs):

        for _arg in args:
            print(f"Argument : {_arg}. Argument type: {type(_arg)}")
            if isinstance(_arg, int) == False:
                print(f"Invalid arg: {type(_arg)} with value {_arg}. Expected type int.")
                exit(0)
            result = func(*args, **kwargs)

        return result
    return wrapper

@myDecorator
def addThreeArguements(arg1 : int, arg2 : int, arg3 : int) -> int:
    return arg1 + arg2 + arg3


@decoratorValidatingAddition
def addThreeArguementsWithValidation(arg1 : int, arg2 : int, arg3 : int) -> int:
    return arg1 + arg2 + arg3

if __name__ == "__main__":
    print(addThreeArguements(1, 2, 3))

    print(addThreeArguementsWithValidation(1,2,3.2))
