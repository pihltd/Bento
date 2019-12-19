#!/usr/bin/env python

import json
from pandas.io.json import json_normalize
import pprint

jsonfile = "icdc-full-response.json"
flatfile = "flatJSON.txt"

def flattenJSON(jsondata):
    flatdata = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a,name + str(i) +'_')
                i += 1
        else:
            flatdata[name[:-1]] = x

    flatten(jsondata)
    return flatdata


def main():
    #Read in the json file
    with open(jsonfile) as f:
        jsondata = json.load(f)
    f.close()

    #Flatten the json
    flatdata = flattenJSON(jsondata)
    json_normalize(flatdata)

    pprint.pprint(flatdata)

    #g = open(flatfile, "w")
    #g.write(flatdata)
    #g.close()

    #with open(flatfile) as g:
    #    json.dump(flatdata,g)
    #g.close()

main()
