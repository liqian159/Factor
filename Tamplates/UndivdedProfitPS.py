#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    UndivdedProfitPS = dv.add_formula('UndivdedProfitPS', 
               "undistributed_profit/capital_stk"
               , is_quarterly=False)
    return UndivdedProfitPS    
