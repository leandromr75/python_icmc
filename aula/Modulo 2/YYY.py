
class Corretor:
    
    def var(self, string):
        ''' Cria as variações da string dada '''
        sub_lista = [] 
        for i, letra in enumerate(string):
            lista = list(string)
            lista.pop(i) 
            sub_lista += [''.join(lista)] 
        return {item:string for item in sub_lista}    
   
    def conc_lista_dic(self, lista):
        ''' Concatena os dicionários de uma lista '''
        dic = {}
        for item in lista:
            dic.update(item)
        return dic

    def __init__(self,arquivo):
        ''' Lê o arquivo linha a linha, cria uma lista de dicionarios e concatena a lista '''
        with open(arquivo,'r') as f:
            self.lista_dic = [self.var(item) for item in f.read().splitlines()]
            self.dicionarios = self.conc_lista_dic(self.lista_dic)
    
    def sugere(self, string):
        ''' Verifica se a string é chave do dicionario e retornar a palavra correta ''' 
        try:
            return self.dicionarios[string]
        except KeyError:
            print('Palavra desconhecida.')
