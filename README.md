# Cliente Servidor

Trabalho prático da disciplina de Redes de computadores - UFSJ, ministrada
 por Flávio Luiz Schiavoni, 2019.1 
 
 ## Como rodar
 No terminal digite para conectar ao servidor de um site:
 ```
 python cliente.py navegador url_da_pagina_baixada porta 
 ```
 
 Para conectar com o servidor local, digite:
 
 ```
 python cliente.py servidor pagina_buscada porta
```
 caso a porta não seja fornecida, o valor utilizado será 80.
 
 
 Para executar o servidor, digite:
```
python servidor.py caminho porta
```
 
 ## Dependências
```
Python 3.6
socket
sys
threading
```

Eduarda Goulart