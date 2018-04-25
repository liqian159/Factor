#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':5}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha101_013 = dv.add_formula("alpha101_013","-1*Rank(Covariance(Rank(close), Rank(volume), %s))"%(t),
           is_quarterly=False,
           add_data=False)
    return alpha101_013