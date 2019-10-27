                  ### CÓDIGO PARA A VISUALIZAÇÃO DE UM DIAGRAMA DE VORONOY ###

#Importando a biblioteca PIL (Python Imaging Library). Ela é responsável por permitir que
#trabalhemos com manipulação de imagens em Python e seus features serão utilizados para que
#possamos demonstrar visualmente o diagrama gerado.
from PIL import Image
#Importando a biblioteca random para que possamos gerar os pontos em nosso plano
#bidimensional de uma forma aleatoria
import random
#Importando a biblioteca math, pois necessitamos dela para realizarmos certas operações
#e cálculos que necessitam de certas funções presentes nessa biblioteca
import math

def Voronoy(width, height, num_cells):
	diagrama = Image.new("RGB", (width, height)) #Utilizando o módulo Image, criamos uma nova imagem com o método new() que recebe como paramêtros: o modo(que define o tipo e a profundidade do pixel) e as dimensões da nova imagem criada (width e height). Por convenção, adotamos o modo RGB. 
	putpixel = diagrama.putpixel #Apenas renomeando o método image.putpixel. Esse método é responsável por modificar um pixel em uma dada posição. Os parâmetros desse método são: a posição do pixel na imagem(segundo o sistema de coordenadas cartesianas: (x,y) ) e uma tupla indicando a coloração do pixel, seguindo o modo RGB. 
	imgx, imgy = diagrama.size # Método responsável por retornar o tamanho da imagem. O tamanho retornado é uma 2-tupla (width, height)
	#Os pixeis no eixo x estão rotulados da seguinte forma: 0, 1, 2, ..., imgx - 1.
	#O mesmo vale para os pixeis do eixo y.
	nx = [] #list responsável por guardar as coordenadas x de todos os sítios de Voronoy presentes na imagem em questão.
	ny = [] #list responsável por guardar as coordenadas y de todos os sítios de Voronoy presentes na imagem em questão.
	nred = [] #list responsável por guardar a componente R (vermelha/red) da cor que será usada pra colorir cada célula de Voronoy.
	ngreen = [] #list responsável por guardar a componente G (verde/green) da cor que será usada pra colorir cada célula de Voronoy.
	nblue = [] #list responsável por guardar a componente B (azul/blue) da cor que será usada pra colorir cada célula de Voronoy.
	for i in range(num_cells): 
		# A geracao das coordenadas dos sítios de Voronoy, bem como de suas respectivas cores é feita de forma aleatória.
		nx.append(random.randrange(imgx))
		ny.append(random.randrange(imgy))
		nred.append(random.randrange(256))
		ngreen.append(random.randrange(256))
		nblue.append(random.randrange(256))
	#Basicamente, o que acontece aqui é que eu estou iterando sobre todos os pixeis presentes na imagem. Estou computando a distancia de cada
	#pixel para todos os sítios de Voronoy presentes na imagem e guardo qual foi a mínima distância encontrada e o índice do Sítio de Voronoy que está
	#mais próximo do ponto em questão. Depois de fazer todos esses cálculo, atribuimos (mudando a coloração do pixel em questão) o píxel à Célula de Voronoy
	#mais próxima. E, iterativamente, vamos construindo as Células de Voronoy e, consequentemente, o Diagrama de Voronoy.
	# O Algoritmo em questão apresenta complexidade temporal: O(N*M) 
	# N -> número de píxeis presentes em cada linha.
	# M -> número de píxeis presentes em cada coluna.
	for y in range(imgy): #Todos os píxeis em Height
		for x in range(imgx): #Todos os píxeis em Width                                                          '''
			dmin = math.hypot(imgx-1, imgy-1) #Atribui para dmin a maior distancia possivel.
			j = -1 # a variavel j guarda o id do Sítio de Voronoy que se encontra mais próximo do ponto em questão.
			for i in range(num_cells):
				d = math.hypot(nx[i]- x, ny[i]- y)
				if d < dmin:
					dmin = d
					j = i
			putpixel((x, y), (nred[j], ngreen[j], nblue[j])) #Realizando uma alteração em um píxel específico.
	for element in zip(nx, ny): #Irei deixar todos os pontos que representam o sítio de um Diagrama de Voronoy na cor preta para facilitar a visualização no Diagrama de Voronoy.
		tupla = (element[0], element[1])
		tupla1 = (element[0] + 1, element[1])
		tupla2 = (element[0], element[1] + 1)
		tupla3 = (element[0] - 1, element[1])
		tupla4 = (element[0], element[1] - 1)
		putpixel(tupla, (0, 0, 0)) #Esse é o código rgb que equivale à cor preta.
		putpixel(tupla1, (0, 0, 0))
		putpixel(tupla2, (0, 0, 0))
		putpixel(tupla3, (0, 0, 0))
		putpixel(tupla4, (0, 0, 0))
	diagrama.save("Diagrama de Voronoy.png", "PNG") #Método responsável por salvar como arquivo ".png" a imagem do Diagrama de Voronoy gerado.
	diagrama.show() #Método responsável por permitir a visualização do arquivo ".png" para o usuário por meio de um pop-up.

def main():
	print("Digite o comprimento, a altura e a quantidade de sitios de Voronoy, respectivamente, para gerar o Diagrama de Voronoy:")
	info = list(map(int, input().split())) #Recebendo a entrada.
	# info[0] = Comprimento da imagem (width)
	# info[1] = Altura da imagem (height)
	# info[2] = Quantidade de sítios de Voronoy que estarão presentes no Diagrama de Voronoy gerado.
	Voronoy(info[0], info[1], info[2])


if __name__ == "__main__":
	main()
