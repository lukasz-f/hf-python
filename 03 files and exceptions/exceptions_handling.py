try:
    # your code which might cause a runtime error
    pass
except:
    # your error-recovery code
    pass

# Handle all exceptions and do nothing
try:
    # your code which might cause a runtime error
    pass
except:
    pass

# Handle only ValueError
try:
    # your code which might cause a runtime error
    pass
except ValueError:
    print('ValueError occurs')

# Handle with exception object
try:
    # your code which might cause a runtime error
    pass
except ValueError as err:
    print('ValueError occurs: ' + str(err))

# Handle exception if occur and always run finally code
try:
    # your code which might cause a runtime error
    pass
except IOError:
    # your code when exception occurs
    pass
finally:
    # your code that always run
    pass
