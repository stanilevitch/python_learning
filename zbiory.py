bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
print('*'*10)
bric = bri.copy()
bric.add('china')
print('BRI =')
print(bri)
print('*'*10)
print('BRIc =')
print(bric)
print('*'*10)
print('BRI podzbiorem BRIc?')
print(bric.issuperset(bri))
print('*'*10)
bri.remove('russia')
print(bric)
print('+'*10)
print(bri & bric)
print('='*10)
bric.intersection(bri)
print('^'*10)
print(bric)
print('#'*10)