# SubnetCalculator
  * Este es un script para automatizar mi tarea de CCNA. Realiza el subneteo de cierto request, lo ordena de mayor a menor y lo formatea a mi gusto.

  Toma como base el siguiente template: 
  
  source:
  6 red de 8373 hosts
  3 redes de 999 hosts
  2 redes de 333 hosts
  4 redes de 256 hosts
  8 redes de 74 hosts
  1 redes de 35 hosts
  4 redes de 3 hosts
  4 redes de 3 hosts
  
  target:
  6 redes de 8373 hosts
  1 Red -> 10.0.0.0/18 Mascara -> 255.255.192.0
  Rango:
  Primera IP -> 10.0.0.1 -  Ultima IP -> 10.0.63.254
  Broadcast -> 10.0.63.255
  2 Red -> 10.0.64.0/18 Mascara -> 255.255.192.0
  Rango:
  Primera IP -> 10.0.64.1 -  Ultima IP -> 10.0.127.254
  Broadcast -> 10.0.127.255
  ...
