import logging 

# Basic configuration for logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    force = True,
    handlers = [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ] 
)

logger = logging.getLogger('Arithmatic App')

def add(a,b):
    result = a+b
    logger.debug(f'Adding {a}+{b}: {result}')
    return a + b

def subtract(a,b):
    result = a-b
    logger.debug(f'Subtracting {a}-{b}: {result}')
    return a - b

def multiply(a,b):
    result = a*b
    logger.debug(f'Multiplying {a}*{b}: {result}')
    return a * b

def divide(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {a}/{b}: {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero is not allowed')
        return None
    
add(10,15)
subtract(20,5)
multiply(4,6)
divide(10,2)
divide(10,0)