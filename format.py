def format(msg):
	msg = str(msg)
	for simbol in msg:
		if simbol == ',' or simbol == '.' or simbol ==  '!' or simbol ==  '?' or simbol ==  '[' or simbol ==  ']' or simbol ==  '{' or simbol ==  '}' or simbol ==  '\'' or simbol ==  '\"' or simbol == '(' or simbol == ')':
			msg = msg.replace(simbol, '')
	return msg

def formatInput(msg):
	msg = str(msg)
	for simbol in msg:
		if simbol == ',' or simbol == '.' or simbol ==  '!' or simbol ==  '?':
			msg = msg.replace(simbol, '')
	return msg