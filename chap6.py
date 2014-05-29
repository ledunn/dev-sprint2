# Enter your answers for chapter 6 here
# Name: Lauren Dunn


# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

print middle('')

#middle() doesn't work with two letter, one, or no letter strings.

def is_palindrome(word):
	if len(word)<2:
		return "False"

	if first(word)!= last(word):
		print 'False'

	else: print'True'

	return is_palindrome(word[-1])


print is_palindrome('racecar')


# Ex 6.8:

def is_power(a,b):
	if a%b and (a%b)%b
		print "Yes"
		else: print "No"	

print is_power(2,4)

