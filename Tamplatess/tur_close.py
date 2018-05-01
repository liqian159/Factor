#--------------------------------------------------------- 
#type4 - caculate factor with industry category 


def run_formula(dv):
    import pandas as pd
    turnover_ratio = dv.get_ts('turnover_ratio')
    close = dv.get_ts('close')
    tur_close = close.mul(turnover_ratio,axis=0)#¼ÆËã¹«Ê½
    tur_close = pd.DataFrame({sec_symbol: -value.values for sec_symbol, value in tur_close.iteritems()}, index=close.index)
    dv.append_df(tur_close,'tur_close')    
    return dv.get_ts('tur_close')



