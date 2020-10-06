import os
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear')
def RepresentsInt(s):
    """Returns true if it is an integer, returns false if it is not"""
    try: 
        int(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False