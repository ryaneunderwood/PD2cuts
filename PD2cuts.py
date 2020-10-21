import cdms
import pickle
from RQanalysis import RQReader, registercut

pupevs1 = pickle.load( open("/gpfs/fs1/home/m/mdiamond/ryanu/PD2cuts/cPup_23200301_140601.p", "rb" ) )
pupevs2 = pickle.load( open("/gpfs/fs1/home/m/mdiamond/ryanu/PD2cuts/cPup_23200303_231114.p", "rb" ) )

@registercut(branches=['TriggerDetectorNum','TriggerType','TriggerMask'])
def cTrigger_PD2(df):
    return (df['TriggerDetectorNum'] == 1) & ((df['TriggerType']==1) & (df['TriggerMask']==1))
    
@registercut(branches=['PES1OFAmps','PES1OFchisq'])    
def cGoodChi2_PD2_R14(df):
    X=np.array([0, 1e-7, 3e-7, 1e-6 ,2e-6, 2.5e-6, 3.25e-6, 4e-6, 4.5e-6])
    Y=(np.array([36000,36100, 36900, 45000, 110000, 0.2e6, 500000,1420000, 3500000])-34000)*1.3+34000
    tck = interpolate.splrep(X, Y, s=0)
    return df['PES1OFchisq']<interpolate.splev(df['PES1OFAmps'],tck,der=0)
    
@registercut(branches=['TriggerTime','SeriesNumber'])
def cGoodEventRate_PD2_R14(df):
    return ((df['SeriesNumber']==23200303231114) & (df['Triggertime']<31810.4632)) or ((df['SeriesNumber']==23200301140601) & ((df['Triggertime']<28650.068) or (df['Triggertime']>34154.9971)))
    
@registercut(branches=['EventNumber','SeriesNumber'])    
def cNoPileup_PD2_R14(df):
    return (((df['EventNumber'] in pupevs2) & (df['SeriesNumber']==23200303231114)) or ((df['EventNumber'] in pupevs1) & (df['SeriesNumber']==23200301140601)))
             
@registercut(branches=['SeriesNumber'])
def c123biasSeries_PD2_R15(df):
    return ((df['SeriesNumber']==23200814174719) or (df['SeriesNumber']==23200817013541) or (df['SeriesNumber']==23200817133024))

@registercut(branches=['SeriesNumber'])
def c117biasSeries_PD2_R15(df):
    return ((df['SeriesNumber']==23200821185723) or (df['SeriesNumber']==23200823221326) or (df['SeriesNumber']==23200824132810) or (df['SeriesNumber']==23200825214645) or (df['SeriesNumber']==23200826142249) or (df['SeriesNumber']==23200829010441) or (df['SeriesNumber']==23200830010139) or (df['SeriesNumber']==23200831165339) or (df['SeriesNumber']==23200902144505) or (df['SeriesNumber']==23200903232407) or (df['SeriesNumber']==23200905001453))

@registercut(branches=['SeriesNumber'])
def c4sigmathresh_PD2_R15(df):
    return (df['SeriesNumber']>=23200829010441)




OF_to_eV_PD2_R15_117QET=999805207 
OF_to_eV_PD2_R15_123QET=1626483909
OF_to_eV_PD2_R14_120QET=1.18e9
