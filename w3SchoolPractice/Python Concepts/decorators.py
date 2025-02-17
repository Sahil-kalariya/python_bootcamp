import time

def cache_with_expiry(expiry_time):
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())
            if key in cache:
                value, timestamp = cache[key]
                if time.time() - timestamp < expiry_time:
                    print("Retrieving result from cache...")
                    return value
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator



@cache_with_expiry(expiry_time=5)  
def calculate_multiply(x, y):
    print("Calculating product of two numbers...")
    return x * y


print(calculate_multiply(23, 5))  
print(calculate_multiply(23, 5)) 
time.sleep(5)
print(calculate_multiply(23, 5))  
