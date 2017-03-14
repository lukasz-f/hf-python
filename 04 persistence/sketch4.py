#sketch using pickle.dump
import pickle

man = []
other = []

try:
	with open('sketch.txt') as data:
		for each_line in data:
			try:
				(role, line_spoken) = each_line.split(':', 1)
				line_spoken = line_spoken.strip()
				if role == 'Man':
					man.append(line_spoken)
				elif role == 'Other Man':
					other.append(line_spoken)
			except ValueError:
				pass
except IOError:
	print('The datafile is missing!')

try:
	with open('man_data.pickle', 'wb') as man_file, open('other_data.pickle', 'wb') as other_file:
		pickle.dump(man, man_file)
		pickle.dump(other, other_file)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))
