# Import modules

import random
import getpass
import optparse
import os
import struct
import sys
import unittest
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
from tkinter import *

root = Tk()
root.title('File Locker')

def val_ex(en,infile,outfile,pa):
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
    
    ifile=infile
    ofile=str(outfile)
    key=str(pa)
    e=int(en)
   
    if e==1:
        encrypt_file(ifile, ofile, key)
    elif e==2:
        decrypt_file(ifile, ofile, key)
    return

e=Entry(root, width=50, borderwidth=5)   #Get the DIR of the input file
e.pack()
e.insert(0,"Enter the DIR of the 'FILE'")
filein=raw_input(e.get())

enno=Entry(root,width=50, borderwidth=5)  #Get the Output file name
enno.pack()
enno.insert(0,"Enter name for the output ")
fileout=str(enno.get())

pas=Entry(root, width=50, borderwidth=5)  #Get the password to Encrypt/Decrypt the input file
pas.pack()
pas.insert(0,"Enter the password")
password=str(pas.get())

a = Button(root,text='Encrypt', padx=40, pady=20, command=Lambda: val_ex(1,filein,fileout,password)) #Button for Encrypt
b = Button(root,text='Decrypt', padx=40, pady=20, command=Lambda: val_ex(2,filein,fileout,password)) #Button for Decrypt
Button_quit = Button(root, text='Quit', padx=20, pady=20, command=root.quit) #Button for exiting the program

root.mainloop()
