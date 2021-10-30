import re

t="""int foo()
    {
}"""

print(t);

#print( re.sub(r')\n    {',')\n    {\n    xxxx',t,re.M) );

r = re.search(r'cat|dog', 'The cat is here')
print(r)

r = re.findall(r'...at', 'The cat in the hat went splat')
print(r)

r = re.findall(r'^\d','1 is a number')
print(r)

r = re.findall(r'\d$','the number is 2')
print(r)