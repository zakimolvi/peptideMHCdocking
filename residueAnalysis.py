"""
Analyze the interactions contributing to difference between two structures:
pMGAP and MGAPwt

ddg = mean(dG_wt) - mean(dG_phos)
"""
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statannot import add_stat_annotation

pairedPal = sns.color_palette(['#4CACBC', '#A0D995' ])
sns.set(palette=pairedPal, style='ticks', context='notebook')

#total energy term analysis
df = pd.read_csv('a3_scores_annot.csv') #input csv of scorefile rows annotated with peptide (pMGAP or MGAPwt)
df = df[df['Peptide'] == 'MGAP']

energy_terms = ['fa_sol', 'fa_atr', 'rama_prepro', 'fa_dun', 'p_aa_pp',
                'omega', 'lk_ball_wtd', 'hbond_sr_bb', 'fa_rep', 'fa_elec',
                'ref', 'dslf_fa13', 'hbond_lr_bb', 'hbond_bb_sc', 'hbond_sc',
                'fa_intra_rep', 'fa_intra_sol_xover4', 'yhh_planarity', 'Peptide', 'modification'] #from Alford JCTC 2017 fig 8b
df = df[energy_terms]


wtdf = df[df['modification'] == 'unmodified'].drop(columns=['Peptide', 'modification']).mean()
ppdf = df[df['modification'] == 'phosphorylated'].drop(columns=['Peptide', 'modification']).mean()

ddg_wt = wtdf - ppdf
ddg_wt.sort_values(inplace=True)
ddg_wt = ddg_wt[ddg_wt.abs() > 1 ] #only terms with > +/-1 kcal/mol diff

sns.barplot(ddg_wt.index, ddg_wt.values, facecolor='#4CACBC', edgecolor='k')
sns.despine()
plt.axhline(y=0, color='k')
plt.xticks(rotation=45, ha='right', rotation_mode="anchor")
plt.ylabel('ΔEnergy (kcal/mol) ')
plt.tight_layout()
plt.savefig('6_MGAPwt_ddg.png', dpi=300)

