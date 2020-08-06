import json
import random

with open('snli_1.0_test.jsonl', 'r') as f:
    batch = set()
    for line in f.readlines():
        batch.add(json.loads(line)['sentence1'])

selected_txt = random.choices(list(batch), k=50)
premises = []
num = 1
for sen in selected_txt:
    premises.append({"model": "server.Premise",
                    "pk": num,
                    "fields": {
                        "text": sen
                    }})
    num += 1

with open('premise.json', 'w') as pf:
    json.dump(premises, pf)