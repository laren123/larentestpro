import random
import argparse, string;
# Password Generator


# Get passwords function
def getPasswords(characters, length, passwords):
	# Initialize passwords
	_passwords = '';

	# Loop
	for i in range(passwords):
		# Create the password (join random characters)
		password = ''.join(random.choice(characters) for i in range(length));

		# Check if not i == passwords - 1 (last password)
		if not (i == passwords - 1):
			# Insert enter
			_passwords += password + '\n';
		# If i == passwords - 1
		else:
			# Don't insert enter
			_passwords += password;

	# Return all the passwords
	return _passwords;
if __name__ == '__main__':
    pp=''
    fi=int(1)
    if fi==1:
        le=int(input('len:'))
        no=int(input('no:'))
        u=int(input('U:'))
        uu='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l=int(input('L:'))
        ll='abcdefghijklmnopqrstuvwxyz'
        n=int(input('N:'))
        nn='0123456789'
        s=int(input('S:'))
        ss='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        cc=''
        file=str(input('Enter the name:'))
        txt='.txt'
        name=str(file+txt)
        pp=open(name,'w+')
        if u==1:
            cc=cc+uu
        if l==1:
            cc=cc+ll
        if n==1:
            cc=cc+nn
        if s==1:
            cc=cc+ss
        # Print all the passwords
        pas=getPasswords(cc,le,no)
        pp.write(pas)
        pp.close()
        print(pas)
        
