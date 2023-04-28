# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 18:01:34 by tvillare          #+#    #+#              #
#    Updated: 2023/04/28 17:14:05 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re
import hashlib
import argparse
import os
import hmac
import base64
import struct
import time
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description='')

parser.add_argument('-g',
					type=str,
					#action='store_true',
					dest='g',
					help="pide fichero hexadecimal y debuelbe .key")

parser.add_argument('-k',
					type=str,
					#action='store_true',
					dest='k',
					help="pide un .key y retorna una clave de tiempo")

args = parser.parse_args()

re_hexa = re.compile("^[0-9a-fA-F]+$")




def cifrado_fernet(message):
	# Generar una clave secreta aleatoria
	key = Fernet.generate_key()

	# Crear un objeto Fernet con la clave secreta
	cipher_suite = Fernet(key)

	# Cifrar un mensaje
	cipher_text = cipher_suite.encrypt(message.encode())
	return cipher_text



def decoder_fernet(message):
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	plain_text = cipher_suite.decrypt(message)
	return plain_text



####crear id de tiempo
def get_hotp_token(secret, intervals_no):
	key = bytes.fromhex(secret)
	# Decodificar la clave secreta en una cadena de bytes
	msg = struct.pack(">8B", *(intervals_no).to_bytes(8, byteorder='big'))
	# Empaquetar el mensaje como una cadena de 8 bytes
	h = hmac.new(key, msg, hashlib.sha1).digest()
	o = o = h[19] & 15
	# Generar un hash usando ambos. El algoritmo de hash es HMAC
	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
	#unpacking
	return h

def get_totp_token(secret):
	#ensuring to give the same otp for 30 seconds
	x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
	#adding 0 in the beginning till OTP has 6 digits
	return x.zfill(6)
######crear .key



def leer_fichero(file):
	if os.access(file, os.R_OK):
		archivo = open(file, "r")
		# Lee el contenido del archivo usando read()
		contenido = archivo.read()
		archivo.close()
	else:
		print("Error file")
		sys.exit()
	return contenido

def create_file_key(file, contenido):
	## ESCIRBIR EN EL FICHERO
	name = file.split(".")[0] + ".key"
	with open(name, "wb") as archivo:
		archivo.write(contenido)
		archivo.close()

def create_key(file):
	hexa = leer_fichero(file)
	if (len(hexa) < 64) and (re_hexa.match(hexa)):
		print("./ft_otp: error: key must be 64 hexadecimal characters.")
		return
	#hash_object = hashlib.sha1(hexa.encode())
	# Convertimos el valor hash a una cadena hexadecimal
	#hex_dig = hash_object.hexdigest()
	hex_dig = cifrado_fernet(hexa)
	create_file_key(file, hex_dig)




if (args.g != None):
	create_key(args.g)
elif (args.k != None):
	secret = leer_fichero(args.k)
	plain_text = decoder_fernet(secret)
	key = get_totp_token(secret)
	print(key)
