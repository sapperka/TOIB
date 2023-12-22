# Отчет по заданию "Настройка протокола GRE"

## Исходные данные
Топология сети:

![image](https://github.com/sapperka/TOIB/assets/114921945/007fc27c-0755-4ac0-af42-7f0247febb02)

Таблица адресации:

![image](https://github.com/sapperka/TOIB/assets/114921945/c3b224e2-c9ad-4f83-8cbc-1ac28054e094)

## Часть 1. Проверка связи между маршрутизаторами

<strong>Шаг 1. Настройте интерфейс туннеля 0 на маршрутизаторе RA.</strong>

a. Используйте команду show ip interface brief на маршрутизаторе RA , чтобы определить IP-адрес порта S0/0/0.

![image](https://github.com/sapperka/TOIB/assets/114921945/4c763d40-9295-4d34-87bc-9b77bf7a1993)

b. Отправьте с маршрутизатора RB эхо-запрос на IP-адрес интерфейса S0/0/0 маршрутизатора RA.

![image](https://github.com/sapperka/TOIB/assets/114921945/c2ee4e16-4763-48ee-ab12-6383b0ba4a4b)

<strong>Шаг 2. Отправьте эхо-запрос с компьютера ПК B на компьютер ПК A.</strong>

![image](https://github.com/sapperka/TOIB/assets/114921945/18d0547b-d447-41a9-8b3e-5ea532f968ce)

## Часть 2. Настройка туннелей GRE

<strong>Шаг 1. Настройте интерфейс туннеля 0 на маршрутизаторе RA.</strong>

a. Войдите в режим настройки туннеля 0 на маршрутизаторе RA.

![image](https://github.com/sapperka/TOIB/assets/114921945/890671c1-b5fb-410c-99ff-5cebd4639577)

b. Настройте IP-адрес согласно таблице адресации.

![image](https://github.com/sapperka/TOIB/assets/114921945/17ef040e-dcfc-458c-aed6-ec3653fe2c68)

c. Настройте источник и назначение для конечных точек туннеля 0.

![image](https://github.com/sapperka/TOIB/assets/114921945/dc4d8397-36ae-41d9-af83-477514bab36c)

d. Настройте туннель 0 для передачи трафика IP по GRE.

![image](https://github.com/sapperka/TOIB/assets/114921945/de17d52d-7c12-479c-8b95-4346d5b5a396)

<strong>Шаг 2. Настройте интерфейс туннеля 0 на маршрутизаторе RB.</strong>

a. Войдите в режим настройки туннеля 0 на маршрутизаторе RB.

![image](https://github.com/sapperka/TOIB/assets/114921945/e5b87b1c-2772-444a-ae3f-caaabd966e90)

b. Настройте IP-адрес согласно таблице адресации.

![image](https://github.com/sapperka/TOIB/assets/114921945/a3c20609-6573-451d-8a19-01770c43f813)

c. Настройте источник и назначение для конечных точек туннеля 0.

![image](https://github.com/sapperka/TOIB/assets/114921945/86554b59-f3e3-4b64-bd94-e8ddc43bfbab)

d. Настройте туннель 0 для передачи трафика IP по GRE.

![image](https://github.com/sapperka/TOIB/assets/114921945/73f9298d-bc9b-431c-8d02-b7739e772e61)

<strong>Шаг 3. Настройте маршрут для частного трафика IP.</strong>

![image](https://github.com/sapperka/TOIB/assets/114921945/c213f8e6-b20e-420d-9847-ec52cd72c8b6)

![image](https://github.com/sapperka/TOIB/assets/114921945/f82bdaa9-19a9-45fc-a250-cacca0777d2b)

## Часть 3. Проверка связи между компьютерами

<strong>Шаг 1. Отправьте на ПК A эхо-запрос от ПК B.</strong>

![image](https://github.com/sapperka/TOIB/assets/114921945/62d68f41-fe4b-43e7-8dc6-062eb9e40489)

<strong>Шаг 2. Сделайте трассировку от ПК A до ПК B.</strong>

![image](https://github.com/sapperka/TOIB/assets/114921945/3eb1223c-0a05-461b-8571-0f71f75697e7)

## Проверка правильности выполнения задания:

![image](https://github.com/sapperka/TOIB/assets/114921945/3f065f1e-48bb-4991-9725-31223ea1700f)

## Вернуться в начало

[ТОИБ][def]

[def]: https://github.com/sapperka/TOIB

