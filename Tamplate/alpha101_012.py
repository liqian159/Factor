#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    alpha101_012 = dv.add_formula('alpha101_012', 
               "Sign(Delta(volume,1))*(-1*Delta(close,1))"
               , is_quarterly=False)
    return alpha101_012    
