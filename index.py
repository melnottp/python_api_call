# -*- coding:utf-8 -*-
import json
import requests

def handler (event, context):
    Endpoint = "eu-west-0.prod-cloud-ocb.orange-business.com"     
    Project = context.getProjectID()              
    print("Authentication and Getting token")
    token = context.getToken()
     
    
    print("Hibernate CCE latest cluster")
    url = f"https://cce.{Endpoint}/api/v3/projects/{Project}/clusters/YOUR_CLUSTER_ID/operation/awake"
    payload={}
    headers = {
    'Content-Type': 'application/json',
    'X-Auth-Token': token,
    'X-Cluster-UUID': 'YOUR_CLUSTER_ID'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(event),
        "headers": {
            "Content-Type": "application/json"
        }
    }
