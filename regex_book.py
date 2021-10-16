text = "The agent's phone number is xxxxx"
print('phone' in text)

import re
pattern = 'phone'
print(re.search(pattern, text))

match = re.search(pattern, text)

print(match.span())
print(match.start())
print(match.end())

pattern = 'xxyyy'
print(re.search(pattern, text))

text = 'my phone once, my phones twice'
matches = re.findall('phone',text)
print(matches)


for match in re.finditer('phone', text):
    print(match.span())

for match in re.finditer('phone', text):
    print(match.group())


text = "My phone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)
print(phone.group())

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)

print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))

test_phrase = 'This is a string! But it has xxxx. How can we remove it?'
clean = re.findall(r'[^!.?]+', test_phrase)
print(' '.join(clean))

text = 'Only find the hypen-words in this sentence.'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text))

text = "hello, would you like some catfish?"
texttwo = "hello, would you like some catnap?"
textthree = "hello, have you see this caterpillar?"

print(re.search(r'cat(fish|nap|erpillar)', text))
