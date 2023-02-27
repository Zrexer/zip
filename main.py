import zipfile 
from tqdm import tqdm
from os import system

system("cls")

wordlist = str(input("your worldlist : "))

zip_file = str(input("your zipfile : "))


# initialize the Zip File object
zip_file_2 = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, 'rb') as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue

        else:
            print("[+] Password found : ", word.decode().strip())
            exit(0)

print("[!] Password Not found, try the other wordlist.")

