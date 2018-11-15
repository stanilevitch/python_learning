# python_learning
exercises
##### The 'if' statement, along with 'else' and 'elif'

mark-github
```
if {conditions}:
    {run this code}
elif {conditions}:
    {run this code}
elif {conditions}:
    {run this code}
else:
    {run this code}
```

#### Selenium Python Beginner Tutorial - Learn Selenium Python in one video | Step by Step

---

```python
from datetime import time  

from selenium import webdriver  

driver = webdriver.Chrome("C:\Users\Marcin\PycharmProjects\FirstSeleniumTest\drivers\chromedriver.exe")
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(10)

driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
time.sleep(5)

driver.quit()
```

Funkcja f1 będąca metodą obiektu obiekt1 może zostać wywołana po zapisaniu: 
`obiekt1.f1()`

`'123'.replace('2','a')`

```python
sortowanie w kolejności:
b=[3,2,4,6,7,1,9]
b.sort()
b
[1, 2, 3, 4, 6, 7, 9]
```
⋅⋅⋅
> Oznaczenie `%s` w napisie wskazuje miejsce, w które należy wstawić wartość. 
> Po znaku `%` podaje się wstawiane wartości.
> Like: `print('%s x %s = %s' % (a,b,a*b))`

⋅⋅⋅
```python
komentarze:
# -*- coding: utf-8 -*-
```
Przed łańcuchem musimy podać literkę `u` (od unicode). 
```python
print(u'Powierzchnia prostokąta = %s' % area)
```

|  Struktura  | Identyfikator | Przykład	                                | Typowe użycie                                                               |
| ------------|:-------------:|:-------------------------------------------:|:---------------------------------------------------------------------------:|
| lista	      | list	      | Liczby = [1,4,6,3]                          | Operacje na listach danych (sortowanie, łączenie i dzielenie, modyfikacje)  |
| krotka	  | tuple	      | Czerwień = (255, 0, 0)	                    | Rekord bazy danych, parametr. Krotek nie można modyfikować!                 |
| słownik	  | dict	      | Numery = {‘raz’: 1, ‘dwa’: 2, ‘trzy’: 3}    | Dostęp do danych poprzez nazwę.                                             |     
| zbiór	      | set	          | set([‘Gniezno’, ‘Kraków’, ‘Warszawa’])	    | Sprawdzenie czy jest w zbiorze                                              |

### Listy

`Lista` służy do przechowywania uporządkowanej kolekcji obiektów (danych).

dodanie: `append`

sortowanie: `sort`

usuwanie: `del` =>>> `del shoplist[0]` usuwa pierwszy element z listy

`remove =>>> shoplist.remove('rice')`

`len()` określająca długość listy.


```python
print(item, end=' ')
```

### Krotki
Krotki są używane do przechowywania razem kilku obiektów. Są one podobne do list, ale pozbawione części funkcjonalności (nie można ich modyfikować). Krotki są definiowane poprzez umieszczenie elementów rozdzielonych przecinkami w nawiasach okrągłych () - podczas gdy listy określa się nawiasami kwadratowymi.
Krotki są zwykle stosowane w przypadkach, gdy chcemy uniknąć możliwości zmieniania danych. Na przykład dane odczytane z bazy danych powinny być używane w niezmienionej formie.

```python
`Każde dwa elementy rozdzielone przecinkiem (lub jedna zakończona przecinkiem) są traktowane jak krotka.
1   a=1,
2   krotka=1,a,3
3   print(krotka)
```
`singleton = (2, )` -krotka jednoelementowa (Bez przecinka (2) będzie traktowane jak liczba (możesz sprawdzić drukując `(2).__class__.` )
```python
(2,).__class__
<class 'tuple'>
(2).__class__
<class 'int'>
```

### Słowniki
Słownik można przyrównać do książki adresowej, gdzie można znaleźć adres lub dane teleadresowe osoby, znając tylko jego / jej imię i nazwisko. 
Słownik kojarzy klucze (nazwy) z wartościami (szczegóły).
Stąd używana czasem nazwa ‘tablice asocjacyjne’ (od asocjacja = skojarzenie).

```python
f = {1:'ddd'}
f
{1: 'ddd'}
f.__class__
<class 'dict'>
f = {1:'ddd'}.items()
f
dict_items([(1, 'ddd')])
f.__class__
<class 'dict_items'>
```
```python
ab = {key:value}
------
ab = {
    'name' : 'name@email.com'
    }
# Usuwanie pary z listy
del ab['name']
# Dodawanie i zamiana elementów do słownika
ab[Guido] = guido@python.org
 że jeśli nie ma danych dla klucza ‘Guido’ zostanie dodany do słownika element z takim kluczem. Jeśli już w słowniku jest – nastąpi zmiana adresu.
# Sprawdzenie czy element o danym kluczu jest na liście:
if 'Guido' in ab:
    print("Adres Guido to: %s" % ab['Guido'])

```
 ```python
przeglądanie elementów słownika z wykorzystaniem metody items(). Zwraca ona po kolei pary klucz, wartość – jako elementy krotki.
---
for name, address in ab.items():
    print("Adres {} to {}".format(name, address))
```
### Zbiory
nieuporządkowana kolekcja prostych obiektów. Są one stosowane, gdy ważne jest tylko istnienie obiektu w kolekcji, lub ilość wystąpień. Można je kojarzyć ze zbiorami w matematyce. Mamy podobne operacje: sprawdzenie członkostwa, podzbiory, przecięcia itd….

```python
# WEJŚCIE:
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

# WYJŚCIE:
True
**********
BRI =
{'brazil', 'russia', 'india'}
**********
BRIc =
{'brazil', 'russia', 'india', 'china'}
**********
BRI podzbiorem BRIc?
True
**********
{'brazil', 'russia', 'india', 'china'}
++++++++++
{'brazil', 'india'}
==========
^^^^^^^^^^
{'brazil', 'russia', 'india', 'china'}
##########

```
### WHILE, FOR, IF
 Pętla `while` różni się od pętli `for` przede wszystkim tym, że nie musimy mieć w chwili jej rozpoczęcia informacji o zbiorze danych jaki będzie przetwarzany. 
 Warunkiem powtarzania pętli może być dowolne wyrażenie logiczne (tak zwany niezmiennik pętli).

#### Instrukcja warunkowa (if)
Instrukcja `if` służy do zaznaczenia bloku instrukcji, który się wykona wyłącznie wtedy, gdy prawdziwe będzie wyrażeni logiczne sprawdzane przed wejściem do tego bloku. 
Jeśli warunek jest spełniony, wykonywany jest blok instrukcji (możemy go określić jako “blok warunkowy”). w przeciwnym wypadku możemy wskazać inny blok instrukcji do wykonania. Służy do tego słowo kluczowe `else`. Użycie `else` jest opcjonalne. 






> MATERIALS: c.d.n
> https://leanpub.com/pyprog/read#leanpub-auto-klasy
> http://users.uj.edu.pl/~ufkapano/algorytmy/lekcja07/with.html
> https://pythonprogramming.net/reading-csv-files-python-3/
> https://pl.python.org/docs/tut/node5.html
> 
> book:
> pyprog.pdf
> Slatkin B.
> 







# LINKS:
[Graphviz - Graph Visualization Software(like UML, Roadmap)](https://www.graphviz.org/)
#### Python:
- [Otwarta Edukacja](http://python.otwartaedukacja.pl/)
- [Learnpub](https://leanpub.com/pyprog/read)
- [Konwersja daty](https://pypi.org/project/convertdate/)


#### Python and Selenium
[Selenium with Python: short instruction YouTube](https://www.youtube.com/watch?v=FFDDN1C1MEQ)
