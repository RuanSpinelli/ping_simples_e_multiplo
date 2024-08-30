import os #importando a biblioteca para integrar programas e recursos do sistema operacional
print("#" * 60 )

ip_ou_host = input("Digite o IP ou host a ser verificado: ") #uma variável que vai guardar o ip ou host que fara o ping

print("-=" * 30)

os.system(f'ping -n 6 {ip_ou_host}') #chama o system da biblioteca os. executa o comando ping e usa o parâmetro
# -n para definir quantos pacotes serão enviados