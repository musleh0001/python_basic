""" JavaScript Object Natation """
import json
from urllib.request import urlopen

people_string = """ 
{
    "people": [
        {
            "name": "John Smith",
            "phone": "652-255-4521",
            "emails": ["johnsmith@gmail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "789-255-3545",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

# data = json.loads(people_string)

# for person in data["people"]:
#     del person["phone"]

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)

# Example
# with open("states.json", "r") as f:
#     data = json.load(f)

# for state in data["states"]:
#     del state["area_codes"]

# with open("new_states.json", "w") as f:
#     json.dump(data, f, indent=4)

# api example
with urlopen(
    "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
) as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data["list"]["resources"]:
    name = item["resource"]["fields"]["name"]
    price = item["resource"]["fields"]["price"]
    usd_rates[name] = price

print(50 * float(usd_rates["USD/INR"]))
