# ft_otp
Este programa en Python permite registrar una clave inicial y generar contraseñas temporales utilizando el algoritmo Time-Based One-Time Password (TOTP).

## Uso
El programa puede ser utilizado con dos opciones:

### -g (generar)
Utiliza la opción -g para guardar una clave hexadecimal en un archivo cifrado. La clave debe tener al menos 64 caracteres.

> python ft_otp.py -g \<fichero_clave>

### -k (clave)

Utiliza la opción -k para generar una contraseña temporal basada en la clave almacenada en el archivo cifrado.

> python ft_otp.py -k \<archivo_cifrado>


## Ejemplo de uso
```
$ echo -n "NEVER GONNA GIVE YOU UP" > key.txt
$ ./ft_otp -g key.txt
./ft_otp: error: key must be 64 hexadecimal characters.
$ xxd -p key.txt > key.hex
$ cat key.hex | wc -c
64
$ ./ft_otp -g key.hex
Key was successfully saved in ft_otp.key.
$ ./ft_otp -k ft_otp.key
836492
$ sleep 60
$ ./ft_otp -k ft_otp.key
123518
```
## Dependencias
- sys
- re
- hashlib
- argparse
- os
- hmac
- base64
- struct
- time
