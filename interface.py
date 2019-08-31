from generator import * 
import random


def product_rule():
    string = ''
    string += random_function_generator()
    string += " "
    string += '*'
    string += " "
    string += random_function_generator()
    return string

def quotient_rule():
    string = ''
    string += random_function_generator()
    string += " "
    string += '/'
    string += " "
    string += random_function_generator()
    return string

def power_rule():
    string = ''
    string += '('
    string +=random_function_generator()
    string += ')^'
    string += str(random.randint(1,13))
    return string


def main():

    def check(input):
        try:
            int(input)
        except: 
            print("enter a valid number")
            print("\n\n\n")
            return False
        return True
        

    def generate(chain_rule, product_rule_num, quotient_rule_num, power_rule_num): 
        for _ in range (0, chain_rule):
            print(random_function_generator())
        for _ in range (0, product_rule_num):
            print(product_rule())
        for _ in range (0, quotient_rule_num):
            print(quotient_rule())
        for _ in range (0, power_rule_num):
            print(power_rule())
        print("\n\n\n")
        print("Thank You, Craeted by Brian Kim")

    
    print("-------------------------------------------")
    print("Welcome to the Calculus Problem Generator")
    print("-------------------------------------------")
    variable = raw_input('Press Enter to Start\n')
    if (variable is ''):
        while (True):
            print("\n\n\n")
            print("This Software Assumes Students have learned to differentiate Polynomials, Trig, Logarithmic, and Exponential Functions")
            print("This Software Assumes that Students have familiarity with the Chain Rule")
            no_of_q = raw_input("How Many Questions do you want? : ")
            if check(no_of_q) is True:
                while(True):
                    print("What kind of question do you want?")
                    chain_rule = raw_input('How Many Chain Rule Questions do you want?\n')
                    if check(chain_rule) is False:
                        continue 
                    product_rule_num = raw_input('How Many Product Rule Questions do you want?\n')
                    if check(product_rule_num) is False:
                        continue 
                    quotient_rule_num = raw_input('How Many Quotient Rule Questions do you want?\n')
                    if check(quotient_rule_num) is False:
                        continue 
                    power_rule_num = raw_input('How Many Power Rule Questions do you want?\n')
                    if check(power_rule_num) is False:
                        continue
                    if int(chain_rule) + int(product_rule_num) + int(quotient_rule_num) + int(power_rule_num) != int(no_of_q):
                        print("Question Types don't add up to the total question number")
                        continue
                    generate(int(chain_rule), int(product_rule_num), int(quotient_rule_num), int(power_rule_num))
                    break
            break
    else:
        print("Wrong key pressed")
        print("\n\n\n\n\n")
        main() #Infinite Recursion. Space is 1 since it closes all previous frames.

main()