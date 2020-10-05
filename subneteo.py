import ips

#se encarga de ordenar de mayor a menor la cantidad de hosts leyendo un archivo
def ordena(source_location):
    with open(source_location, 'r') as f:

        l = []
        for line in f:
            x = line
            l.append(x.splitlines())

        g = [] 
        m = []
        for a in l:
            for i in a:
                g.append(i.split())


        for i in g:
            for n, x in enumerate(i):
                if not x.isdigit():
                    i[n] = ''
            while '' in i:
                i.remove('')

            i = list(map(int, i))
            m.append(i)

        m.pop()
        m.sort(key=lambda x: x[1:], reverse=True)
        #print(m)
        return m

#se encarga de imprimir datos ordenados en un archivo
#def imprime(target_location, listaOrdenada):
        with open(target_location, 'w') as wr:
            for ls in listaOrdenada:
                if ls[0] > 1:
                        wr.write(f'{ls[0]} redes de {ls[1]} hosts\n')
                        for i in range(ls[0]):
                            wr.write(f'{i+1} red -> \n')
                            wr.write(f'Primera IP ->  - Ultima IP ->  \n')
                            wr.write(f'Broadcast ->  \n \n')
                        wr.write('--------------------------------------------\n')
                    
                else:
                        wr.write(f'{ls[0]} red de {ls[1]} hosts\n')
                        wr.write(f'{ls[0]} red -> \n')
                        wr.write(f'Primera IP ->  - Ultima IP ->  \n')
                        wr.write(f'Broadcast ->  \n \n')
                        wr.write('--------------------------------------------\n')


#procesa todas las acciones necesarias para un resultado satisfactorio
def procesa(source_location, target_location, red_base):
    listaOrdenada = ordena(source_location)
    ips.calcula_ips(red_base, listaOrdenada, target_location)
    #imprime(target_location, listaOrdenada)

#acciones
procesa('source.txt', 'target.txt', '192.0.0.0/2')








