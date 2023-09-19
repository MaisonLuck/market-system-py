class Mercadinho:
  def __init__(self):
    self.catalago = {'arroz': 10.0, 'macarrao': 7.5, 'acucar': 4.75, 'carne': 45.0}
    self.carrinho = {}
    self.total = 0.0
    
  def comprar(self):
    while True:
      print('Catalago de produtos:')
      for produto, preco, in self.catalago.items():
        print(f'{produto.capitalize()} - R${preco:.2f}')
        
      escolha = input('Digite o nome do produto que deseja comprar (ou "sair" para encerrar): ')
      if escolha.lower() == 'sair':
       break
      
      if escolha in self.catalago:
        quantidade = int(input('Digite a quantidade desejada: '))
        if escolha in self.carrinho:
          self.carrinho[escolha] += quantidade
        else:
          self.carrinho[escolha] = quantidade
        print(f'{quantidade} unidades de {escolha.capitalize()} adicionadas ao carrinho.')
        
      else:
        print('Produto não encontrado no catalago. Tente Novamente.')
          
    print('\n Resumo da compra')
    for produto, quantidade in self.carrinho.items():
      preco_unitario = self.catalago[produto]
      preco_total = preco_unitario * quantidade
      print(f'{quantidade} unidades de {produto.capitalize()} - R${preco_total:.2f}')
      self.total += preco_total  
      
    print(f'Total da compra: R${self.total:.2f}')
    self.Pagar
      
  def Pagar(self):
    pagamento = input('Digite o valor recebido pelo cliente (ou "cancelar" para cancelar a compra)')
    if pagamento.lower() == 'cancelar':
      print('Compra cancelada.')
      return
    
    valor_pago = float(pagamento)
    troco = valor_pago - self.total
    
    if troco > 0:
      print(f'Valor insuficiente. Faltam R${-troco:.2f}')
      self.Pagar()
    else:
      if troco > 0:
        print(f'Troco: R${troco:.2f}')
      cpf_nota = input('Deseja informar o seu CPF na nota fiscal? (sim/não): ')
      if cpf_nota.lower() == 'sim':
          cpf = input('Digite o seu CPF: ')
          print(f'Nota fiscal: Total da compra - R${self.total:.2f} | CPF - {cpf}')
      else:
        print(f'Nota fiscal: Total da compra - R${self.total:.2f}')
        
    self.catalago = {'arroz': 10, 'macarrao': 7.5, 'acucar': 4.75, 'carne': 45.0}
    self.carrinho = {}
    self.total = 0.0


mercado = Mercadinho()

mercado.comprar()    
                                 