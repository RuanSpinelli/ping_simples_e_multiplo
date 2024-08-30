import os
import time

#with open("nome_do_arquivo_que_quer_abrir.extensão") as nome_para_se_referir_ao_arquivo
with open("hosts.txt") as arquivo:
    dump = arquivo.read()
    dump = dump.splitlines()
    
    for ip in dump:
        
        print(f"verificando o ip {ip}")
        print("-=" * 30)
        os.system(f'ping -n 2 {ip}')
        print("-=" * 30)
        time.sleep(5)
