class BaseDeDados:

  #início construtor
  def __init__(self):
    self.dados = [] #argumento definido, sem uso no construtor, tipo vetor

  
  def inserir(self, id, nome): #chamado id e nome, pois n está no construtor
    vetor = id, nome
    self.dados.append(vetor) #add elementos a tupla

  
  def listar(self): #exemplo básico de listagem usando o for (percorrer lista ou tupla)
    for i in self.dados:
      print(i)

  
  def remover(self, id):
    i = 0
  
    while i < len(self.dados):
      if self.dados[i][0] == id:
        self.dados.pop(self.dados.index(self.dados[i]))
        i = 0
      else:
        i += 1
