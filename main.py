from functions import *

how_to_call = "If you meant to call this function, please use regular python syntax.\n"

def main_loop():
    '''
    Main loop handling user console input and output.

    Parameters:
    None

    Returns:
    None
    
    '''
    
    print("call one of these functions: z_1_a, z_1_b, z_2, z_3, z_4, z_5")
    while True:
        command = input()

        if("exit" in command or "quit" in command):
            break
        
        response = None
        try:
            response = eval(command)
        except:
            print("invalid query")
            
        if(response != None):
            print(response)
        if(type(response) == type(z_1_a)):
            print(how_to_call)
            help(response)

if __name__ == '__main__':
    main_loop()
