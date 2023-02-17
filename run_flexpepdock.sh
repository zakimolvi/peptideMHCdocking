#!/bin/sh
# Given an input structure of a peptide of interest threaded onto MHC, use Rosetta's FlexPepDock protocol to perform high-resolution docking.

# rosetta path
$ROSETTA3="~/rosetta_bin_mac_2020.08.61146_bundle/main/source"

#prepack input pdb and dock
$ROSETTA3/bin/FlexPepDocking.macosclangrelease -flexpep_prepack -ex1 -ex2aro -use_input_sc -out:suffix _prepacked -out:no_nstruct_label -s input.pdb
$ROSETTA3/bin/FlexPepDocking.macosclangrelease -pep_refine -nstruct 200 -ex1 -ex2aro -use_input_sc -out:suffix _docked -s input_prepacked.pdb

#view score file
pretty_tsv score.sc

# get score of top 10 models
bash run_gettop10.sh
