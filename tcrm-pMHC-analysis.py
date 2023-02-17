"""
Use scored structures of TCRm-peptide-MHC complex to regress Rosetta energy terms against in vitro binding measured by flow cytometry using seaborn lmplot
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import palettable
pal = palettable.colorbrewer.qualitative.Pastel2_8.mpl_colors
sns.set(
    context = 'talk', style='darkgrid', inpalette= pal[3:]
)
def annotate(data, **kws):
    r, p = sp.stats.pearsonr(data['norm_MFI'], data['value'])
    ax = plt.gca()
    ax.text(.05, .8, 'r={:.2f}, p={:.2g}'.format(r, p),
            transform=ax.transAxes)

df = pd.read_csv('data.csv')
df = df[df['description'].str.contains('sep')]
df = df[~df['description'].str.contains('nohet')]

longdf = df.drop(columns=['src', 'SCORE: total_score', 'Unnamed: 0', 'description'])
longdf = longdf.melt(id_vars=['Phosphopeptide','norm_MFI'])

g = sns.lmplot(
    x = 'norm_MFI', y = 'value', col='variable', col_wrap=3, data=longdf, sharey=False
)
plt.xlabel('normalized MFI')
g.map_dataframe(annotate)

plt.tight_layout()
plt.savefig('lmplot.pdf')
