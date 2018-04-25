#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':10}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha101_040 = dv.add_formula("alpha101_040","(-1* Rank(StdDev(high, %s)))* Correlation(high, volume, %s)"%(t,t),
           is_quarterly=False,
           add_data=False)
    return alpha101_040   