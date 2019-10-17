import json
people_string = '''
{
	"people": [
		{
			"name" : "John Smith",
			"phone" : "615-555-7164",
			"emails" : ["johnsmith@gmail.com", "johnsmith@workplace.com"],
			"has_license" : false
		},
		{
			"name" : "Jane Doe",
			"phone" : "560-555-5153",
			"emails" : null,
			"has_license" : true
		}
	]
}
'''
#how to convert json string into python object
data = json.loads(people_string) 
print(data['people'])

for person in data['people']:
	print(person['name'])
	del person['phone']

people_string_2 = json.dumps(data)
for person in data['people']:
	print(person)









