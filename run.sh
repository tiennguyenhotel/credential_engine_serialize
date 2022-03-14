#!/bin/bash
if [ ! -d env ]; then
	python3 -m venv myenv
fi

source myenv/bin/activate
pip3 install -r requirements.txt


## start the code 
source ctid.sh

./fetch.py $CTID

