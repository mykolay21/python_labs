import urllib.request
import json
import operator

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


my_list = []
for p in data:
   my_list.append(int(p['employee_salary']))
my_list.sort(reverse=True)
print(my_list)


my_dict = {}
for x in data:
    my_dict.update({x['employee_name']: int(x['employee_salary'])})

print(my_dict)

a = sorted(my_dict.items(), key=lambda y: y[1], reverse=True)
print(a)