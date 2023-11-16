import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc
ball mall hall wall tall
'''

sentence = 'Start a sentence and then bring it to an end ball mall hall wall tall'

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.edu
bob.Samples@example.co.uk
example@example.org
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''

pattern = re.compile(r'\d{3}')
search = pattern.search(text_to_search)
print(search)

# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)
#     print(match.start(), match.end(), match.span(), match.group())
#     print(match.group(1))






