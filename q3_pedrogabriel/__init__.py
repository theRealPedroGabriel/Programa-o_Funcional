from PIL import Image , ImageEnhance


abrir_imagem = lambda caminho: Image.open("C:\\Users\\pgsmc\\Imagens\\mike.jpg")#caminho da imagem de sua escolha

get_brilho = lambda: float(input('Digite o fator de brilho (0-1): '))

ajustar_brilho = lambda imagem, brilho: ImageEnhance.Brightness(imagem).enhance(brilho)

exibir_imagem = lambda imagem: imagem.show("Imagem com brilho ajustado")

salvar_imagem = lambda imagem, caminho: imagem.save(caminho)

imagem = abrir_imagem('imagem.jpg')

brilho = get_brilho()

imagem_ajustada = ajustar_brilho(imagem, brilho)

exibir_imagem(imagem_ajustada)

salvar_imagem(imagem_ajustada, 'imagem_brilho.jpg')





# Para atualizar o valor para a nova image, utilize image.putpixel((x, y), modified_pixel)
