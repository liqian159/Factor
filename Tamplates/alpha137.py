#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    alpha137 = dv.add_formula('alpha137',"16*(close-Delay(close,1)+(close-open)/2+Delay(close,1)-Delay(open,1))/If((Abs(high-Delay(close,1))>Abs(low-Delay(close,1))&&Abs(high-Delay(close,1))>Abs(high-Delay(low,1)),Abs(high-Delay(close,1))+Abs(low-Delay(close,1))/2+Abs(Delay(close,1)-Delay(open,1))/4,If(Abs(low-Delay(close,1))>Abs(high-Delay(low,1))&&Abs(low-Delay(close,1))>Abs(high-Delay(close,1)),Abs(low-Delay(close,1))+Abs(high-Delay(close,1))/2+Abs(Delay(close,1)-Delay(open,1))/4,Abs(high-Delay(low,1))+Abs(Delay(close,1)-Delay(open,1))/4)))*Max(Abs(high-Delay(close,1)),Abs(low-Delay(close,1)))", is_quarterly=False)
    return alpha137 