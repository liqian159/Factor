#--------------------------------------------------------- 
#type4 - caculate factor with industry category 


def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.research.signaldigger import process
    from jaqs_fxdayu.data import signal_function_mod as sfm
    defult_param = {'t':20}
    if not param:
        param = defult_param
    t = param['t']
    Open = dv.get_ts("open_adj")
    High = dv.get_ts("high_adj")
    Low = dv.get_ts("low_adj")
    Close = dv.get_ts("close_adj")
    trade_status = dv.get_ts('trade_status')
    mask_sus = trade_status == u'停牌'
    # 剔除掉停牌期的数据　再计算指标
    open_masked = process._mask_df(Open,mask=mask_sus)
    high_masked = process._mask_df(High,mask=mask_sus)
    low_masked = process._mask_df(Low,mask=mask_sus)
    close_masked = process._mask_df(Close,mask=mask_sus)

    MACD = sfm.ta(ta_method='MACD',ta_column=0,Open=open_masked,High=high_masked,Low=low_masked,
        Close=close_masked,Volume=None,timeperiod=20)
    macd= sfm.ta('MACD',Close=close_masked,fastperiod=15, slowperiod=20, signalperiod=5)
    dv.append_df(macd,'macd')
    macdmax = dv.add_formula('macdmax',"-(Ts_Max(macd,%s))"%(t),is_quarterly=False,add_data=True)#日更新指标
    return dv.get_ts('macdmax')









