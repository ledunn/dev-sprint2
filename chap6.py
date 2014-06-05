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
		pass

	elif len(word)==3 and first(middle(word))== last(middle(word)):
		return True
	if first(word)== last(word):
		return is_palindrome(middle(word))
	else:
		return False	
				

x=is_palindrome('racecar')
print x

#Ex 6.8:

def gcd(a,b):
	gcd(a,b)=gcd(b,r)
	gcd(a,0)=a	

