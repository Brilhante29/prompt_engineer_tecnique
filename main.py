import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# Criação do novo notebook
nb = new_notebook()

# Introdução ao Meta Prompting
nb.cells.append(new_markdown_cell("# Meta Prompting com Modelos de Linguagem"))
nb.cells.append(new_markdown_cell(
    "## O que é Meta Prompting?\n\n"
    "O *Meta Prompting* é uma técnica avançada de prompting que foca nos aspectos estruturais e sintáticos das tarefas, em vez de detalhes específicos do conteúdo. "
    "Segundo [Zhang et al. (2024)](https://arxiv.org/abs/2311.11482), o objetivo do meta prompting é construir uma maneira mais abstrata e estruturada de interagir com modelos de linguagem grande (LLMs), "
    "enfatizando a forma e o padrão das informações sobre métodos tradicionais centrados no conteúdo."
))

# Características principais do Meta Prompting
nb.cells.append(new_markdown_cell(
    "### Características Principais do Meta Prompting\n\n"
    "De acordo com Zhang et al. (2024), as principais características do meta prompting incluem:\n"
    "1. **Orientado para a estrutura**: Prioriza o formato e o padrão dos problemas e soluções em vez de detalhes específicos.\n"
    "2. **Focado em sintaxe**: Usa a sintaxe como um template para a resposta esperada.\n"
    "3. **Exemplos abstratos**: Utiliza exemplos abstratos para ilustrar a estrutura dos problemas, sem focar em detalhes específicos.\n"
    "4. **Versátil**: Aplicável em diversos domínios, capaz de fornecer respostas estruturadas para uma ampla gama de problemas.\n"
    "5. **Abordagem categórica**: Baseia-se na teoria dos tipos para enfatizar a categorização e o arranjo lógico dos componentes em um prompt."
))

# Vantagens do Meta Prompting sobre Few-Shot Prompting
nb.cells.append(new_markdown_cell(
    "### Vantagens do Meta Prompting sobre Few-Shot Prompting\n\n"
    "Zhang et al., 2024, destacam que o meta prompting difere do few-shot prompting por focar em uma abordagem mais orientada à estrutura ao invés de uma abordagem centrada no conteúdo.\n\n"
    "As vantagens do Meta Prompting incluem:\n"
    "1. **Eficiência de tokens**: Reduz o número de tokens necessários ao focar na estrutura, em vez de conteúdo detalhado.\n"
    "2. **Comparação justa**: Proporciona uma abordagem mais justa para comparar diferentes modelos de resolução de problemas ao minimizar a influência de exemplos específicos.\n"
    "3. **Eficiência em zero-shot**: Pode ser visto como uma forma de zero-shot prompting, onde a influência de exemplos específicos é minimizada."
))

# Exemplo prático de Meta Prompting
nb.cells.append(new_markdown_cell(
    "### Exemplo de Meta Prompting com Solução Abstrata\n\n"
    "Vamos demonstrar um exemplo prático de meta prompting para resolver um problema estruturalmente abstrato. "
    "Em vez de fornecer conteúdo específico, o prompt orienta o modelo a seguir uma estrutura geral.\n\n"
    "**Prompt:**\n\n"
    "> Resolva o problema de adicionar números primos. A resposta esperada deve incluir o processo de identificação de primos e o cálculo da soma.\n\n"
    "**Resposta Estruturada Esperada:**\n\n"
    "> Identifique todos os números primos na lista. Some os valores encontrados. Informe o resultado final."
))

# Função de exemplo para Meta Prompting
nb.cells.append(new_code_cell(
    """# Exemplo de Meta Prompting para resolver um problema abstrato
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

chat = ChatOllama(model="llama3")
template_meta = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente que resolve problemas usando uma abordagem estrutural e baseada em sintaxe.'),
    ('human', 'Resolva o problema de adicionar números primos. A resposta deve seguir uma estrutura clara: identificar números primos, somar os valores, e fornecer o resultado final.')
])

def exemplo_meta_prompting():
    resposta = template_meta | chat
    output = resposta.invoke({})
    return output["content"]

# Executar a função de Meta Prompting
resultado_meta_prompting = exemplo_meta_prompting()
print(f"Resultado do exemplo Meta Prompting: {resultado_meta_prompting}")
"""
))

# Aplicações do Meta Prompting
nb.cells.append(new_markdown_cell(
    "## Aplicações do Meta Prompting\n\n"
    "Ao focar nos padrões estruturais da resolução de problemas, o Meta Prompting oferece uma abordagem clara para navegar em tópicos complexos, "
    "melhorando as capacidades de raciocínio dos LLMs em diversos domínios. Aplicações típicas incluem tarefas de raciocínio complexo, problemas matemáticos, desafios de codificação, e questões teóricas.\n\n"
    "Para mais detalhes, consulte o trabalho de Zhang et al. (2024): [Meta Prompting Paper](https://arxiv.org/abs/2311.11482)."
))

# Conclusão
nb.cells.append(new_markdown_cell(
    "## Conclusão\n\n"
    "O Meta Prompting oferece uma maneira eficiente e estruturada de guiar modelos de linguagem em tarefas complexas. "
    "Focando em padrões estruturais e sintáticos, ele reduz a necessidade de exemplos específicos e promove respostas mais generalizadas e aplicáveis. "
    "Essa técnica é especialmente útil em domínios onde a estrutura de resolução de problemas é mais relevante do que o conteúdo específico."
))

# Salvar o notebook
notebook_path = "meta_prompting_notebook.ipynb"
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook criado e salvo como {notebook_path}")
