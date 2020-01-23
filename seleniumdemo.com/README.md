# seleniumdemo.com

### Wprowadzenie
Repozytorium zawiera przypadki testowe, testy automatyczne napisane w języku programowania Python przy użyciu Selenium oraz raport wygenerowany przy użyciu Allure  dotyczący strony [seleniumdemo.com](http://seleniumdemo.com "seleniumdemo.com").

### Struktura
Repozytorium zawiera foldery:
- locators;
- pages;
- reports; #todo
- tests;
- test cases. #todo

### Opis
##### Locators
Folder zawiera lokatory używane w testach automatycznych. Lokatory pogrupowane są w klasy. Każda klasa dotyczy konkretnego obszaru podlegającego testom. Utworzona jest również klasa "Generic" zawierająca lokatory powtarzające się w różnych obszarach.
##### Pages
Folder zawiera metody związane z różnymi funkcjami na stronie. Wszystkie metody opisane są przy pomocy nazwy (allure.step) oraz logów. Większość metod zapisuje zrzut ekranu z wykonywanych czynności.
##### Reports
Folder zawiera raport z testów utworzony przy pomocy Allure.
##### Tests
Folder zawiera klasy z testami automatycznymi. Wszystkie testy zawierają tytuł (allure.title) oraz opis (allure.description).
##### Test cases
Folder zawiera przypadki testowe, do których utworzone są testy automatyczne.
