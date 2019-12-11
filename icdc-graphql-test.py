#!/usr/bin/env python

import argparse
import pprint
import requests
import icdcQueries as icdc
import yaml
import json
from pandas.io.json import json_normalize
import pandas as pd

def runQuery(url,query):
  request = requests.post(url, json={'query':query})
  if request.status_code == 200:
      return request.json()
  else:
      raise Exception ("Query failed code {}. {}".format(request.status_code,query))

def parseSchema(jsondata):
    schemafields = []
    for type in jsondata['data']['__schema']['types']:
        schemafields.append(type['name'])
    pprint.pprint(schemafields)

def caseCount(jsondata):
    #parse out the cases from an SBG query
    caselist = []
    for case in jsondata['data']['case']:
        caselist.append(case['case_id'])
    return caselist

def json2yaml(jsondata):
    yamldata = yaml.dump(jsondata)
    pprint.pprint(yamldata)

def writeYAML(jsondata, filename):
    yamlfile = open(filename, "w")
    yamlfile.write(yaml.dump(jsondata))
    yamlfile.close()

def flattenJSON(jsondata):
    #https://stackoverflow.com/questions/37706351/nested-json-to-csv-generic-approach
    #https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10?gi=4fbbb7be6da5#.y46j8vr6ghttps://medium.com/@amirziai/flattening-json-objects-in-python-f5343c794b10#.y46j8vr6g
    flatdata = {}

    def flatten(x, name=''):
    #def flatten(x):
        if type(x) is dict:
            for a in x:
                #flatten(x[a], name + a + '_')
                flatten(x[a], a)
                #flatten(x[a])
        elif type(x) is list:
            i = 0
            for a in x:
                #flatten(a, name + str(i) + '_')
                flatten(a,name)
                #flatten(a)
                i +=1
        else:
            #flatdata[name[:-1]] = x
            flatdata[name] = x
            #flatdata = x

    flatten(jsondata)
    return flatdata

def writeCSV(jsondata, filename):
    #https://stackoverflow.com/questions/56883988/conversion-from-nested-json-to-csv-with-pandas
    #flatdata = flattenJSON(jsonlist)
    #finaldata = json_normalize(flatdata)
    finaldata = pd.DataFrame(flattenJSON(case) for case in jsondata['data']['case'])
    csvfile = open(filename,"w")
    finaldata.to_csv(csvfile,encoding = 'utf-8', index = False)
    csvfile.close()

def writeJSON(jsondata, filename):
    jsonfile = open(filename, "w")
    jsonfile.write(jsondata)
    jsonfile.close()


def main(args):
    tier = { "stage" : "https://caninecommons-stage.cancer.gov/v1/graphql/",
    "qa" : "https://caninecommons-qa.cancer.gov/v1/graphql/",
    "dev" : "https://caninecommons-dev.cancer.gov/v1/graphql/",
    "prod" : "https://caninecommons.cancer.gov/v1/graphql/"}
    query = ""

    if args.veryverbose:
        pprint.pprint(args.tier)
        pprint.pprint(tier[args.tier])
    icdc.init()
    if args.qa:
        if args.tier == 'prod':
            query = idc.prod_sbg_single_case
        else:
            query = icdc.sbg_single_case
    else:
        query = icdc.sbg_all_cases
    if args.veryverbose:
        pprint.pprint(query)
    data = runQuery(tier[args.tier], query)
    if args.veryverbose:
        pprint.pprint(data)

    if args.filename is not None:
        if args.outputtype is not None:
            if args.outputtype == 'yaml':
                writeYAML(data, args.filename)
            elif args.outputtype == 'csv':
                writeCSV(data, args.filename)
            elif args.outputtype == 'json':
                writeJSON(data, args.filename)
    else:
        json2yaml(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action = "store_true", help = "Enable verbose errors")
    parser.add_argument("-vv", "--veryverbose",action = "store_true", help = "Enable insane verbosity")
    tiers = ["stage", "qa", "dev", "prod"]
    parser.add_argument("-t", "--tier", required = True, type = str.lower, choices = tiers, help = "Allowed values prod, stage, qa, dev")
    parser.add_argument("-q", "--qa", action = "store_true", help = "Use test query")
    types = ["yaml", "csv","json"]
    parser.add_argument("-o", "--outputtype", help = "Output file type, Allowed values yaml, json, csv")
    parser.add_argument("-f", "--filename", help = "Filename for output")

    args = parser.parse_args()
    main(args)
