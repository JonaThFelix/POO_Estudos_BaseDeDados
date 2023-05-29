from BaseDeDados import BaseDeDados as rp

def i():
  print('-'*65)
  
repositorio1 = rp()

i()
#adicionei os elementos ao vetor
repositorio1.inserir(1, 'jubileu')
repositorio1.inserir(2, 'carlos')
repositorio1.inserir(3, 'beatriz')
repositorio1.inserir(4, 'ana')

#listei pra verificar se de fato foram preenchidos
repositorio1.listar()

#removi o elemento 2, carlos
repositorio1.remover(2)
i()
#listei para verificar se de fato o elemento 2 foi removido
repositorio1.listar()
