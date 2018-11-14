zoo = ('python', 'elephant', 'penguin')
print('Ilość zwierząt w zoo = %s' % len(zoo))
new_zoo = ('monkey', 'camel', zoo)
print(new_zoo)
print('razem %s miejsca' % len(new_zoo))
print('Zwierzeta nabyte ze starego zoo: ')
print(new_zoo[2])
print('Ostatnie zwierzę ze starego zoo to %s: ' % new_zoo[2][2])
print("Ilość zwierząt w nowym zoo: ", len(new_zoo) - 1 + len(new_zoo[2]))

print(new_zoo[1])

myempty = ()
print(myempty)
