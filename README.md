# IA-Trabalho-Final

Opção 1: Implementação de um Agente Inteligente para Resolução de Problemas em Am
bientes Dinâmicos.
Objetivo: Implementar umagenteinteligente que possa resolver problemas em um ambiente dinâmico simulado, como um labirinto ou um jogo simples (exemplo: caça ao tesouro).
Descrição:
    1. Definição do Ambiente: Criar ou escolher um ambiente simulado que represente o problema a ser resolvido. O ambiente deve conter elementos dinâmicos que possam mudar ao longo do tempo, como obstáculos móveis ou mudanças nas regras do jogo.
    2. Projeto do Agente: O agente deve ser capaz de perceber o ambiente, tomar decisões com base nas informações disponíveis e agir para alcanc¸ar um objetivo específico, como encontrar a saída do labirinto ou coletar todos os tesouros.
    3. Estratégias de Busca e Decis˜ ao: Implementar uma ou mais estratégias de busca (ex.: busca em profundidade, busca em largura, busca A*) para guiar o agente. Implementar uma forma de o agente aprender com experiências anteriores, melhorando suas decisões ao longo do tempo (ex.: aprendizado por reforço).
    4. Teste e Avaliação: Testar o desempenho do agente em diferentes cenários, avaliando a eficiência e a capacidade de adaptação do agente.
    Entrega: Código-fonte, documentação explicando o design do agente e a escolha das estratégias de busca, além de um relatório detalhado com a análise dos resultados.
    Tecnologias sugeridas: Python (usando bibliotecas como Pygame para simulação), Java, ou outra linguagem de escolha

Opção 2: Sistema de Inferência Baseado em Lógica de Primeira Ordem.
Objetivo: Desenvolver um sistema de inferência que utiliza lógica de primeira ordem para resolver problemas complexos de inferência.
Descrição:
    1. Representação do Conhecimento: Definir um conjunto de predicados, funções e regras lógicas
    que representam o conhecimento em um domínio específico. Exemplos incluem um sistema de di
    agnóstico médico ou um sistema de recomendação baseado em preferências e histórico do usuário.
    2. Implementação do Motor de Inferência: Implementar o motor de inferência que, dado um conjunto de fatos e regras, pode derivar novas informações usando técnicas como resolução ou encadeamento (forward chaining/backward chaining).
    3. Interface do Usuário: Opcionalmente, criar uma interface para entrada de fatos e visualização dos resultados da inferência, ou permitir a interação via console.
    4. Teste e Validação: Testar o sistema com diferentes conjuntos de dados para garantir que a inferência lógica funcione corretamente e seja capaz de lidar com casos complexos.
    Entrega: Código-fonte, documentação detalhada sobre a representação do conhecimento e a implementação do motor de inferência, além de um relatório com a avaliação dos testes. 
    Tecnologias sugeridas: Prolog, Python (com bibliotecas como pyDatalog), Java.


Opção 3: Desenvolvimento de um Sistema de Busca Informada para Resolução de Problemas de Planejamento.
Objetivo: Implementar um sistema de busca informada, como o algoritmo A*, para resolver problemas de planejamento, como o problema do caminho mais curto em um grafo.
Descrição:
    1. Definição do Problema: Escolher um problema de planejamento, como encontrar o caminho mais curto em um grafo, resolver um quebra-cabeça, ou planejar rotas para entregas de mercadorias.
    2. Implementação do Algoritmo de Busca: Implementar o algoritmo de busca A* utilizando uma função heurística apropriada ao problema escolhido. Testar diferentes heurísticas e analisar seu impacto no desempenho do algoritmo.
    3. Comparação com Outras Técnicas: Implementar também algoritmos de busca não informada,
    como busca em profundidade e busca em largura, e comparar os resultados em termos de tempo
    de execução e número de nós explorados.
    4. Visualização dos Resultados: Criar visualizações que mostrem o processo de busca e a solução final encontrada. Isso pode incluir animações que mostram o progresso do algoritmo em encontrar a solução.
    Entrega: Código-fonte, documentação explicando a implementação do algoritmo A* e as heurísticas utilizadas, um relatório detalhado com a comparação entre os diferentes algoritmos e uma análise dos resultados.
    Tecnologias sugeridas: Python (com bibliotecas como NetworkX para grafos), Java, C++.

    Entendido, vou proceder com a análise dos arquivos enviados e sugerir possíveis melhorias com base no que foi implementado até agora. 


### Sugestões Gerais:

1. **Melhoria nas Heurísticas:**
   - Além da Euclidiana e Manhattan, uma boa sugestão seria adicionar a heurística baseada nas distâncias em linha reta (hDLR), conforme já discutido. Isso pode ser especialmente relevante para melhorar a eficácia do A* com um dado mais realista (mesmo que estimado).

2. **Comparação de Algoritmos:**
   - Atualmente, o código executa e mostra o caminho encontrado pelos diferentes algoritmos. Uma melhoria interessante seria fazer uma comparação direta entre eles em termos de:
     - Tempo de execução
     - Número de nós explorados
   - Isso pode ser medido com o uso da biblioteca `time` para medir o tempo e uma contagem dos nós visitados dentro de cada algoritmo.

3. **Visualização:**
   - A visualização atual mostra o grafo e o caminho final. Algumas sugestões para melhorar isso incluem:
     - Mostrar a sequência de exploração dos nós ao longo do tempo.
     - Destaque visual dos nós visitados (talvez com cores que mudam conforme o algoritmo visita cada nó).
     - Incluir a capacidade de salvar a visualização em um arquivo de imagem, útil para relatórios.

4. **Manutenção da Consistência nos Algoritmos:**
   - Verifique se todos os algoritmos estão utilizando estruturas de dados eficientes. Por exemplo, no A*, o uso da fila de prioridade (`heapq`) já é eficiente. Para o DFS e BFS, certifique-se de que a estrutura de fila (deque) esteja sendo usada corretamente para garantir a eficiência máxima.

5. **Relatório Automático:**
   - Adicionar uma funcionalidade para gerar um relatório comparativo entre os diferentes algoritmos automaticamente, incluindo:
     - Caminho encontrado
     - Distância total
     - Tempo de execução
     - Número de nós explorados
   - Isso pode ser gerado em um arquivo `.txt` ou `.csv` para ser utilizado na análise final do trabalho.

6. **Modularidade:**
   - A implementação está bem modularizada, mas uma sugestão é dividir as funções em arquivos menores caso o projeto aumente de tamanho. Por exemplo, as heurísticas podem ser separadas em um arquivo próprio se houver várias opções.