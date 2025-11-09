import requests
from PIL import Image
from io import BytesIO

class Imagem():
    def imagem_mago():
        url_da_imagem = "https://chatgpt.com/backend-api/estuary/content?id=file_000000001400720e90bdbfea1a8209ed&ts=489634&p=fs&cid=1&sig=2ad4fa22b14e0ec1c946782d4b93b99cd0b571ccd253affaee96415c49f2719a&v=0"
        resposta = requests.get(url_da_imagem)
        imagem_em_memoria = BytesIO(resposta.content)
        imagem_aberta = Image.open(imagem_em_memoria)
        imagem_aberta.show() 


Imagem.imagem_mago()