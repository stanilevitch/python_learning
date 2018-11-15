# 'ab' to krótka lista adresowa
ab = {
    'Ruby': 'ruby@gmail.com',
    'Trufi': 'trufi@wp.pl',
    'Doris': 'doris@www.pl',
    'Flufi': 'flufi@google.eu'
}
print(ab)
print("Adres Rubiego to: ", ab['Ruby'])
print("Ilość kontaktów na liście: {}\n".format(len(ab)))

# Usuwanie pary z listy
del ab['Flufi']
print("Ilość kontaktów na liście: {}".format(len(ab)))

for name, address in ab.items():
    print("Adres {} to {}".format(name, address))

# dodanie pary do listy
ab['Guido'] = 'guido@ddd.eu'
print("Ilość kontaktów na liście: {}".format(len(ab)))

if 'Guido' in ab:
    print("Adres Guido to: %s" % ab['Guido'])