import json

def dumpUser(filename, user, password):
	with open('users.json','r+') as file:
		users_data = json.load(file)
		users_data.append({'username': user, 'password': password})
		file.seek(0)
		json.dump(users_data, file, indent=4)
	print('User dumped to ' + filename)