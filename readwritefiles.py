import os

check_file = True
path_to_file = "/home/clara/Documents/Djangogirls/secrets.txt"

while check_file:
    file_exists = os.path.exists("/home/clara/Documents/Djangogirls/secrets.txt")
    if file_exists:
        print("secret.txt file exists")

        secret_file = open(path_to_file, 'r+')
        for line in secret_file:
            print(line)

        secret_file.write("I know your secrets, muhahahaha")
        secret_file.close()

        check_file = False
