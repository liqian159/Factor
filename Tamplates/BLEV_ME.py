#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    BLEV_ME = dv.add_formula('BLEV_ME', 
               "tot_non_cur_liab/(tot_non_cur_liab+tot_liab_shrhldr_eqy)"
               , is_quarterly=False)
    return BLEV_ME    