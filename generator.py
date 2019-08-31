import random
from datastructures import poly_node
from datastructures import trig_node
from datastructures import log_node 



def polynomial_gen():
    '''
    Generates a random polynomial in list format
    '''
    polynomial = []
    signs = ['+', '-']
    length = random.randint(1,5)
    polynomial.append(length) #first element of the datastructure stores the length of the polynomial.
    for _ in range(0, length):
        polynomial.append(poly_node('x', random.randint(1,25), random.randint(1,6)))
        polynomial.append(signs[random.randint(0, 1)])
    return polynomial

def trig_gen(): 
    '''
    Generates a random trig function in list format
    '''
    returnlst = []
    signs = ['+', '-']
    length = random.randint(1,3)
    returnlst.append(length)
    trig = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']
    for _ in range (0, length):
        returnlst.append(trig_node(trig[random.randint(0, 5)], 'random polynomial'))
        returnlst.append(signs[random.randint(0, 1)])
    return returnlst

def log_gen(): 
    '''
    Generates a random log, ln function in list format
    I decided to include the exponential function :) 
    '''
    returnlst = []
    length = random.randint(1,3)
    returnlst.append(length)
    signs = ['+', '-']
    log = ['log', 'ln', 'e']
    for _ in range (0, length):
        returnlst.append(log_node(log[random.randint(0, 2)], 'random polynomial'))
        returnlst.append(signs[random.randint(0, 1)])
    return returnlst

def trig_decompressor(trig):
    decompressed = ''
    count = 1
    for _ in range(trig[0]):
        if count % 2 == 1: #count is odd, it is a node
            decompressed += trig[count].gettrig()
            decompressed += '('
            decompressed += random_function_generator()
            decompressed += ')'
            count+=1 
        elif count % 2 == 0 and count != trig[0]: #it is a sign and not the last element
            decompressed += trig[count]
            count +=1
        else: #last item in element 
            count += 1
    return decompressed

def log_decompressor(log): 
    decompressed = ''
    count = 1
    for _ in range(log[0]):
        if count % 2 == 1: #count is odd, it is a node
            if(log[count].getexp() == 'e'): #e functions has an exponenet! 
                decompressed += log[count].getexp()
                decompressed += '^'
                decompressed += random_function_generator()
            else:
                decompressed += log[count].getexp()
                decompressed += '('
                decompressed += random_function_generator()
                decompressed += ')'
            count+=1 
        elif count % 2 == 0 and count != log[0]: #it is a sign and not the last element
            decompressed += log[count]
            count +=1
        else: #last item in element 
            count += 1
    return decompressed
        

def polynomial_decompressor(polynomial):
    decompressed = ''
    count = 1  
    for _ in range(polynomial[0]):                
        if count % 2 == 1: #if i is odd (means it is a node)
            if polynomial[count].getdeg() == 1:
                decompressed += str(polynomial[count].getnum())
                decompressed += polynomial[count].getvar()        
            else:
                decompressed += str(polynomial[count].getnum())
                decompressed += polynomial[count].getvar()
                decompressed += '^'
                decompressed += str(polynomial[count].getdeg())
                count += 1
        elif count % 2 == 0 and count != polynomial[0]: #not a node, it is a sign
            decompressed += polynomial[count]
            count += 1
        else: #the last item on the polynomial list must not be a sign
            count += 1
    return decompressed 

def random_function_generator(): 
    '''
    generates a random polynomial, trig, x, log, exponential function
    returns a decompressed, list format of these polynomials so it can ba spliced to other functions.
    '''
    random_func = [polynomial_gen, polynomial_gen, polynomial_gen, trig_gen, log_gen]
    length = random.randint(0, 4)

    if (random_func[length] is polynomial_gen):
        return polynomial_decompressor(random_func[length]())
    elif (random_func[length] == trig_gen):
        return trig_decompressor(random_func[length]())
    elif (random_func[length] == log_gen):
        return log_decompressor(random_func[length]())

