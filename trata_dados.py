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
        print(url)
