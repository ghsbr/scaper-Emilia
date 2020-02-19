import requests
import json
src = requests.get('https://apps.arpae.it/REST/qa_stazioni?where={%22per_mappa%22:true}&projection={%22foto%22:0}')

with open("data.json", "w") as f:
  f.write(json.dumps(json.loads(src.text),indent = 2))