# Sistema de Vendas de Tíquetes - RU UEM

Trabalho desenvolvido em dupla para a disciplina de Fundamentos de Algoritmos (2024) da Universidade Estadual de Maringá.

O objetivo foi criar um programa em Python executado no terminal para simular o processo de venda de tíquetes do Restaurante Universitário e gerar relatórios simples ao final do dia.

## O que o programa faz

- **Registro de vendas:** permite escolher a categoria da pessoa (aluno, servidor, docente ou externo), a quantidade de refeições e a forma de pagamento (PIX, dinheiro ou cartão). O sistema calcula o total e pede confirmação antes de salvar a operação.
- **Tabela de preços aplicada:**
  - Alunos e servidores com renda de até 3 salários mínimos: R$ 5,00
  - Servidores com renda acima de 3 salários mínimos e docentes: R$ 10,00
  - Comunidade externa: R$ 19,00
- **Relatório diário:** calcula a receita total acumulada, o total de tíquetes vendidos e monta no próprio terminal dois gráficos de barras em texto:
  - Distribuição percentual de tíquetes vendidos por categoria de usuário.
  - Distribuição percentual da receita obtida por método de pagamento.

## Como foi feito

O código foi escrito em Python padrão, sem dependências externas, utilizando principalmente:

- `Enum` para organizar os tipos de usuários e meios de pagamento.
- `dataclass` para estruturar os dados de cada tíquete vendido.
- Listas e laços de repetição para armazenar e processar as transações em memória.
- Testes de exemplo documentados diretamente nas funções (`doctest`).

## Autores

- Arthur Kendy Nishimuta
- Bianca Yuka Kokubu
