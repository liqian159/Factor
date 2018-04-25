#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param
        
    t = param['t']
    
    VOL120 = dv.add_formula("VOL120","Ts_Mean(turnover_ratio,%s)"%(t),
           is_quarterly=False,
           add_data=False)
    return VOL120        