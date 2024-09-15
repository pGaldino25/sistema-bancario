# Desafio de Caixa Eletrônico - DIO

Este projeto faz parte de um desafio proposto durante o curso na [Digital Innovation One](https://www.dio.me/). O objetivo é criar uma aplicação simulando o funcionamento de um caixa eletrônico, utilizando conceitos de **orientação a objetos** e **clean code** em Python.

## Funcionalidades

A aplicação permite realizar as seguintes operações:

- **Depósito**: Adiciona um valor ao saldo da conta.
- **Saque**: Retira um valor do saldo, respeitando o limite de saques e o limite diário de R$ 500.
- **Extrato**: Exibe o saldo atual e todas as transações realizadas.
- **Sair**: Encerra o programa.

## Regras

- O limite máximo por saque é de **R$ 500**.
- O número máximo de saques permitidos por dia é **3**.
- O valor do depósito deve ser positivo.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/pGaldino25/desafio-caixa-eletronico.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd desafio-caixa-eletronico
    ```

3. Execute o programa:
    ```bash
    python app.py
    ```

## Estrutura do Projeto

- **`ContaBancaria`**: Classe responsável por gerenciar o saldo, realizar depósitos e saques, e gerar o extrato.
- **`CaixaEletronico`**: Classe que controla o fluxo de interação com o usuário, exibindo o menu e encaminhando as operações para a classe `ContaBancaria`.

## Exemplo de Uso

Após rodar o programa, você verá o seguinte menu:

[d] Depositar \
[s] Sacar \
[e] Extrato\
[q] Sair 

=>


Você pode escolher as opções desejadas, inserir valores de saque ou depósito, e visualizar o extrato conforme sua necessidade.

## Requisitos

- Python 3.x

## Licença

Este projeto é distribuído sob a licença MIT. Para mais detalhes, veja o arquivo [LICENSE](LICENSE).
