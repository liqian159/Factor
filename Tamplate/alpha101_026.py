#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5,'t3':5,'t4':3}
    if not param:
        param = defult_param
    
    alpha101_026 = dv.add_formula('alpha101_026', 
           '''1* Ts_Max(Correlation(Ts_Rank(volume, %s), Ts_Rank(high, %s), %s), %s)'''%(param['t1'],param['t2'],param['t3'],param['t4']),
           is_quarterly=False)
    
    return alpha101_026