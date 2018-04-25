#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':3}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha101_015 = dv.add_formula("alpha101_015","-1*Ts_Sum(Rank(Correlation(Rank(high), Rank(volume),%s)), %s)"%(t,t),
           is_quarterly=False,
           add_data=False)
    return alpha101_015        

