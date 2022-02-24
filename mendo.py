import requests
import json
import os
from os import path

from create_user import createUser
from dump_user import dumpUser
from misc import header

def individualProblem():
	id = input('Enter Problem ID (found in URL): ')
	t = input('Enter Number of Test Cases: ')

	if path.exists('testcases') == False:
		os.mkdir('testcases')

	test_path = 'testcases/' + id

	if path.exists(test_path) == False:
		os.mkdir(test_path)

	for i in range(1, int(t) + 1):
		with requests.Session() as s:
			user, password = createUser()
			s.post('https://mendo.mk/Login.do', data={'username': user, 'password': password})
			dumpUser('users.json', user, password)
			
			url = 'https://mendo.mk/User_TestCaseDownload.do?id=' + id + '&testcase=' + str(i)
			r = s.get(url, stream=True)
			print('Test Case ' + str(i) + ': Done')
			open(test_path + '/TEST_' + id + '_' + str(i) + '.zip', 'wb').write(r.content)

def createUsers():
	len = int(input('Enter the amount of users you want to create(I recommend a smaller amount than 100): '))
	for i in range(len):
		user, password = createUser()
		dumpUser('users.json', user, password)

	print('Done!')

def main():
	header()
	print('1. Individual Problem\n2. Create users only')

	choice = int(input('Enter choice: '))

	if choice == 1:
		individualProblem()
	elif choice == 2:
		createUsers()
	else:
		print('Invalid option selected!')
		input('...')
		return 0

if __name__ == '__main__':
	main()
