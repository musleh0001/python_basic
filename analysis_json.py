import time
import requests
import json

# https://formulae.brew.sh/api/formula/a2pss.json
response = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = response.json() 

results = []

start = time.perf_counter()
for package in packages_json: 
    package_name = package['name']
    package_desc = package['desc']
    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    res = requests.get(package_url)
    package_json = res.json()

    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    data = {
            "name": package_name,
            "desc": package_desc,
            "analytics": {
                "30d": installs_30,
                "90d": installs_90,
                "365d": installs_365
                }
        }

    results.append(data)
    # time.sleep(res.elapsed.total_seconds())
    print(f"Got {package_name} in {res.elapsed.total_seconds()} seconds")
end = time.perf_counter()
print(f"Finished in {end - start} seconds")

with open("package_info.json", "w") as f:
    json.dump(results, f, indent=2)
