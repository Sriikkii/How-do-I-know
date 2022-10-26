import argparse
import pickle
import csv
import os
import pandas as pd
import pyperclip
try :
    import cryptography
except:
    os.system('pip install cryptography')
    import cryptography

import os
try :
    import pwinput
except:
    os.system('pip install pwinput')


from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)



def view():
    df = pd.read_csv("passwords.txt",sep='|')
    #print(df)
    #ch = input("you want to know your password ? pls enter y to continue ").lower()
    x = input("enter the Username you want to check ")
    y = df[df['username']== x ]
    print(y)
    j = input(" do you like the password to be in  clipboard (Y/N) ").upper()
    if j == 'Y':
        o = int(input("enter the index number "))
        u = df._get_value( o , 'Passwords')
        pyperclip.copy(u)
        print("Copied to your clipboard")
        d = input("you wish to decode the password (Y/N) ? ").lower()
        if d == 'y' :
            B = fer.decrypt(u.encode()).decode()
            pyperclip.copy(B)
            print("copied to your clipboard")
        else:
            pass
    else:
        pass
    h = input("Do you wish to see the full table ? (Y/N) ").upper()

    if h  == 'Y':
        for i in range(1):
            q = pwinput.pwinput("enter the secondary master pswd ") 
            t = open("decryp",'r')
            r = t.read()
            t.close()
            if q == r :
                print(df)
            else:
                print("Incorrect password")
    
    """
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.encrypt(passw.encode()).decode())"""
def view2(): 
    print("Note only clipboard option is only available for encrypted passwords")

    df = pd.read_csv("pswd.txt",sep='|')
    #print(df)
    #ch = input("you want to know your password ? pls enter y to continue ").lower()
    
    h = input("Do you wish to see the Contents  ? (Y/N) ").upper()

    if h == 'Y':
        for i in range(1):
            q = pwinput.pwinput(prompt="enter the secondary master pswd ",mask="*") 
            g = pwinput.pwinput(prompt="enter the master pswd ",mask="*")
            v = open("h.txt",'r')
            w = v.read()
            if g == w :
                t = open("decryp",'r')
                r = t.read()
                t.close()
                if q == r :
                    y = input("You wish to see the full contents (Y/N) ? or specific username (S) ?  ").lower()
                    if y == 'y':
                        print(df)
                    elif y == 's':
                        b = input("enter the Username you want to check ")
                        a = df[df['username']== b ]
                        print(a)
                else:
                    print("Incorrect password")
                    break
            else:
                print("Incorrect Master password")
        else:
            pass
    
                    
                    
    """  
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            f.write("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())"""
                     


def add():
    name = input('Account Name: ')
    pwd = pwinput.pwinput(prompt='Password  ', mask='*')
    with open("pswd.txt",'a') as h:
        h.write(name + "|" + pwd + "\n")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



def en_de():
    k = input('enter the key')
    ch = input("Do you want to encrypt your message or decrypt your message ?(E/D)").upper()
    if ch == 'E' :
        fer = Fernet(k)
        M = input("enter your decrypted message ")
        K = fer.encrypt(M.encode()).decode()
        j = input(" would you like to save this in a file (Y/N)").upper()
        if j == 'Y':
            f_name = input("enter the file name")
            choice = input("Choice of 1 for TEXT FILE  2 for CSV file 3 for BINARY FILE ")
            if choice == '1':
                F = f_name + '.txt'
                f = open(F,'w')
                f.write(M + "|" + K+ "\n")
                f.close()
                pass
            elif choice == '2' :
                L = f_name + '.csv'
                l = open(L,'w')
                sw = csv.writer(l,delimiter='|',lineterminator='\n')
                sw.writerow(['Decrypted','Encrypted'])
                t = [M,K]
                sw.writerow(t)
                l.close()
                pass
            else:
                p = []
                b = f_name + '.dat'
                s = open(b,'wb')
                p.append([M,K])
                pickle.dump(p,s)
                pass
        else:
            print(K)

    else:
        fer = Fernet(k)
        G = input("enter your Encrypted message to Decrypt")
        V = fer.decrypt(G.encode()).decode()
        o = input(" would you like to save this in a file (Y/N)").upper()
        if o == 'Y':
            e_name = input("enter the file name")
            choice = input("Choice of 1 for TEXT FILE  2 for CSV file 3 for BINARY FILE")
            if choice == '1':
                u = e_name + '.txt'
                y = open(u,'w')
                y.write(G + "|" + V+ "\n")
                y.close()
            elif choice == '2' :
                i = e_name + '.csv'
                I = open(i,'w')
                sw = csv.writer(I,delimiter='|',lineterminator='\n')
                sw.writerow(['Decrypted','Encrypted'])
                d = [G,V]
                sw.writerow(d)
                I.close()
            else:
                g = []
                B = e_name + '.dat'
                S = open(B,'wb')
                g.append([G,V])
                pickle.dump(g,S)
        else:
            print(V)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('option', help='add / view / Encrypt & Decrypt')
    parser.add_argument("add", help = "add your password and username")
    parser.add_argument("view", help = "view your data")
    parser.add_argument("view2", help = "view your data in decrypted form")
    parser.add_argument("ed",help = "encode or decode your message")

    args = parser.parse_args()
    print(args.add)
    print(args.view)
    print(args.view2)
    print(args.ed)

    if args.option == "add":
        add()
    elif args.option == "view":
        view()
    elif args.option == "view2":
        view2()
    elif args.option == "ed":
        en_de()




while True:
    j = open("h.txt",'r')
    o = j.read()
    j.close()
    Master_Pswd = pwinput.pwinput(prompt='Master pswd ' , mask='*')
    if Master_Pswd == o :
        print('Good To Go ')
        
    else:   
        break

    mode = input(
        "Would you like to add a new password or view existing ones (view, add), Encrypt or Decrypt your data (ed), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        ch = input("Would You like to see the encoded or decoded pswd ? for encrypted pswd enter 'E' or for dercrypted pswd enter 'D'").upper()
        if ch == 'E':
            view()
        else:
            l = open("decryp",'r')
            d = l.read()
            l.close()
            f = pwinput.pwinput(prompt='decryp pswd ', mask='*')
            if f == d :
                view2()
                continue
            else:
                print('Incorrect password')
                break
    elif mode == "add":
        add()
    elif mode == 'ed':
        en_de()
    else:
        print("Invalid mode.")
        continue





















"""alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
 
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye") """