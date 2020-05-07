file = open('conf', 'r')

lines = file.read().split('\n')

parsed_conf = {}

for line in lines:

    if line:

        if line[0] not in ['#', ';', ' ']:
            tmp_list = line.split()

            parsed_conf[tmp_list[0]] = tmp_list[1:]

file.close()

while True:

    request = input(">> ")

    tmp_line = request.split()

    if tmp_line[0] == 'get' and tmp_line[1] == 'param':

        if tmp_line[2] in parsed_conf.keys():

            if parsed_conf[tmp_line[2]] != '':

                print(">> {} : {}".format(tmp_line[2], ' '.join(parsed_conf[tmp_line[2]])))
            else:
                print(">> Параметр не задан")
        else:
            print(">> Параметр не найден")
    else:
        print(">> Неизвестная команда")

    print(">> Продолжить? (yes/no)")

    while True:

        answer = input(">> ")

        if answer == "yes":
            break
        elif answer == "no":
            print(">> Осуществляется выход из программы")
            quit()
        else:
            print(">> Вы ошиблись, повторите ответ (yes/no)")
