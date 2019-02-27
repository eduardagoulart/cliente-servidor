"""
Essa função testa se a URL passada é válida, ou seja, começa com http://
"""


def le_url(url):
    if "http://" not in url:
        print("Site inválido, por favor tente outro")
        exit(400)
    url = url.split("http://")

    if len(url) > 1:
        url.pop(0)
        url = url[0]
    print(url)


le_url("http://www.presidentesjdr.com.br/")
