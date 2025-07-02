from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()



comodo = Comodo(
      input('Qual a largura do comodo? '),
      input('Qual a profundidade do comodo? ')
)

print("A area das paredes é: ",
      calc.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura))

print("A area das teto é: ",
      calc.calcular_area_teto(comodo.largura, comodo.profundidade))

print("A litragem de tinta necessária é:",
      calc.calcular_litragem_necessaria())