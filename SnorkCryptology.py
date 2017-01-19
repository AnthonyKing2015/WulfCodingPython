# Programmed by: Anthony King on 1/19/2017
# This program will take any given sentence and encrypt it with 
# the snork encryption as well as decrypt it using the same method.the

print "Please enter the sentence you wish to be encrypted:  ",

sentence = raw_input()
length = len(sentence);

#This section of code will encrypt the sentence with the snork method
encrypted = sentence.replace('a', str(length));
encrypted = encrypted.replace('e', str(length+1));
encrypted = encrypted.replace('i', str(length+2));
encrypted = encrypted.replace('o', str(length+3));
encrypted = encrypted.replace('u', str(length+4));
print "The encrypted sentence is %s" % encrypted

#While this section of code will decrypt the sentence with the snork method
decrypted = encrypted.replace(str(length), 'a');
decrypted = decrypted.replace(str(length+1), 'e');
decrypted = decrypted.replace(str(length+2), 'i');
decrypted = decrypted.replace(str(length+3), 'o');
decrypted = decrypted.replace(str(length+4), 'u');
print "The decrypted sentence is %s" % decrypted
