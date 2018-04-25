#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':6}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha189 = dv.add_formula("alpha189","Ts_Mean(Abs(close-Ts_Mean(close,%s)),%s)"%(t,t),
           is_quarterly=False,
           add_data=False)
    return alpha189        