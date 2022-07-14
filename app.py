from POO.CalcIPv4.classes import CalcIPv4


calc_ipv4 = CalcIPv4(ip='192.168.0.1', masc='255.255.255.192')

print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.masc}')
print(f'Rede: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Prefixo: {calc_ipv4.prefixo}')
print(f'N° de IPs da rede: {calc_ipv4.n_ips}')
