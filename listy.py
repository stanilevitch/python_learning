shoplist = ['jablka', 'mango', 'marchewka', 'banany']
print(shoplist)
print('Mam %s rzeczy do kupienia. \nSą to: ' % len(shoplist))
for item in shoplist:
    print(f"- {item}")
    # print(item, end=' ')
print("Dla koleżanki muszę jeszce kupić ryż")
shoplist.append('rice')
print("Pełna lista zakupów to obecnie: \nSą to: %s" % shoplist)
print("Posortowana lista: ")
shoplist.sort()
print(shoplist)
print("Usuwamy pierwszy element bo nie potrzebujemy: ")
firstitem = shoplist[0]
print(firstitem)
del shoplist[0]
print("Zapamiętam, że nie kupiłem: %s" % firstitem)
print("Ostateczna lista zakupów: %s" % shoplist)
for item in shoplist:
    print(f"- {item}")
shoplist.remove('rice')
print(shoplist)