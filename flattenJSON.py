#!/usr/bin/env python

#https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas/notebook
#https://hackersandslackers.com/json-into-pandas-dataframes/
#https://github.com/pandas-dev/pandas/issues/26284

import json
from pandas.io.json import json_normalize
import pprint

jsonfile = "icdc-full-response.json"
#jsonfile = "icdc-SBGSingleResponse.json"
flatfile = "flatJSON.txt"

def flattenJSON(jsondata):
    flatdata = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
                #flatten(x[a],name)
        elif type(x) is list:
            i = 0
            for a in x:
                #flatten(a,name + str(i) +'_')
                flatten(a,name)
                i += 1
        else:
            flatdata[name[:-2]] = x
            #pprint.pprint(("Name: %s") % (name))
            #flatdata[name[:]] = x

    flatten(jsondata)
    return flatdata


def main():
    #Read in the json file
    with open(jsonfile) as f:
        jsondata = json.load(f)
    #f.close()

    #df = json_normalize(jsondata['data']['case'])
    #pprint.pprint(df.dtypes)
    #pprint.pprint(df.head(5))

    #cohort is not iterable

    #busted
    #df2 = json_normalize(data=jsondata['data']['case'], record_path=['cohort', 'diagnoses', 'demographic', 'samples'])


    #Working
    #df2 = json_normalize(data=jsondata['data']['case'], record_path=['samples', 'files'], meta=['case_id'])
    df2 = json_normalize(data=jsondata['data']['case'], record_path=['samples','files'], meta=['case_id'])
    #record_path is apparently for parent-child, not sibilings.
    pprint.pprint(df2.head())

    #pprint.pprint(jsondata)
    #pprint.pprint(json_normalize(jsondata))
    #pprint.pprint(json_normalize(jsondata.head()))

    #Flatten the json
    #flatdata = flattenJSON(jsondata)
    #json_normalize(flatdata)

    #pprint.pprint(flatdata)

    #g = open(flatfile, "w")
    #g.write(str(flatdata))
    #g.close()

main()
