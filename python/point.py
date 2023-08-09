## Instanciar uma classe -> nome_do_objeto = Classe()
## nome_do_objeto pode ser o que voce quiser
## Classe(), deve respeitar o construtor da classe que você quer instanciar.
##EX: Se em __init__(self, moranguinho, batatinha, capim), ao instanciar a classe, ela deve receber os parametros moranguinho, batatinha, capim 
##->> Classe(moranguinho, batatinha, capim)
class Point:
    def __init__(self, point1=0, point2=0):
        self.move(point1, point2)
 
    def move(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
 
    def reset(self):
        self.move(0, 0)
 
    def calculate_distance(self, other_point):
        return (
            (self.point1 - other_point.point1) ** 2
            + (self.point2 - other_point.point2) ** 2
        ) ** (1/2)