# COSC440ASGN2
Linux Password Cracker

A simple password cracker for Linux. This program takes the shadow file (/etc/shadow) as an argument and uses a dictionary file to recover the users' passwords. The shadow file is only readable by superusers to secure encrypted passwords. 

# Quick How-To 
1. Make sure that the python script (crack.py) is executable. 
2. Skip this step if python script is executable. Type in chmod +x crack.py to make it executable. 
3. Make sure that crack.py and the dictionary file (dict.txt) are in the same directory. 
4. Run it by typing: sudo python crack.py -f /etc/shadow in the command line. 
5. Sample Output: 
![ScreenShot](https://github.com/kgapulan/COSC440ASGN2/blob/master/output.png)
