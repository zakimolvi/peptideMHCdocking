"""
Compare rosetta scores for whole model and interface of C0701 vs C0702 bound peptide. 
Annotate with paired t-test statistic.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statannot import add_stat_annotation
import numpy as np
from scipy.stats import mannwhitneyu, normaltest


c7_pal = sns.color_palette(["#cab6d7", "#b5d3b4"])
sns.set(palette=c7_pal, style='ticks', context='notebook')

fp_df = pd.read_csv('flexpep_scores.csv')
ia_df = pd.read_csv('interface_scores.csv')

box_pairs = [
(("pMYO9B", "C0701"), ("pMYO9B", "C0702")),
(("pNCOR", "C0701"), ("pNCOR", "C0702")),
(("pWNK", "C0701"), ("pWNK", "C0702")),
(("pZNF518A", "C0701"), ("pZNF518A", "C0702")),
]

## plot total complex rosetta score
order = ['pMYO9B', 'pNCOR', 'pWNK', 'pZNF518A']

ax = sns.stripplot(x='peptide', y='total_score', hue='HLA', data=fp_df, dodge=True, linewidth=1, order=order)
add_stat_annotation(
    ax, data=fp_df, x='peptide', y='total_score', hue='HLA',
    box_pairs=box_pairs,
    test='t-test_paired', text_format='star',
    loc='outside', verbose=2, order=order)
sns.despine()
plt.ylabel('Rosetta score (REU)')
plt.xlabel('phosphopeptide')
plt.legend(bbox_to_anchor=(1, 0.5), title='HLA', loc='center left')
plt.tight_layout()
plt.savefig('2_flexpepscores.png', dpi=300)

plt.close()

## plot dSASA_int
ax = sns.stripplot(x='peptide', y='dSASA_int', hue='HLA', data=ia_df, dodge=True, linewidth=1, order=order)
add_stat_annotation(
    ax, data=ia_df, x='peptide', y='dSASA_int', hue='HLA',
    box_pairs=box_pairs,
    test='t-test_paired', text_format='star',
    loc='outside', verbose=2, order=order)
sns.despine()

plt.ylabel(r'Interfacial SASA ($\AA$$^{2}$)')
plt.xlabel('phosphopeptide')
plt.legend(bbox_to_anchor=(1, 0.5), title='HLA', loc='center left')
plt.tight_layout()
plt.savefig('2_SASAint.png', dpi=300)
