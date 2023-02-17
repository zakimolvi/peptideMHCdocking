# peptideMHCdocking
Docking peptides of interest to MHC using a local installation of Rosetta Modeling Suite. 

## Requirements
- Local Rosetta3 installation
- Python3 along with `pandas`, `statannot`, `seaborn`, `matplotlib`, `numpy`
- `pretty_tsv`:
```
function pretty_tsv {
    column -t -s $'\t' -n "$@" | less -F -S -X -K
}
```


## Manifest
`run_flexpepdock.sh`: Initialize simulation of 200 high resolution models given a prepared PDB file.

`assemble_scorefiles.py`: Concatenate score files of multiple simulations and annotate with HLA and peptide name

`plotScores.py`: Plot scores and add t-test annotation
![](2_flexpepscores.png)

`residueAnalysis.py`: Breakdown Rosetta score by energy term and visualize each term's mean ddG between two structures.
![](6_MGAPwt_ddg.png)
