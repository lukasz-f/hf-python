str = 'asdf:fdsa:asdf'


str.split(':') 				#['asdf', 'fdsa', 'asdf']
(a, b) = str.split(':', 1) 	#['asdf', 'fdsa:asdf']

#Locate substring in another string
str.find(':') #4
str.find('!') #-1
