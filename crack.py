#!/usr/bin/python
import os,sys
import crypt
import codecs
from datetime import datetime,timedelta
import argparse 
today = datetime.today()
os.system('clear')

def testPass(cryptPass,user):
	dicFile = open ('dict.txt','r')
	ctype = cryptPass.split("$")[1]
	found = False
	time = time = str(datetime.today() - today)
	if ctype == '6': 
		print "[*] Hash Type is SHA-12... "
		salt = cryptPass.split ("$")[2]
		insalt= "$" + ctype + "$" + salt + "$"
		for word in dicFile.readlines():
			word= word.strip('\n')
			cryptWord = crypt.crypt(word,insalt)
			if( cryptWord == cryptPass):
				found= True
				
				print "[+]Found password for the user: " + user + " =====> " + word + " (Time: " + time+ ")\n"
			
			
	if ( found == False): 
		print "[-]Password not found in dictionary."  + " (Time: " + time+ ")\n"

	print "_______________________________________________________________________"
			
			
exit	

def main(): 
	userInput = argparse.ArgumentParser(description='Linux Password Cracker')
   	userInput.add_argument('-f', action='store', dest='path', help='Path to shadow file, example: \'/etc/shadow\'')
   	shadPath=userInput.parse_args()
   	if shadPath.path == None:
		userInput.print_help()
        
   	else:
		passFile = open (shadPath.path,'r')
         	for line in passFile.readlines():
			line = line.replace("\n","").split(":")
           	  	if  not line[1] in [ 'x', '*','!' ]:
          	 		user = line[0]
           	  		cryptPass = line[1]
				print "[*] Cracking Password For: " + user
           	  		testPass(cryptPass,user)
if __name__ == "__main__" :
	main()
	
