import binascii
import sys

#def function to convert string to integer
def convert(stringname):
    value1 = (stringname.encode('utf-8').hex())
    value2 = int(value1,16)
    return (value2)

####get user to enter password
print ("")
print ("this program will now de-crypt the contents of a text file using a the same password as was used to encrypt")
print ("")
print ("")
print ("***WARNING - ENTERING THE WRONG PASSWORD COULD RENDER DATA PERMINENTLY INACCESSIBLE***")
print ("")
print ("")
print ("enter the password to decrypt the file contents and press enter        ")
print("")
key = input()

#check if password is minimum 12 charactors
length_key = len(str(key))

#check if password is minimum 12 charactors, max 24
while length_key not in range(12, 24):
    if length_key <12:
        print("")
        print("user key to short, must be at least 12 charactors")
        print("")
        print ("enter a password to encrypt file contents - must be a minimum of 12 charactors and then press enter ***YOU WILL NEED THE SAME PASSWORD TO DECRYPT THE FILE***    ")
        print("")
        key = (input())
        length_key = len(str(key))
        if length_key in range(12, 24):
            break

    elif length_key > 24:
        print("")
        print("user password to long, must be no longer than 24 charactors")
        print("")
        print ("enter a password to encrypt file contents - must be a minimum of 12 charactors and then press enter ***YOU WILL NEED THE SAME PASSWORD TO DECRYPT THE FILE***    ")
        print("")
        key = input()
        length_key = len(str(key))
        if length_key in range(12, 24):
            break

    else:
        continue

print ("")
print ("")

##get user to provide file path to target text file
print ("drag and drop file to be decrypted         " )
print ("")
file_path = input()


#chek if file path is valid
from pathlib import Path
file_name = Path(file_path)
if file_name.is_file():
    print ("")
    print ("")
    print("decrypting data now")
    print ("")
    print ("")
else:
    print ("")
    print("File doesn't exit, exiting now - check the filepath is correct")
    print ("example filepath: C:\\users\\admin\\desktop\\secret.txt")
    input ("")
    sys.exit(888)


with open(file_path) as p:
    cyphered = p.read()  # read CT from file


####check to see if key_int is even number of digits
key_int_length = len(str(key))
remainder1 = key_int_length % 2


###### if key length isn't even append a charactor based on the bellow logic to make even length#####

mixer = key[-6:-5]   #read sixth charactor from end of key as variable mixer
mixer_int = convert(mixer)


if remainder1 is 1:
    key_int_length = key_int_length + 1
    split_value = key_int_length // 2


    if mixer_int in range(1, 16):
        key_padded = key + key[-2:-1]
    elif mixer_int in range(16, 31):
        key_padded = key + key[-3:-2]
    elif mixer_int in range(31, 46):
        key_padded = key + key[-4:-3]
    elif mixer_int in range(46, 61):
        key_padded = key + key[-5:-4]
    elif mixer_int in range(61, 76):
        key_padded = key + key[-6:-5]
    elif mixer_int in range(76, 91):
        key_padded = key + key[-7:-6]
    elif mixer_int in range(91, 106):
        key_padded = key + key[-8:-7]
    elif mixer_int in range(106, 121):
        key_padded = key + key[-9:-8]
    elif mixer_int in range(121, 151):
        key_padded = key + key[-10:-9]



else:
    split_value = key_int_length // 2
    key_padded = key # no need to add charactors as even number already



#####cut user supplied password in half and create first 2 keys values
key_str_first_half = key_padded[(split_value):]

key_str_second_half = key_padded[:(split_value)]


###create third key
key_str_third = (key[::-1]) #invert key string


####convert everything to integars so we can do maths ##########

k1 = convert(key_str_first_half)
k1 = k1**2
#convert second half of key to integars
k2 = convert(key_str_second_half)
k2 = k2 **2
#convert 3rd key key to integars
k3 = convert(key_str_third)
k3 = k3 **2

#####convert CT to inegers so we can do maths
ct3 = int(cyphered) # convert cyphered string to int


##### maths to revert CT to PT integer values
ct2 = ct3 // k3
ct1 = ct2 // k2


######invert integars by converting to string, invert, then back to integers
ct1_string = str(ct1)
ct1_string2 = (ct1_string[::-1]) #invert string
ct1_string2 = int(ct1_string2)


ct1 = ct1_string2

pt  = ct1 // k1

##convert plain_text_int back to hex
plain_text_hex = hex(pt)

plain_text_hex = plain_text_hex[2:]  # remove leading 0x so binascii.unhexify doesn't error on 0x as unvalid hex


###convert back into ascii
plain_text = binascii.unhexlify(plain_text_hex)
plain_text = str(plain_text)

### clean up
plain_text_clean = plain_text[2:-1] # remove leading b' and trailing '
plain_text_clean2 = plain_text_clean

print ("decrypted data shown bellow:")
print (plain_text_clean2)

print ("")
print ("")
print ("Do you wish to output text to file? press 1 for YES, press 2 for NO *** this cannot be reversed, if above decrypted data is not readable select no (2) ***")
print ("")
output5 = (input (""))


if output5 in ["1"]:
    ###output to file
    output = str(plain_text_clean2)  # convert to string (can't write integars to file)
    f = open(file_path, "w+")  # example file creation
    f.write(output)
    f.close()  # close file
    print("")
    print("")
    print("finished :) have a nice day")
    print("")
    print("")
    input("")
    sys.exit(111)


elif output5 in ["2"]:
    print ("")
    print("exiting now, no data written to file")
    input("")
    sys.exit(777)



#check for valid input i.e 1 or 2
while output5 not in range(1, 2):
    print ("")
    print("Do you wish to output text to file? press 1 for YES, press 2 for NO *** this cannot be reversed, if above decrypted data is not readable select no (2) ***")
    print ("")
    output5 = input("")

    if output5 in ["1"]:
        ###output to file
        output = str(plain_text_clean2)  # convert to string (can't write integars to file)
        f = open(file_path, "w+")  # example file creation
        f.write(output)
        f.close()  # close file
        print("")
        print("")
        print("finished :) have a nice day")
        print("")
        print("")
        input("")
        sys.exit(111)

    elif output5 in ["2"]:
        print("")
        print("exiting now, no data written to file")
        input("")
        sys.exit(777)


