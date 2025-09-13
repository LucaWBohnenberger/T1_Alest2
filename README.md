# Projeto Fintech: Simulador de Livro de Ordens (HAL Corporation)

Este projeto implementa um sistema de processamento de ordens de compra e venda de ações para a HAL Corporation, desenvolvido para uma empresa do setor financeiro. O objetivo principal do simulador é encontrar as melhores combinações de transações para maximizar o lucro da fintech, processando as ordens em tempo real com alta performance.

## 1. O Problema a ser Resolvido

A fintech recebe um fluxo contínuo de ordens de compra e venda de ações. O sistema deve processar cada nova ordem que chega, executando imediatamente todas as transações possíveis e lucrativas.

As especificações são:
* **Ordem de Compra (`C <quant> <preço>`)**: Representa o desejo de comprar uma quantidade `<quant>` de ações por um preço **máximo** de `<preço>` por ação.
* **Ordem de Venda (`V <quant> <preço>`)**: Representa o desejo de vender uma quantidade `<quant>` de ações por um preço **mínimo** de `<preço>` por ação.
* **Lucro da Fintech**: O lucro é gerado pela diferença (o "spread") entre o preço de uma ordem de compra e o de uma ordem de venda compatível. Por exemplo, ao casar uma compra de R$12 com uma venda de R$10, a fintech lucra R$2 por ação negociada.
* **Objetivo Principal**: A estratégia de negócio deve ser sempre a de **maximizar o lucro**, o que implica em maximizar a diferença de preço em cada transação.
* **Requisito de Desempenho**: O algoritmo precisa ser extremamente rápido para lidar com milhares de transações por segundo.

## 2. Estratégia da Solução

Para garantir o lucro máximo a cada momento, a estratégia adotada é a de sempre casar a melhor oferta de compra com a melhor oferta de venda disponíveis. Isso se traduz em:

> **Casar a ordem de compra com o preço mais alto disponível com a ordem de venda com o preço mais baixo disponível.**

Uma transação só é válida se `preço_compra >= preço_venda`. Ao seguir essa regra a cada nova ordem, garantimos que cada transação individual gere o maior lucro possível. Como as ordens são processadas sequencialmente, a maximização local em cada passo leva à maximização do lucro total ao final da simulação.

## 3. Algoritmos e Estruturas de Dados Utilizados

Para implementar a estratégia de forma eficiente, a escolha das estruturas de dados é crucial. Um acesso rápido às "melhores" ordens de compra e venda é fundamental.

A solução foi implementada utilizando duas **Filas de Prioridade (Heaps)**:

### Max-Heap (Heap Máximo) para Ordens de Compra
* **O que é**: Uma estrutura de dados que mantém a ordem de compra com o **maior preço** sempre no topo.
* **Por que foi usado**: Permite acesso em tempo constante `O(1)` à melhor oferta de compra (a que paga mais), que é essencial para casar com novas ordens de venda. As operações de inserção e remoção têm complexidade logarítmica `O(log n)`, o que é extremamente eficiente.

### Min-Heap (Heap Mínimo) para Ordens de Venda
* **O que é**: Uma estrutura de dados que mantém a ordem de venda com o **menor preço** sempre no topo.
* **Por que foi usado**: Da mesma forma, permite acesso `O(1)` à melhor oferta de venda (a que pede menos), garantindo a maximização do spread ao casar com novas ordens de compra. A complexidade das operações também é `O(log n)`.

### Fluxo do Algoritmo:
1.  **Chega uma nova Ordem de Compra (C 100  R$50)**:
    * O sistema consulta o topo do **Min-Heap de Vendas**.
    * Enquanto houver ordens de venda com preço `<= R$50`, o sistema remove a de menor preço (ex: V 80  R$45), executa a transação, calcula o lucro (100 * (50-45)), e atualiza as quantidades.
    * Se a ordem de compra não for totalmente satisfeita, o restante é inserido no **Max-Heap de Compras**.

2.  **Chega uma nova Ordem de Venda (V 200  R$60)**:
    * O sistema consulta o topo do **Max-Heap de Compras**.
    * Enquanto houver ordens de compra com preço `>= R$60`, o sistema remove a de maior preço (ex: C 150  R$62), executa a transação, calcula o lucro, e atualiza as quantidades.
    * Se a ordem de venda não for totalmente satisfeito, o restante é inserido no **Min-Heap de Vendas**.

## 4. Resultados dos Testes

O algoritmo foi executado com o arquivo de teste fornecido. Os resultados obtidos pela simulação batem exatamente com os valores de referência confirmados pela fintech.

* **Lucro da Empresa**: $45538
* **Quantidade de Ações Negociadas**: 1228
* **Ordens de Compra Pendentes**: 3
* **Ordens de Venda Pendentes**: 7

O tempo de execução para este volume de transações é praticamente instantâneo, validando a eficiência da abordagem.

## 5. Conclusões sobre o Desempenho

A solução desenvolvida atende ao requisito de alta performance de forma robusta. A complexidade de tempo para processar uma única nova ordem que resulta em `k` transações é de `O(k * log n)`, onde `n` é o número de ordens pendentes no livro de ofertas.

Como as operações fundamentais (`inserir`, `remover` e `consultar o topo`) nas heaps são logarítmicas, o sistema escala de forma excelente. Mesmo com milhões de ordens pendentes no livro, o tempo para processar uma nova ordem permanece extremamente baixo, garantindo a capacidade do sistema de lidar com o volume de "milhares de transações por segundo" exigido pela fintech. A escolha de Heaps foi, portanto, a mais acertada para este problema.
