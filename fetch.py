import sys

import requests
import json


## create json files from ctid argument

for ctid in sys.argv[1]:
    res=requests.get("https://credentialengineregistry.org/resources/{}".format(ctid))
    json_val=res.json()
    file_name=f"{ctid}.json"
    with open ("staging/"+file_name,'w') as outfile:
        json.dump(json_val,outfile)
