# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON datasets into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

# Print each key-value pair in json_data
for k, v in json_data.items():
    print(k + ' : ' + str(v))

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])