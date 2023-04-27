# ft_otp
Este proyecto consiste en la implementación de OTP en python que permita registrar una clave inicial y generar una nueva contraseña cada vez que se solicite.

## Uso
El programa se ejecuta desde la línea de comandos y cuenta con las siguientes opciones:

## Generar clave

> ./ft_otp -g [ruta_archivo_clave_hexadecimal+64]

Genera un archivo cifrado que contiene la clave de cifrado. La ruta del archivo debe ser especificada en el argumento.

## Generar contraseña temporal

> ./ft_otp -k [ruta_archivo_clave .key]

Genera una nueva contraseña temporal y la muestra en la salida estándar. La ruta del archivo que contiene la clave de cifrado debe ser especificada en el argumento.

## Requisitos
- Se debe especificar una clave hexadecimal de al menos 64 caracteres para generar la contraseña temporal.
- El archivo que contiene la clave de cifrado se cifrará en todo momento.
- El programa hará uso de alguna librería o función que permita acceder al tiempo del sistema.

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
