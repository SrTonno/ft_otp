import hmac, base64, struct, hashlib, time
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
	while len(x)!=6:
		x+='0'
	return x
#base64 encoded key
secret = '0e7a4426850cd939288145e9048203ed8f81fb09'
print(get_totp_token(secret))
