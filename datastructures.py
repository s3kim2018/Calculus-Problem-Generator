class poly_node:
    '''
    Data Structure for Polynomials 
    '''
    def __init__(self, var, num, degree):
        self.var = var
        self.num = num
        self.degree = degree

    def getvar(self):
        return self.var

    def getnum(self):
        return self.num    
    
    def getdeg(self):
        return self.degree

class trig_node:
    '''
    Data Structure for Trig Functions
    '''
    def __init__(self, trig, function):
        self.trig = trig
        self.func = function

    def gettrig(self):
        return self.trig
    
    def getfunc(self):
        return self.func
        
class log_node: 
    '''
    Data Structure for Trig and Exponential Functions
    '''
    def __init__(self, exp, function):
        self.exp = exp
        self.func = function
    
    def getexp(self):
        return self.exp
    
    def getfunc(self):
        return self.func