class Employee:
    '''
    Essa classe employee possui os métodos raise_salary (valor) e get_info ()
    '''
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary (self, valor):
        '''
        raise_salary ARGS: valor --> int

        Este método realiza um aumento percentual no salário do empregado.
        '''
        print (f'Recebendo um aumento de:{valor}%')
        porcentagem = valor/100

        self.salary += porcentagem * self.salary

    def get_info (self):
        '''
        Este método exibe as informações do empregado.
        '''
        return f'Nome: {self.name}\n Salário Atual: {self.salary}'