# import re
# hit = ['Kashmir', 'kashmirsrinagar', 'pulwama', 'jammu kashmir', 'pakistan',
#        'encounter', 'terrorist', 'attack', 'freedom', 'lockdown', 'anantnag', 'shopian', 'kulgam', 'sopore', '#kashmir']
# eg = 'kashmir'
# pattern = re.compile(eg, re.IGNORECASE)
# matches = [x for x in hit if pattern.search(x)]

# print(matches)

from urllib.parse import urlencode

payload = {'q': '#administrator', 'password': 'xyz'}
result = urlencode('#administrator')
print(result)
