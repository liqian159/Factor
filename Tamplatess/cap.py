#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    cap = dv.add_formula("cap","(Ts_Max(TTM(capital_stk),%s))"%(t),
           is_quarterly=True,
           add_data=False)
    return cap        

