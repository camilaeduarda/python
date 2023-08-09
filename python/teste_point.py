from point import Point
objeto_um = Point ()
point2 = Point ()

objeto_um.move (5, 7)
point2.move (-2, 3)

result1 = objeto_um.calculate_distance (point2)
print (f"A distância em relação a point2 é:{result1}")
print (f"Valor do ponto 1 para o objeto objeto_um antes do reset: {objeto_um.point1}") 
#-->> objeto_um.point1 == acessando o objeto objeto_um e lendo com o ponto, o atributo point1 desse objeto
objeto_um.reset ()
print (f"Valor do ponto 1 para o objeto point1 depois do reset: {objeto_um.point1}")
result1 = objeto_um.calculate_distance (point2)
print (f"A distância em relação a point2 é:{result1}")