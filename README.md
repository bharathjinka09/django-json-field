# To access the api data
## Endpoint : http://127.0.0.1:8000/
```json.map(dog => dog['fields']['data']['pets']['dogs'])```

```
import requests

response = requests.get('http://127.0.0.1:8000/')

contacts = response.json()

for contact in contacts:
	print(contact['fields']['data'])

```