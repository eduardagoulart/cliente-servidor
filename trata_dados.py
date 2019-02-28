class ProcessaDadosURL:
    def __init__(self, url):
        self.url = url

    """
    Essa função testa se a URL passada é válida, ou seja, começa com http://
    """

    def le_url(self):
        if "http://" not in self.url:
            print("Site inválido, por favor tente outro")
            exit(400)
        url = self.url.split("http://")

        if len(url) > 1:
            url.pop(0)
            url = url[0]
        return url

    def separa_nome_diretorio(self):
        url = self.le_url()
        tamanho_nome = 0
        for i in range(len(url)):
            tamanho_nome += 1
            if i == '/':
                break

        nome_do_site = []
        diretorio = []
        for i in range(0, tamanho_nome):
            if i < tamanho_nome:
                nome_do_site.append(url[i])
            else:
                diretorio.append(url[i])

        nome_do_site = ''.join(nome_do_site)
        diretorio = ''.join(diretorio)

        return nome_do_site, diretorio


ProcessaDadosURL('http://www.presidentesjdr.com.br/linhasehorarios.html').separa_nome_diretorio()
