import re
f = open("input.txt", 'r')
func = open("functions.txt",'r').read()
keywords = open("keywords.txt",'r').read()
args = open("arguments.txt",'r').read()
method = open("method.txt",'r').read()
for x in f:
	# Match operator characters
	result = re.findall("(?!\'[\\w\\s]*[\\']*[\\w\\s]*)([-=+/*^<>])(?![\\w\\s]*[\\']*[\\w\\s]*\')", x)
	if result:
		for y in result:
			x = re.sub(y,"<span class=\\\"snippet-operator\\\">"+y+"</span>",x)

	# Match Keywords
	# Fill this in with whatever keywords are used in the snippet of code
	result = re.findall(keywords,x)
	if result:
		for y in result:
			x = re.sub(y,"<span class=\\\"snippet-keyword\\\">"+y+"</span>",x)

	# Match the word 'With' because it wouldn't play nicely with the others
	result = re.findall("(?:^|\\W)(with)(?:$|\\W)",x)
	if result:
		for y in result:
			x = re.sub(y,"<span class=\\\"snippet-keyword\\\">"+y+"</span>",x)

	# Match method name
	# Fill in with whatever your method is called
	result = re.findall("",x)
	if result:
		for y in result:
			x = re.sub(y,"<span class=\\\"snippet-method\\\">"+y+"</span>",x)

	# Match arguments
	# Fill in with whatever function arguments your program has
	result = re.findall(args,x)
	if result:
		for y in result:
			x = re.sub(y,"<span class=\\\"snippet-function-argument\\\">"+y+"</span>",x)

	# Match Tabs
	x = re.sub("(\t)",r"\\t",x)

	# Match Newlines
	x = re.sub("(\n)",r"\\n",x)

	# Match Functions
	result = re.findall(func,x)
	if result:
		for y in result:
			x = re.sub(y,"<span class=\\\"snippet-function\\\">"+y+"</span>",x)

	# Match Strings
	result = re.findall("'(.+?)'",x)
	if result:
		for y in result:
			x = re.sub("'(.+?)'","<span class=\\\"snippet-string\\\">'"+y+"'</span>",x)

	out = open("output.txt","a")
	out.write(x)
	out.close()

f.close()