# To access the api data
## Endpoint : http://127.0.0.1:8000/
```json.map(dog => dog['fields']['data']['pets']['dogs'])```

```
import requests

response = requests.get('http://127.0.0.1:8000/')

dogs = response.json()

for dog in dogs:
	print(dog)

```