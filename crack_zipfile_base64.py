import zipfile
import base64
from tqdm import tqdm

# the password list path you want to use, must be available in the current directory
wordlist = "WORD_LIST_HERE"
# the zip file you want to crack its password
zip_file = "ZIP_NAME_HERE"

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=base64.b64encode(word.strip()))
        except:
            continue                                                                                                                                                                                                                       
        else:                                                                                                                                                                                                                              
            print("[+] Password found:", word.decode().strip())                                                                                                                                                                            
            print("[+] Password found b64:", base64.b64encode(word.strip()))                                                                                                                                                               
            exit(0)                                                                                                                                                                                                                        
print("[!] Password not found, try other wordlist.")
