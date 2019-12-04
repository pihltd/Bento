#!/usr/bin/env python

#import graphene
import argparse
import pprint
import requests
import icdcQueries as icdc
#import json

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


def main(args):
    tier = { "stage" : "https://caninecommons-stage.cancer.gov/v1/graphql/",
    "qa" : "https://caninecommons-qa.cancer.gov/v1/graphql/",
    "dev" : "https://caninecommons-dev.cancer.gov/v1/graphql/"}

    schemaquery = """
    {
      __schema{
        types{
          name
        }
      }
    }
    """


    casequery = """
      {
        __type(name:"CaseDetail"){
          name
          fields{
            name
            description
            type{
              name
              kind
            }
          }
        }
      }
    """
    if args.verbose:
        pprint.pprint(args.tier)
        pprint.pprint(tier[args.tier])
    icdc.init()
    if args.verbose:
        pprint.pprint(icdc.sbg_single_case)
    data = runQuery(tier[args.tier], icdc.sbg_single_case)
    #data = runQuery(tier[args.tier], schemaquery)
    pprint.pprint(data)
    #parseSchema(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action = "store_true", help = "Enable verbose errors")
    tiers = ["stage", "qa", "dev"]
    parser.add_argument("-t", "--tier", required = True, type = str.lower, choices = tiers, help = "Allowed values stage, qa, dev")

    args = parser.parse_args()
    main(args)
