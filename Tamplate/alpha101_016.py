#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha101_016 = dv.add_formula("alpha101_016","-1*Rank(Correlation(Rank(high), Rank(volume), %s))"%(t),
           is_quarterly=False,
           add_data=False)
    return alpha101_016        

