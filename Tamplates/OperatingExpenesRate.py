#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    OperatingExpenesRate = dv.add_formula('OperatingExpenesRate', 
               "less_selling_dist_exp/total_oper_rev"
               , is_quarterly=False)
    return OperatingExpenesRate    