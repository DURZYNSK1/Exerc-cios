#CALCULADORA
while True:
    try:
      num_1 = float(input('Digite um número:'))
      num_2 = float(input('Digite um número: '))
      print('[1] Multiplicar')
      print('[2] Somar')
      print('[3] Dividir')
      print('[4] Subtrair')
      print('[5] Sair')
      
      operacao = input('Escolha sua operação: ')
      if operacao == '5':
           print('Saindo da calculadora.')
           break
           
      if operacao not in ['1', '2', '3', '4']:
       print('Opção inválida. Tente novamente.')
       continue
       
       if operacao == '1':
        print(f'Resultado: {num_1 * num_2}')
        
      elif operacao == '2':
       print(f'Resultado: {num_1 + num_2}')
       
      elif operacao == '3':
        if num_2 == 0:
            print('Não é possível dividir por zero.')
        else:
            print(f'Resultado: {num_1 / num_2}')
      elif operacao == '4':
       print(f'Resultado: {num_1 - num_2}')

    except ValueError:
        print('Você não digitou um número!')
        continue
    