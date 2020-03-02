import urllib.request
import json

url = "http://dummy.restapiexample.com/api/v1/employees"
urllib.request .urlopen(url)
print(urllib.request .__version__)
response = urllib.request .urlopen(url)
data = json.loads(response.read())

print(data)