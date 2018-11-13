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

# LINKS:
[Graphviz - Graph Visualization Software(like UML, Roadmap)](https://www.graphviz.org/)
#### Python:
- [Otwarta Edukacja](http://python.otwartaedukacja.pl/)
- [Learnpub](https://leanpub.com/pyprog/read)
- [Konwersja daty](https://pypi.org/project/convertdate/)


#### Python and Selenium
[Selenium with Python: short instruction YouTube](https://www.youtube.com/watch?v=FFDDN1C1MEQ)

-
-
-


c.d.
https://leanpub.com/pyprog/read#leanpub-auto-klasy
Przetwarzanie niewielkich ilości danych