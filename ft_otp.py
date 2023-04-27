# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tvillare <tvillare@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/20 18:01:34 by tvillare          #+#    #+#              #
#    Updated: 2023/04/27 16:50:12 by tvillare         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import re
import hashlib


re_hexa = re.compile("^[0-9a-fA-F]+$")

def leer_fichero(file):
	archivo = open(file, "r")
	# Lee el contenido del archivo usando read()
	contenido = archivo.read()
	archivo.close()
	return contenido

def create_key(file):
	hexa = leer_fichero(file)
	if (len(hexa) < 64) and (re_hexa.match(hexa)):
		print("./ft_otp: error: key must be 64 hexadecimal characters.")
		return
	hash_object = hashlib.sha1(hexa.encode())
	# Convertimos el valor hash a una cadena hexadecimal
	hex_dig = hash_object.hexdigest()


