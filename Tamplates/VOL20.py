#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    VOL20 = dv.add_formula("VOL20","Ts_Mean(turnover_ratio,%s)"%(t),
           is_quarterly=False,
           add_data=False)
    return VOL20        