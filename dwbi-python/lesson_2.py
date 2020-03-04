import urllib.request
import json

url = "http://dummy.restapiexample.com/api/v1/employees"
urllib.request .urlopen(url)
print(urllib.request .__version__)
response = urllib.request .urlopen(url)
json_data = json.loads(response.read())

print(json_data)

#parsed_json = (json.loads(json_data))
#print(json.dumps(parsed_json, indent=4, sort_keys=True))

with open("data_file.json", "w") as write_file:
    json.dump(json_data, write_file)

print(json_data['data'])

data = json_data['data']
print(data)

person_json = json.dumps(data)
print(person_json)


my_list = []
for p in data:
   my_list.append(int(p['employee_salary']))
my_list.sort(reverse=True)
print(my_list)

