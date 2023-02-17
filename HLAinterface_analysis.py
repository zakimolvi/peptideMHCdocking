"""
Now we know fa_elec and fa_sol are strongest terms in ddG of MGAPwt - pMGAP,
Which residue interactions are involved?
"""
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statannot import add_stat_annotation

pairedPal = sns.color_palette(['#4CACBC', '#A0D995' ])
sns.set(palette=pairedPal, style='ticks', context='notebook')

box_pairs = [
((66, "phosphorylated"), (66, "unmodified")),
]

df = pd.read_csv('per_res_MGAPwt_pMGAP.csv') # per residue breakdown of top 10 models for each
df = df[df['pdbid2'].str.contains('4B')] #constrain to peptide interactions (chain B)
df = df[df['pdbid1'].str.contains('A')] #only peptide-HLA interactions (chain A & chain B)

order = [62, 66, 69, 70, 99, 159, 163]

df['xvals'] = [x[:-1] for x in df['pdbid1']]
df['xval_i'] = df['xvals'].astype('int')
df = df.sort_values('xval_i')
ax  = sns.stripplot(x='xval_i', y='fa_elec', hue='modification', data=df,
              dodge=True, size=8, edgecolor='k', linewidth=1.5, order = order) #66A baby!!!!!!!

add_stat_annotation(
    ax, data=df, x='xval_i', y='fa_elec', hue='modification',
    box_pairs=box_pairs,
    test='t-test_paired', text_format='star',
    loc='outside', verbose=2, order=order)

plt.xlabel('HLA-A3 residue no.')
sns.despine()
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles[0:2], ['wt', 'phospho '], title='MGAP P4Ser')
plt.ylabel('electrostatic potential (kcal/mol)')
plt.savefig('7_Ser4_interaction_fa_elec.eps', dpi=300)

plt.clf()

sns.stripplot(x='xvals', y='fa_sol', hue='modification', data=df,
              dodge=True, size=8, edgecolor='k', linewidth=1.5) #66A baby!!!!!!!
plt.xlabel('HLA-A3 residue no.')
sns.despine()
plt.legend(title='MGAP P4Ser')
plt.ylabel('solvation energy (kcal/mol)')
# plt.savefig('7_Ser4_interaction_fa_sol.png', dpi=300)
