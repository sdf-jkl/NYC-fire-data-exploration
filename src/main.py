from sodapy import Socrata
import requests
from requests.auth import HTTPBasicAuth
import json
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Fire')
parser.add_argument('--page_size', type=int, help='how many rows to get per page', required=True)
parser.add_argument('--num_pages', type=int, help='how many pages to get in total', default = 1)
args = parser.parse_args(sys.argv[1:])
print(args)

#DATASET_ID="8m42-w767"
#INDEX_NAME='fire'

DATASET_ID=os.environ["DATASET_ID"]
APP_TOKEN=os.environ["APP_TOKEN"]
ES_HOST=os.environ["ES_HOST"]
ES_USERNAME=os.environ["ES_USERNAME"]
ES_PASSWORD=os.environ["ES_PASSWORD"]
INDEX_NAME=os.environ["INDEX_NAME"]


if __name__ == '__main__': 

    try:
        resp = requests.put(f"{ES_HOST}/{INDEX_NAME}", auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD),
                json={
                    "settings": {
                        "number_of_shards": 1,
                        "number_of_replicas": 1
                    },
                    "mappings": {
                        "properties": {
                            "starfire_incident_id": {"type": "keyword"},
                            "incident_datetime": {"type": "date"},
                            "incident_borough": {"type": "keyword"},
                            "incident_classification": {"type": "keyword"},
                            "dispatch_response_seconds_qy": {"type": "keyword"},
                            "incident_response_seconds_qy": {"type": "keyword"},
                            "engines_assigned_quantity": {"type": "keyword"},
                        }
                    },
                }
            )
        resp.raise_for_status()
        print(resp.json())
        
    except Exception as e:
        print("Index already exists! Skipping")    

    client = Socrata("data.cityofnewyork.us", APP_TOKEN, timeout=10000)
    for page in range(args.num_pages):
        offset = page * args.page_size
        rows = client.get(DATASET_ID, limit=args.page_size, offset=offset)
        
        es_rows = []
    
        for row in rows:
            try:
                es_row = {
                    "starfire_incident_id": row["starfire_incident_id"],
                    "incident_datetime": row["incident_datetime"],
                    "incident_borough": row["incident_borough"],
                    "incident_classification": row["incident_classification"],
                    "dispatch_response_seconds_qy": row["dispatch_response_seconds_qy"],
                    "incident_response_seconds_qy": row["incident_response_seconds_qy"],
                    "engines_assigned_quantity": row['engines_assigned_quantity'],
                }
    
            except Exception as e:
                print(f"Error!: {e}, skipping row: {row}")
                continue
    
            es_rows.append(es_row)
    
        bulk_upload_data = ""
        for line in es_rows:
            action = '{"index": {"_index": "' + INDEX_NAME + '", "_id": "' + line["starfire_incident_id"] + '"}}'
            data = json.dumps(line)
            bulk_upload_data += f"{action}\n"
            bulk_upload_data += f"{data}\n"
        print('rows uploaded ',len(es_rows))
        try:
            resp = requests.post(f"{ES_HOST}/_bulk",
                data=bulk_upload_data, auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD), headers={"Content-Type": "application/x-ndjson"})
            resp.raise_for_status()
            print(f'Uploaded page {page+1} to Elasticsearch')
    
        except Exception as e:
            print(f"Failed to insert in ES: {e}")
