#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':10}
    if not param:
        param = defult_param
    
    alpha101_018 = dv.add_formula('alpha101_018', 
           '''-1*Rank(((StdDev(Abs((close-open)),%s)+(close-open))+Correlation(close, open, %s)))'''%(param['t1'],param['t2']),
           is_quarterly=False)
    
    return alpha101_018