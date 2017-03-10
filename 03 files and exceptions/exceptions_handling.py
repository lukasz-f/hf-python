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
	print('ValueError occurs')

#Handle with exception object
try:
	#your code which might cause a runtime error
except ValueError as err:
	print('ValueError occurs: ' + str(err))

#Handle exception if occur and always run finally code
try:
	#your code which might cause a runtime error
except IOError:
	#your code when exception occurs
finally:
	#your code that always run
