# back-end-iskra

Aquest servidor opera al port 4000 utilitzant el protocol TCP/IP.

Esta preparat per llegir 20B de cada request i espera números de 9 dígits o menys.

Si rep un numero nou el guardarà en una llista i en un fitxer de log.

Si rep un numero de menys de 9 dígits afegirà els 0 que facin falta per tenir un numero de 9 dígits.

Si rep la paraula terminate de qualsevol client el servidor tancarà els socket i es pararà.

Mentre el server esta en funcionament cada 10 segons mostrarà una llista amb tots els números guardats.



## Per executar el programa des de la línia de comandes

```python3 iskra_server.py```
