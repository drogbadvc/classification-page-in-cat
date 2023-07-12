import http.client

conn = http.client.HTTPSConnection("www.machinools.com")

payload = "{\n    \"url_input\": [\"https://cartable-et-pyjama.fr/blog/comment-faire-garder-ses-enfants-lete-sans-trop-depenser/\"],\n    \"option\": \"Title\",\n    \"word_list\": [\"santé\", \"parent\", \"enfant\", \"politique\", \"mariage\", \"Immobilier\", \"cuisine\", \"vacances\"]\n}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/api/classification/classify", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
