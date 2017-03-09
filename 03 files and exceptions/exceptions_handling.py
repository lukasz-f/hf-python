try:
	#your code which might cause a runtime error
except:
	#your error-recovery code

#Handle all exceptions and do nothing
try:
	#your code which might cause a runtime error
except:
	pass

#Handle only ValueError
try:
	#your code which might cause a runtime error
except ValueError:
	print('ValueError occure')
