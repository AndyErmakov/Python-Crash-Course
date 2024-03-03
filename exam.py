from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
for i in range(26):
    for j in range (26):
        find_me = chr(97+i)+chr(97+j)
        secret_password = find_me + 'bcmpda'
        x = unzip_with_7z(zip_file_path, dest_path, secret_password)
        if x is True:
            print("You are lucky!")
            print('the password is:', secret_password)
            break
    if x is True:
        break

