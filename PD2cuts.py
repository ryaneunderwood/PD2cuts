@registercut(branches=['TrigDet','TriggerType','TriggerMask'])
def cTrigger_PD2(df):
    return df['EventType'] == 1 & df['TriggerType']==1 &&df['TriggerMask']==1
    
@registercut(branches=['PES1OFAmps','PES1OFchisq'])    
def cGoodChi2_PD2(df)
    X=np.array([0, 1e-7, 3e-7, 1e-6 ,2e-6, 2.5e-6, 3.25e-6, 4e-6, 4.5e-6])
    Y=(np.array([36000,36100, 36900, 45000, 110000, 0.2e6, 500000,1420000, 3500000])-34000)*1.3+34000
    tck = interpolate.splrep(X, Y, s=0)
    return df['PES1OFchisq']<interpolate.splev(df['PES1OFAmps'],tck,der=0)
    
@registercut(branches=['TriggerTime','SeriesNumber'])
def cGoodEventRate_PD2
    return (df['SeriesNumber']==23200303231114 & df['Triggertime']<31810.4632) or (df['SeriesNumber']==23200301140601 & (df['Triggertime']<28650.068 or df['Triggertime']>34154.9971 ))
    
@registercut(branches=['TriggerTime','SeriesNumber'])    
def cNoPileup_PD2
    return 1