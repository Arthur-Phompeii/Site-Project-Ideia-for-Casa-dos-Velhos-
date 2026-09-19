# Implementação simples de fila usando lista
class Fila:
  def __init__(self):
    self.elementos = []
    
  def enqueue(self, item):
    """Adiciona um item no final da fila."""
    self.elementos.append(item)
    
  def dequeue(self):
    """Remove e retorna o item do início."""
    if not self.esta_vazia():
        return self.elementos.pop(0)
    return None
    
  def esta_vazia(self):
    """Verifica se a fila está vazia."""
    return len(self.elementos) == 0
    
  def tamanho(self):
    """Retorna o número de elementos."""
    return len(self.elementos)


# Usando a fila
f = Fila()
f.enqueue("Cliente A")
f.enqueue("Cliente B")
f.enqueue("Cliente C")
print(f.dequeue()) # Imprime "Cliente A"
print(f.dequeue()) # Imprime "Cliente B"


class TarefaPrioritaria:
  def __init__(self, descricao, prioridade):
    self.descricao = descricao
    self.prioridade = prioridade
    
  def __repr__(self):
    return f"[{self.prioridade}] {self.descricao}"

class GerenciadorTarefas:
  def __init__(self):
    self.alta_prioridade = Fila()
    self.normal = Fila()
    self.baixa = Fila()
    
  def adicionar_tarefa(self, tarefa):
    if tarefa.prioridade == "alta":
        self.alta_prioridade.enqueue(tarefa)
    elif tarefa.prioridade == "normal":
        self.normal.enqueue(tarefa)
    else:
        self.baixa.enqueue(tarefa)
    
  def proxima_tarefa(self):
    """Retorna próxima tarefa por ordem de prioridade."""
    if not self.alta_prioridade.esta_vazia():
        return self.alta_prioridade.dequeue()
    elif not self.normal.esta_vazia():
        return self.normal.dequeue()
    elif not self.baixa.esta_vazia():
        return self.baixa.dequeue()
    return None

# Usando o sistema
gerenciador = GerenciadorTarefas()
gerenciador.adicionar_tarefa(TarefaPrioritaria("Enviar email", "normal"))
gerenciador.adicionar_tarefa(TarefaPrioritaria("Corrigir bug crítico","alta"))
gerenciador.adicionar_tarefa(TarefaPrioritaria("Atualizar documentação", "baixa"))
gerenciador.adicionar_tarefa(TarefaPrioritaria("Cagar mole", "alta"))

while True:
 tarefa = gerenciador.proxima_tarefa()
 if tarefa is None:
     break
 print(f"Processando: {tarefa}")