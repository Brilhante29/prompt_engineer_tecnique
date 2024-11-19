Aqui está um documento de referência abrangente para as técnicas avançadas de prompting, com uma estrutura detalhada de cada técnica, incluindo descrições, processos, exemplos de entrada e saída.

---

# **Guia Completo de Técnicas de Prompting para Modelos de Linguagem**

Este documento descreve as técnicas de prompting avançadas que aprimoram a eficácia dos modelos de linguagem em uma ampla variedade de tarefas. Cada técnica inclui uma explicação sobre o processo, um exemplo ilustrativo de entrada e saída, e o contexto de uso.

---

### **1. Zero-shot Prompting**

**Descrição:** Permite que o modelo realize uma tarefa sem exemplos prévios. Utiliza o conhecimento embutido do modelo para responder diretamente.

- **Exemplo:**
  - **Input:** "Traduza para o francês: 'Bom dia, como você está?'"
  - **Output:** "Bonjour, comment ça va?"

**Processo:** O modelo utiliza seu conhecimento para inferir a resposta sem a necessidade de exemplos adicionais.

---

### **2. Few-shot Prompting**

**Descrição:** Apresenta alguns exemplos da tarefa para guiar o modelo na realização correta.

- **Exemplo:**
  - **Input:** "Traduza para o francês: 'Bom dia' -> 'Bonjour', 'Boa noite' -> 'Bonne nuit', 'Como você está?' ->"
  - **Output:** "Comment ça va?"

**Processo:** Com exemplos, o modelo identifica padrões e os aplica para gerar respostas consistentes.

---

### **3. Chain-of-Thought Prompting**

**Descrição:** Incentiva o modelo a desenvolver um raciocínio passo a passo para resolver problemas complexos.

- **Exemplo:**
  - **Input:** "Se você tem 3 maçãs e ganha mais 2, quantas maçãs você tem? Pense passo a passo."
  - **Output:** "Primeiro, você tem 3 maçãs. Depois, ganha mais 2. 3 + 2 = 5. Portanto, você tem 5 maçãs."

**Processo:** O modelo divide o problema em partes menores, o que aumenta a clareza e precisão da resposta.

---

### **4. Self-Consistency**

**Descrição:** Gera múltiplas respostas e escolhe a mais consistente para melhorar a precisão.

- **Exemplo:**
  - **Input:** "Se você tem 3 maçãs e ganha mais 2, quantas maçãs você tem?"
  - **Output:** "5 maçãs."

**Processo:** O modelo avalia várias tentativas e seleciona a resposta que se repete com mais frequência.

---

### **5. Generate Knowledge Prompting**

**Descrição:** Permite ao modelo gerar conhecimento adicional relevante antes de responder.

- **Exemplo:**
  - **Input:** "Quem escreveu 'Dom Quixote'?"
  - **Output:** "Miguel de Cervantes."

**Processo:** O modelo recupera informações sobre o tópico antes de formular a resposta final.

---

### **6. Prompt Chaining**

**Descrição:** Combina múltiplos prompts em sequência, em que a saída de um serve de entrada para o próximo.

- **Exemplo:**
  - **Prompt 1 Input:** "Liste os ingredientes para uma salada grega."
  - **Prompt 1 Output:** "Tomate, pepino, cebola, azeitonas, queijo feta."
  - **Prompt 2 Input:** "Forneça a receita usando esses ingredientes."
  - **Prompt 2 Output:** "Corte tomate, pepino e cebola. Misture com azeitonas e queijo feta. Tempere com azeite, sal e orégano."

**Processo:** A saída do primeiro prompt alimenta o segundo, criando um fluxo lógico para gerar a resposta.

---

### **7. Tree of Thoughts**

**Descrição:** O modelo explora múltiplos caminhos de raciocínio para resolver questões complexas.

- **Exemplo:**
  - **Input:** "Como resolver o problema da fome mundial?"
  - **Output:** "1. Aumentar a produção agrícola. 2. Melhorar a distribuição de alimentos. 3. Reduzir o desperdício."

**Processo:** O modelo considera múltiplas abordagens e seleciona as mais promissoras para a resposta final.

---

### **8. Retrieval-Augmented Generation (RAG)**

**Descrição:** Recupera informações de uma base de dados externa para fornecer uma resposta precisa.

- **Exemplo:**
  - **Input:** "Qual é a capital do Brasil?"
  - **Output:** "Brasília."

**Processo:** O modelo consulta fontes externas para obter informações antes de responder.

---

### **9. Automatic Reasoning and Tool-use**

**Descrição:** O modelo utiliza ferramentas externas para cálculos ou consultas especializadas.

- **Exemplo:**
  - **Input:** "Qual é a raiz quadrada de 144?"
  - **Output:** "12."

**Processo:** Reconhecendo a necessidade de cálculo, o modelo utiliza uma ferramenta ou realiza o cálculo internamente.

---

### **10. Automatic Prompt Engineer**

**Descrição:** O modelo gera prompts para guiar a si mesmo ou outro modelo em uma tarefa específica.

- **Exemplo:**
  - **Input:** "Crie um prompt para uma história de ficção científica."
  - **Output:** "Escreva uma história ambientada em um futuro onde IA governa o mundo, explorando os desafios e benefícios."

**Processo:** O modelo desenvolve prompts relevantes, facilitando a geração de conteúdo alinhado ao objetivo.

---

### **11. Active-Prompt**

**Descrição:** Permite interação ativa com o usuário para melhorar o contexto e a precisão da resposta.

- **Exemplo:**
  - **Input:** "Conte-me sobre a Revolução."
  - **Modelo:** "Você poderia especificar qual revolução?"
  - **Usuário:** "Revolução Industrial."
  - **Output:** "A Revolução Industrial começou no século XVIII e transformou a produção..."

**Processo:** O modelo interage com o usuário para refinar o escopo da resposta.

---

### **12. Directional Stimulus Prompting (DSP)**

**Descrição:** Utiliza um estímulo direcional para guiar o LLM em direção a saídas específicas.

- **Exemplo:**
  - **Input:** Artigo: "A IA está transformando a saúde."
  - **Estímulo Direcional:** "Palavras-chave: IA, saúde, diagnósticos"
  - **Output:** "A IA aprimora diagnósticos e tratamentos na saúde."

**Processo:** Um modelo menor gera palavras-chave que direcionam o LLM, otimizando a resposta.

---

### **13. Program-Aided Language Models (PAL)**

**Descrição:** O modelo cria programas para resolver problemas complexos em vez de resolvê-los diretamente.

- **Exemplo:**
  - **Input:** "Qual é a soma dos números de 1 a 100?"
  - **Programa Gerado:** `sum(range(1, 101))`
  - **Output:** "5050"

**Processo:** O modelo cria um programa que, ao ser executado, produz a resposta.

---

### **14. ReAct (Reasoning and Acting)**

**Descrição:** O modelo intercala raciocínio e ações, como consultas de pesquisa, para chegar à resposta.

- **Exemplo:**
  - **Input:** "Quem é o presidente atual do Brasil?"
  - **Pensamento:** "Preciso verificar a informação."
  - **Ação:** "Pesquisar [presidente do Brasil]"
  - **Output:** "Lula."

**Processo:** Combina raciocínio com ações, consultando fontes para assegurar precisão.

---

### **15. Reflexion**

**Descrição:** Permite que o modelo aprenda com feedback linguístico, ajustando-se iterativamente.

- **Exemplo:**
  - **Input:** "O que tem chaves, mas não abre portas?"
  - **Tentativa 1:** "Uma senha."
  - **Feedback:** "Incorreto."
  - **Reflexão:** "Considere objetos físicos."
  - **Tentativa 2:** "Um piano."
  - **Output:** "Correto."

**Processo:** Após feedback, o modelo ajusta suas tentativas para melhorar a resposta.

---

### **16. Multimodal Chain-of-Thought (CoT)**

**Descrição:** Usa dados textuais e visuais para resolver problemas.

- **Exemplo:**
  - **Input:** Gráfico de vendas mensais: "Em qual mês as vendas foram mais altas?"
  - **Raciocínio:** "A barra mais alta corresponde a março."
  - **Output:** "As vendas foram mais altas em março."

**Processo:** O modelo combina texto e imagem para fornecer a resposta.

---

### **17. Graph Prompting**

**Descrição:** Usa grafos para estruturar relações entre conceitos ou entidades.

- **Exemplo:**
  - **Input:** "Explique a relação entre células, tecidos e órgãos."
  - **Grafo:** "Células → Tecidos → Órgãos"
  - **Output:** "Células formam tecidos, que formam órgãos."

**Processo:** Estruturas de grafos permitem raciocínios mais organizados.

---

### **18. Meta-Prompting**

**Descrição:** O modelo gera prompts adicionais para si mesmo para criar uma melhor resposta.

- **Exemplo:**
  - **Input:** "Estratégia para aprender um idioma."
  - **Meta-Prompt:** "Quais perguntas devo fazer para criar um plano?"
  - **Output:** "Perguntas como: 'Qual é meu nível?' e 'Quanto tempo posso dedicar?' ajudam a criar um plano."

**Processo:** O

 modelo identifica questões fundamentais para formular uma resposta abrangente.

---

Este documento fornece uma referência rápida para as técnicas mais avançadas de prompting, facilitando a escolha e implementação da estratégia adequada para diferentes aplicações e contextos de uso.