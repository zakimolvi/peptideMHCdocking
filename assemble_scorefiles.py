""""
Walk subdirs, concatenate score files into DF, annotate

"""
import pandas as pd
import os
path = './' 
fp = []
ia = []
pdb_hla_dict = {'5VGE-K66N-S99Y':'C0701', '5VGE':'C0702'}

for root, dirs, files in os.walk(path):
	#watch out bc this walks the parent dir too
	for file in files:
		if (file.endswith(".sc") and file.__contains__("ianal")):
			ia.append(os.path.join(root,file))
		elif(file.endswith(".csv") and file.startswith("top")):
			fp.append(os.path.join(root,file))

fp_df = pd.read_csv(fp[0])
ia_df = pd.read_csv(ia[0], delim_whitespace=True, skiprows=1)

print(fp)
print(ia)

for ndf in fp[1:]:
	ndf = pd.read_csv(ndf)
	fp_df = fp_df.append(ndf)

for odf in ia[1:]:
	odf = pd.read_csv(odf, delim_whitespace=True, skiprows=1)
	ia_df = ia_df.append(odf)

def format_df(dframe):
	dframe['model'] = [x.split('_')[0]+'_'+x.split('_')[1] for x in dframe['description']]
	dframe['peptide'] = [x.split('_')[1] for x in dframe['description']]

	dframe['HLA'] = [x.split('_')[0] for x in dframe['description']]
	dframe['HLA'] = dframe['HLA'].map(pdb_hla_dict)

	return dframe

fp_df = format_df(fp_df)
ia_df = format_df(ia_df)

fp_df.to_csv('flexpep_scores.csv')
ia_df.to_csv('interface_scores.csv')
