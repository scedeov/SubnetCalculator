from ipaddress import ip_network

dic_mascaras = {
    2147483648: '1',
    1073741824: '2',
    536870912: '3',
    268435456: '4',
    134217728: '5',
    67108864: '6',
    33554432: '7',
    16777216: '8',
    8388608: '9',
    4194304: '10',
    2097152: '11',
    1048576: '12',
    524288: '13',
    262144: '14',
    131072: '15',
    65536: '16',
    32768: '17',
    16384: '18',
    8192: '19',
    4096: '20',
    2048: '21',
    1024: '22',
    512: '23',
    256: '24',
    128: '25',
    64: '26',
    32: '27',
    16: '28',
    8: '29',
    4: '30',
    2: '31',
    1: '32'
}


def calcula_ips(ip_base, lista_lista_hosts, target_location):
    network = ip_network(ip_base)

    hosts = [item[1] for item in lista_lista_hosts]
    num_redes = [item[0] for item in lista_lista_hosts]

    lista_mascaras = [calcula_mascara(mascara) for mascara in hosts]

    contador = 0
    with open(target_location, 'w') as wr:
        for mask in lista_mascaras:
            while True:
                rango_subneteado = list(network.subnets(
                    new_prefix=int(mask)))  # lista_mascaras
                rango_limpio = rango_subneteado[:int(
                    num_redes[contador])]  # num_base
                wr.write(f'{num_redes[contador]} redes de {hosts[contador]} hosts\n')
                #wr.write(f'{contador+1} Red -> {rango_subneteado[0]}\n')
                contador2 = 0
                contador3 = 0
                while contador2 < num_redes[contador]:
                    
                    rango_limpio = rango_subneteado[:int(num_redes[contador])]
                    for net in rango_limpio:
                        contador3 = contador3 + 1
                        wr.write(f'{contador3} Red -> {net.with_prefixlen} Mascara -> {net.netmask}\n')
                        
                        wr.write(
                            f'Rango:\nPrimera IP -> {net.network_address + 1} -  Ultima IP -> {net.broadcast_address -1}\n')
                        wr.write(f'Broadcast -> {net.broadcast_address}\n')

                        siguiente_base = net.broadcast_address + 1
                        network = ip_network(f'{siguiente_base}/{mask}')
                        contador2 = contador2 + 1
                    rango_subneteado = list(
                        network.subnets(new_prefix=int(mask)))
                contador = contador + 1
                break
            wr.write('\n')


def calcula_mascara(cantidad_hosts):
    max_hosts_keys = list(dic_mascaras.keys())
    for i, max_hosts in enumerate(max_hosts_keys):
        if (max_hosts - 2) == cantidad_hosts:
            return dic_mascaras[max_hosts_keys[i]]
        elif max_hosts - 2 < cantidad_hosts:
            return dic_mascaras[max_hosts_keys[i - 1]]
    return -1


# wr.write calcula_mascara(12))
