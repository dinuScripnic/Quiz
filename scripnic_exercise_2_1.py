def open_file():
	"""
	Opens the database(json) in read mode. No values required
	"""
	import json
	try:
		data = open('database1.json')
		database = json.load(data)
		return database
	except FileNotFoundError:
		database = {}
		# I am sure this is not the right way of doing it, but it works )))
		return database


def main(database):
	"""
	Runs all the required procedures to get to the next step.
		main(file)
		file: a json object
	"""
	# gave this loops to make the program work until user gives a right command

	while True:
		action = input('Enter R to register, L to login, D to delete: ').upper()
		# get the input about users requirement
		# added upper function in case user writes with lowercase
		# delete function is my own idea, for a more complete functionality
		if action == 'R':
			print('OK, registering a new user.')
			user_data = register_user(database)
			break
		elif action == 'L':
			print('OK, log in a registered user.')
			user_data = log_in_user(database)
			break
		elif action == 'D':
			print('Sad that you leave us :(')
			delete_user(database)
			save_file(database)
			exit()
			# force the program to close
		else:
			print('ERROR!!! INVALID COMMAND!!! Try once again!')
	return user_data


def register_user(database):
	"""
	Registers a new user, add this information to database.
		register_user(file)
		file: a json object
	"""
	# also requires the user to give inputs until the right input is achieved
	while True:
		log_in = input('Enter your E-mail address: ')
		if log_in not in database:
			# add information about new user in the database, this is the only way I could manage to do it
			database.update({log_in: {"password": password_approving(), "points": 135}})
			print(f'Congratulations, has been successfully registered.')
			break
		else:
			print('Sorry, this e-mail address already exist.\nPlease, try another one.')
	return log_in, database[log_in]


def log_in_user(database):
	"""
	Logs in a user, who is in database.
		log_in_user(file)
		file: a json object
	"""
	while True:
		log_in = input('Enter your E-mail address: ')
		if log_in in database:
			password = input('Please, enter your password: ')
			if database[log_in]['password'] == password:
				print('Log in successful')
				break
			else:
				print('Invalid password')
		else:
			print(f'{log_in} not found, try once again')
	return log_in, database[log_in]


def delete_user(database):
	"""
	Delete information about user from database.
	After processing the program closes automatically
		delete_user(file)
		file: a json object
	"""
	while True:
		log_in = input('Enter your E-mail address: ')
		if log_in in database:
			password = input('Enter your password: ')
			if database[log_in]['password'] == password:
				del database[log_in]
				# delete all information about the introduced user from the database
				print(f'User {log_in} successfully deleted')
				return database
			else:
				print('Password is incorrect, try once again!')
		else:
			print(f'Sorry, {log_in} not detected, Try once again!')


def password_approving():
	"""
	Require from user 2 passwords to register a new user.
	Use in combination with register_user(...).
	"""
	while True:
		password1 = input('Enter your password: ')
		password2 = input('Repeat your password: ')
		if password1 == password2:
			return password1
		else:
			print('Sorry, the two passwords don’t match.')


def save_file(database):
	"""
	Saves all changes in database.
		save_file(file)
		file: a json object
	"""
	import json
	data = open('database1.json', 'w')
	data.write(json.dumps(database))
	data.close()
