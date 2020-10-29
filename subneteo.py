import ips

# se encarga de ordenar de mayor a menor la cantidad de hosts leyendo un archivo


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
        # print(m)
        return m


# procesa todas las acciones necesarias para un resultado satisfactorio
def procesa(source_location, target_location, red_base):
    listaOrdenada = ordena(source_location)
    ips.calcula_ips(red_base, listaOrdenada, target_location)
    #imprime(target_location, listaOrdenada)


# acciones
procesa('source.txt', 'target.txt', '10.0.0.0/8')
