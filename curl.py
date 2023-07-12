import http.client

conn = http.client.HTTPSConnection("www.machinools.com")

payload = "{\n    \"text_input\": [\"Les différentes solutions pour faire garder ses enfants · La babysitter · L'assistante maternelle agréée · L'auxiliaire parentale ou nounou à domicile\"],\n    \"option\": \"Text\",\n    \"word_list\": [\"santé\", \"parent\", \"enfant\", \"politique\", \"mariage\", \"Immobilier\", \"cuisine\", \"vacances\"]\n}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/api/classification/classify", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
