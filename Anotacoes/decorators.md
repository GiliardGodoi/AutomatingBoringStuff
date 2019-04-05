# Simples explicação sobre decorators

'''python
def decorator_function_name(function):

    def wrapper(param):
        #do something cool

        function(param.value)

        return "success"

    return wrapper

@decorator_function_name
def yeah_function(value):
    #do something with value

    return value 
    
'''