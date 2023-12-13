from collections import deque
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if no is None:
            return No(chave)

        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)

        return no

    def percorrer_em_ordem(self):
        resultado = []
        self._percorrer_em_ordem(self.raiz, resultado)
        return resultado

    def _percorrer_em_ordem(self, no, resultado):
        if no:
            self._percorrer_em_ordem(no.esquerda, resultado)
            resultado.append(no.chave)
            self._percorrer_em_ordem(no.direita, resultado)

    def profundidade(self):
        return self._profundidade(self.raiz)

    def _profundidade(self, no):
        if no is None:
            return 0

        profundidade_esquerda = self._profundidade(no.esquerda)
        profundidade_direita = self._profundidade(no.direita)

        return max(profundidade_esquerda, profundidade_direita) + 1

    def nos_folha(self):
        return self._nos_folha(self.raiz)

    def _nos_folha(self, no):
        if no is None:
            return []

        if no.esquerda is None and no.direita is None:
            return [no.chave]

        nos_folha_esquerda = self._nos_folha(no.esquerda)
        nos_folha_direita = self._nos_folha(no.direita)

        return nos_folha_esquerda + nos_folha_direita
    

# usando

arvore = ArvoreBinaria()
chaves = [200, 450, 123, 52, 133, 321, 422, 523, 36, 64]

for chave in chaves:
    arvore.inserir(chave)

print("Percorrendo em Ordem:", arvore.percorrer_em_ordem())
print("Profundidade da Árvore:", (arvore.profundidade()-1))
print("Nós Folha:", arvore.nos_folha())