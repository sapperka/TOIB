# Отчет по заданию "Идентификация и аутентификация"

## Выполнение

```bash
# Создали пользователя super-{Rybakov_VA} и наделили его привилегиями суперпользователя.
rybakovva@Rybakov:~$ sudo useradd super-{Rybakov_VA}
useradd: пользователь «super-{Rybakov_VA}» уже существует
rybakovva@Rybakov:~$ sudo passwd super-{Rybakov_VA}
Новый пароль: 
Повторите ввод нового пароля: 
passwd: пароль успешно обновлён
rybakovva@Rybakov:~$ sudo usermod -aG sudo super-{Rybakov_VA}

# Создали группу group-{BBMO-02-23}.
rybakovva@Rybakov:~$ sudo groupadd group-{BBMO-02-23}

# Добавили пользователя super-{Rybakov_VA} в группу group-{BBMO-02-23}.
root@EgorovY:~# usermod -aG group-{BBMO-02-23} super-{Rybakov_VA}

# Проверили наличие пользователя в группе.
root@EgorovY:~# groups super-{Rybakov_VA}

# Создали пользователя user-{Rybakov_VA} и добавили его в группу group-{BBMO-02-23}.
root@EgorovY:~# useradd user-{Rybakov_VA}
root@EgorovY:~# usermod -aG group-{BBMO-02-23} user-{Rybakov_VA}

# Наделили полномочиями пользователя user-{Rybakov_VA} по созданию и удалению файлов в домашнем каталоге пользователя super-{Rybakov_VA} с использованием механизма разграничения доступа chmod.
root@EgorovY:~# chmod 770 /home/super-{Rybakov_VA}
root@EgorovY:~# chown super-{Rybakov_VA}:group-{BBMO-02-23} /home/super-{Rybakov_VA}

# Продемонстрировали работу механизмов разграничения доступа.
$ su user-{Rybakov_VA}
$ touch /home/super-{Rybakov_VA}/test_file.txt
$ rm /home/super-{Rybakov_VA}/test_file.txt

```

[ Окно программы Oracle VM VirtualBox ]

![image](https://github.com/sapperka/TOIB/assets/114921945/6325b15d-cb97-4a2f-8a3f-cda7cc046f95)

[ Терминал ]

![image](https://github.com/sapperka/TOIB/assets/114921945/7edbc868-4e19-47a8-b45d-61d1f90151a3)
![image](https://github.com/sapperka/TOIB/assets/114921945/0fd7285d-63f8-4f7a-92ef-d3db1953df9b)

## Вернуться в начало

[ТОИБ][def]

[def]: https://github.com/sapperka/TOIB

