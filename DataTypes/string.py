#string
my_name = ''' Hello Jayaram
How 
r u ? '''
print (my_name);

sample_str = 'programizarefrtersrefr';
print(sample_str[3])
##get -1 compile

print ('---- -1 -------')

print(sample_str[-1])

print ('#slicing 2nd to 5th character')

print(sample_str[2:5])

print ('#slicing negative  2nd to 5th character')

print(sample_str[-3:-1])

# del my_name
# print(my_name)
print ('---- -------')
print(my_name *3)
print ('---- -------')
print ('Letter Count')

count=0
for letters in sample_str:
  if(letters =='r'):
    count += 1

print('count is = ', count)    
print ('---- -------')
print ('check true in operator')

check = 'a' in 'jayaram';

print (check)
print ('---- -------')
print ('upper lower split ')
print ('---- -------')
str1 = 'PrOgRaMiZ'
str2 = 'jaya ram ven kata naray anan'

print(str1.upper())

print (str2.lower())

print(str2.split())
print ('---- -------')
print ('replace ')
str3 = 'jayaram venkatanarayanan'
str4 = str3.replace('venkatanarayanan','V')
print(str4)
print ('---- -------')
print ('find ')
str5 = str3.find('am')
print(str5)

print ('----Len -------')
str6 = 'jayaram venkatanarayanan'
print(len(str6))
print ('---- string List enumerate()-------')
str_enm = enumerate(str6)
print(str_enm)
str_enmList = list(enumerate(str6))
print(str_enmList)

print('checking string')

sample_str = 'programizarefrtersrefr';
count=0
for letters in sample_str:
  if(letters =='r'):
    count += 1

print('count is = '+ str(count) + 'totally') 
print ('---- string List enumerate()-------')
#format
name ='Jayaram'
age = 31

print(f'hello {name} you r {age}')

#[start:stop:stepover]
print('[start:stop:stepover]')
print('-----------------------')
my_str = '1234567890'

print(my_str[0:8:2])
print(my_str[::2])

print('nedative', my_str[::-2])
print('-----------------------')