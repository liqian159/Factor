#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    alpha150 = dv.add_formula('alpha150', 
               "(close+high+low)/3*volume"
               , is_quarterly=False)
    return alpha150    

