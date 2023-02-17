# Script to find all dirs containing get_top10.py and run get_top10.py
​
#!/bin/bash
​
dirlist=`find . -name get_top10.py -print0 | xargs -0 -n1 dirname | sort --unique`
​
for a in $dirlist
do
    echo $a
    cd $a
    python3 get_top10.py
    cd top_10
    ~/rosetta_bin_mac_2020.08.61146_bundle/main/source/bin/InterfaceAnalyzer.macosclangrelease -s *.pdb -out:suffix _ianal
    cd ../../
done
