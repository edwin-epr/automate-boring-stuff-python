# %%
import re

# %%
# Function to print with this feature of python and Zed
def write(arg: object) -> None:
    print(f'Output: {arg}')

# %%
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
if mo:
    print(f'Phone number found: {mo.group()}')
else:
    print('No phone number found.')

# %%
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
if mo:
    mo.group(1)
    mo.group(2)
    mo.group(0)
    mo.group()
# %%
areaCode: str = ''
mainNumber: str = ''
if mo:
    mo.groups()
    areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# %%
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
if mo:
    print(mo.group(1))
    print(mo.group(2))
# Matching multiple group with the pipe
# Example A
# %%
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

# Example B
# %%
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
# Optional matching with the question mark
# %%
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# %%
phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# Matching zero or more with the star
# %%
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# %%
# Matching one or more with the plus compile
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
print(f'Output: {mo1.group()}')
mo2 = batRegex.search('The adventures of Batwowowowoman')
print(f'Output: {mo2.group()}')
mo3 = batRegex.search('The adventures of Batman')
print(f'Output: {mo3 == None}')
# %%
# Matching specific repetitions with braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(f'Output: {mo1.group()}')
mo2 = haRegex.search('Ha')
print(f'Output: {mo2 == None}')
# %%
# Greedy and non-greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(f'Output: {mo1.group()}')
#
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(f'Output: {mo2.group()}')
# %%
# The findall() method
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mos = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
write(mos.group())
# If there are no groups in the regular expression
mof = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
write(mof)
# If there are groups in the regular expression
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mof = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
write(mof)

# %%
# Character classes
xmasRegex = re.compile(r'\d+\s\w+')
out = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
    swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
write(out)

# %%
# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
out = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
write(out)
# Match all the characters that are not in the character class
consonoantRegex = re.compile(r'[^aeiouAEIOU]')
out = consonoantRegex.findall('RoboCop eats baby food. BABY FOOD.')
write(out)

# %%
# The caret and doller sign characters
beginsWithHello =re.compile(r'^Hello')
out1 = beginsWithHello.search('Hello, World!')
write(out1)
out2 = beginsWithHello.search('He said hello.')
write(out2 == None)
# %%
endsWithNumber = re.compile(r'\d$')
out3 = endsWithNumber.search('Your number is 42')
write(out3)
out4 = endsWithNumber.search('Your number is forty two.')
write(out4 == None)
# %%
wholeStringIsNum = re.compile(r'^\d+$')
out5 = wholeStringIsNum.search('1234567890')
write(out5)
out6 = wholeStringIsNum.search('12345xyz67890')
write(out6 == None)
out7 = wholeStringIsNum.search('12 34567890')
write(out7 == None)

# %%
# The wild card character
atRegex = re.compile(r'.at')
out = atRegex.findall('The cat in the hat sat on the flat mate.')
write(out)

# %%
# Matching everything with the dot-star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
write(mo.group(1))
write(mo.group(2))
# %%
# Non-Greedy version
nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>')
write(mo1)
# Greedy version
greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
write(mo2)

# %%
# Matching newlines with the dot character
# No newline regular expression
noNewlineRegex = re.compile(r'.*')
out1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\
    \nUphold the law.').group()
write(out1)
# Newline regular expression
newlineRegex = re.compile(r'.*', re.DOTALL)
out2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\
    \nUphold the law.').group()
write(out2)

# %%
# Case-insensitive matching
robocop = re.compile(r'robocop', re.IGNORECASE)
out1 = robocop.search('RobocOp is part man, part machine, all cop.').group()
out2 = robocop.search('ROBOCOP protects the innocent.').group()
out3 = robocop.search('Al, why does your programming book talk about robocop so much?').group()
write(out1)
write(out2)
write(out3)
# %%
# Substituting strings with the sub() method
namesRegex = re.compile(r'Agent \w+')
out1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
write(out1)

# %%
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# agentNamesRegex.sub('\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# Lo anterior funciona, pero en Zed no lo interpreta bien, pero lo anterior se arregla como sigue:
agentNamesRegex = re.compile(r'Agent (?P<first_letter>\w)\w*')
out2 = agentNamesRegex.sub('\g<first_letter>****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
write(out2)

# %%
def replace_agent_name(match):
    return match.group(1) + "****"

agentNamesRegex = re.compile(r'Agent (\w)\w*')
out3 = agentNamesRegex.sub(replace_agent_name, 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(out2)

# %%
# Managing complex regexes
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)
out = phoneRegex.search('Loco465-235.5083  ext. 453')
out.group(4)
