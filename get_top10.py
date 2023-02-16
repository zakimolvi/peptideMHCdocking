import pandas as pd
import os
import subprocess
import shutil
​
# get score file (some are named score.sc others score_docked.sc)
parent_path = os.listdir()
score_file = None
​
for file in parent_path:
    if file.startswith("score"):
        score_file = file
​
while score_file == None:
    break
​
os.mkdir("top_10")
​
df = pd.read_csv(score_file, delim_whitespace=True, skiprows=1)
df = df.sort_values(by='total_score', ascending=True).iloc[0:10]
df.to_csv('top_10/top10.csv')
top10_models = [x+'.pdb' for x in df['description']]
​
for fmodel in top10_models:
    shutil.copy(fmodel,"top_10/"+fmodel)
