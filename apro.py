#!/usr/bin/env python

# Import modules
import random
import getpass
import optparse
import os
import struct
import sys
import unittest
from Crypto.Hash import MD5
from Crypto.Hash import MD2
from Crypto.Hash import MD4
from Crypto.Hash import SHA224
from Crypto.Hash import SHA256
from Crypto.Hash import SHA384
from Crypto.Hash import SHA512
from hashlib import sha256
from random import randrange

PY3 = sys.version_info[0] == 3
if PY3:
    import builtins
    print_ = getattr(builtins, 'print')
    raw_input = getattr(builtins, 'input')
    unicode_type = str
else:
    unicode_type = unicode
    def print_(s):
        sys.stdout.write(s)
        sys.stdout.write('\n')

from io import BytesIO

from Crypto.Cipher import AES
from Crypto import Random



CIPHER_AES = 2

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
def _gen_padding(file_size, block_size):
    pad_bytes = block_size - (file_size % block_size)
    padding = Random.get_random_bytes(pad_bytes - 1)
    bflag = randrange(block_size - 2, 256 - block_size)
    bflag -= bflag % block_size - pad_bytes
    return padding + chr(bflag).encode('raw_unicode_escape')

def _read_padding(buffer, block_size):
    return (buffer[-1] % block_size) or block_size

def generate_iv(block_size):
    return Random.get_random_bytes(block_size)

def get_aes_cipher(key, iv):
    if isinstance(key, unicode_type):
        key = key.encode('utf-8')

    iv_length = AES.block_size  # 16.
    key_length = 32
    key_iv_length = iv_length + key_length
    d = d_i = b''
    while len(d) < key_iv_length:
        d_i = sha256(d_i + key).digest()
        d += d_i[:16]

    new_key = d[:key_length]
    new_iv = d[key_length:key_iv_length]
    return AES.new(new_key, AES.MODE_CBC, new_iv)

CIPHER_MAP = {
    CIPHER_AES: (get_aes_cipher, AES.block_size),
}

def encrypt(in_buf, out_buf, key, chunk_size=4096,
            cipher_type=CIPHER_AES):
    get_cipher, block_size = CIPHER_MAP[cipher_type]
    iv = generate_iv(block_size)
    cipher = get_cipher(key, iv)
    bytes_read = 0
    wrote_padding = False

    out_buf.write(iv)

    while 1:
        buffer = in_buf.read(chunk_size)
        buffer_len = len(buffer)
        bytes_read += buffer_len
        if buffer:
            if buffer_len < chunk_size:
                buffer += _gen_padding(bytes_read, block_size)
                wrote_padding = True
            out_buf.write(cipher.encrypt(buffer))
        else:
            if not wrote_padding:
                padding = _gen_padding(bytes_read, block_size)
                out_buf.write(cipher.encrypt(padding))
            break

def decrypt(in_buf, out_buf, key, chunk_size=4096,
            cipher_type=CIPHER_AES):
    get_cipher, block_size = CIPHER_MAP[cipher_type]
    iv = in_buf.read(block_size)

    cipher = get_cipher(key, iv)
    decrypted = ''

    while 1:
        buffer = in_buf.read(chunk_size)
        if buffer:
            decrypted = cipher.decrypt(buffer)
            out_buf.write(decrypted)
        else:
            break

    if decrypted:
        padding = _read_padding(decrypted, block_size)
        out_buf.seek(-padding, 2)
        out_buf.truncate()

def checksum_MD5(filename,c_size):
    h = MD5.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_RIPEMD160(filename,c_size):
    h = RIPEMD160.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_BLAKE2b(filename,c_size):
    h = BLAKE2b.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()


def checksum_MD2(filename,c_size):
    h = MD2.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_MD4(filename,c_size):
    h = MD4.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_SHA1(filename,c_size):
    h = SHA1.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_SHA224(filename,c_size):
    h = SHA224.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_SHA256(filename,c_size):
    h = SHA256.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_SHA384(filename,c_size):
    h = SHA384.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def checksum_SHA512(filename,c_size):
    h = SHA512.new()
    chunk_size = c_size
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def encrypt_file(in_file, out_file, key, chunk_size=4096,
                 cipher_type=CIPHER_AES ):
    with open(in_file, 'rb') as in_fh:
        with open(out_file, 'wb') as out_fh:
            encrypt(in_fh, out_fh, key, chunk_size, cipher_type)

def decrypt_file(in_file, out_file, key, chunk_size=4096,
                 cipher_type=CIPHER_AES):
    with open(in_file, 'rb') as in_fh:
        with open(out_file, 'wb') as out_fh:
            decrypt(in_fh, out_fh, key, chunk_size, cipher_type)



    def setUp(self):
        self.in_filename = '/tmp/crypt.tmp.in'
        self.out_filename = '/tmp/crypt.tmp.out'
        self.dec_filename = '/tmp/crypt.tmp.dec'
        self.key = 'testkey'

    def tearDown(self):
        self.remove_files(
            self.in_filename,
            self.out_filename,
            self.dec_filename,
        )

    def remove_files(self, *filenames):
        for fn in filenames:
            if os.path.exists(fn):
                os.unlink(fn)

    def write_bytes(self, num, ch=b'a'):
        buf = ch * num
        with open(self.in_filename, 'wb') as fh:
            fh.write(buf)
        return buf

    def crypt_data(self, num_bytes, ch, in_key=None, out_key=None, chunk_size=4096):
        in_key = in_key or self.key
        out_key = out_key or self.key

        buf = self.write_bytes(num_bytes, ch)
        encrypt_file(self.in_filename, self.out_filename, in_key, chunk_size,
                     self.cipher_type)
        decrypt_file(self.out_filename, self.dec_filename, out_key, chunk_size,
                     self.cipher_type)

        with open(self.dec_filename, 'rb') as fh:
            decrypted = fh.read()

        return buf, decrypted


if __name__ == '__main__':
    fi=int(input('Choose:'))
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
        if u==1:
            cc=cc+uu
        if l==1:
            cc=cc+ll
        if n==1:
            cc=cc+nn
        if s==1:
            cc=cc+ss
        # Print all the passwords
        print(getPasswords(cc,le,no));
        
    elif fi==2:
        infile=raw_input('Enter the input:')
        outfile=input('Enter the out:')
        key=input('Enter the key:')
        e=int(input('1 OR 2'))
   
        if e==1:
            encrypt_file(infile, outfile, key)
        elif e==2:
            decrypt_file(infile, outfile, key)
            
    else:
        in_file=input('Enter the input:')
        chunks=8000
        print('\t Warning! \n Lesser the chunk size, more the time takes. \n Choose your chunk size according to the size of the file')
        chunks=int(input('Enter the Chunk size:'))
        choose=int(input('Hash Algorithm: \n (1) MD5 \n (2) MD2 \n (3) MD4 \n (4) SHA1 \n (5) SHA224 \n (6) SHA256 \n (7) SHA384 \n (8) SHA512 \n (9) RIPEMD160 \n (10) BLAKE2b \n Choice:'))
        if choose==1:
            print('Checksum: ',checksum_MD5(in_file,chunks))
        elif choose==2:
            print('Checksum: ',checksum_MD2(in_file,chunks))
        elif choose==3:
            print('Checksum: ',checksum_MD4(in_file,chunks))
        elif choose==4:
            print('Checksum: ',checksum_SHA1(in_file,chunks))
        elif choose==5:
            print('Checksum: ',checksum_SHA224(in_file,chunks))
        elif choose==6:
            print('Checksum: ',checksum_SHA256(in_file,chunks))
        elif choose==7:
            print('Checksum: ',checksum_SHA384(in_file,chunks))
        elif choose==8:
            print('Checksum: ',checksum_SHA512(in_file,chunks))
        elif choose==9:
            print('Checksum: ',checksum_RIPEMD160(in_file,chunks))
        elif choose==10:
            print('Checksum: ',checksum_BLAKE2b(in_file,chunks))
    

    
    
   
