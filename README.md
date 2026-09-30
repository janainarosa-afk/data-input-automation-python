# data-input-automation-python
Robô de automação de processos (RPA) desenvolvido em Python com PyAutoGUI e Pandas para inserção em massa de dados cadastrais. Inclui lógica de resiliência e persistência de estado (checkpointing) para retomada pós-falhas.
# Automação de Inserção de Dados Resiliente com Python

Este projeto consiste em um script de Automação de Processos (RPA) desenvolvido em **Python** para resolver uma dor clássica de negócios: o cadastro massivo e manual de dados em sistemas legados (ERPs/Web).

# Contexto de Negócio & Problema
Tarefas manuais de digitação de planilhas para sistemas internos geram gargalos de tempo, retrabalho e erros operacionais. O objetivo deste robô é simular a ação humana para alimentar dados de produtos com velocidade, liberando o time operacional para tarefas analíticas.

# Arquitetura e Diferenciais Técnicos
Ao contrário de scripts de automação simples, este projeto foi desenhado focando em **resiliência e consistência de dados**:

*   **Persistência de Estado (Checkpointing):** Se a automação for interrompida por instabilidade de rede ou ação do usuário, o script gera o arquivo `produtos_restantes.csv`. Ao reiniciar, o robô lê este arquivo e **retoma exatamente de onde parou**, evitando duplicidade de cadastros no banco de dados.
*   **Manipulação de Dados com Pandas:** Utilização da biblioteca Pandas para leitura e partição da carga de dados (`DataFrames`).
*   **Feedback Visual:** Integração com `tqdm` para exibir a barra de progresso do processamento em lote via terminal.
*   **Mecanismo de Segurança:** Ativação do `pyautogui.FAILSAFE` para interrupção imediata da execução caso o operador mova o mouse para os cantos da tela.

## Tecnologias Utilizadas
*   Python 3
*   Pandas (Manipulação e estruturação de tabelas)
*   PyAutoGUI (Automação de interface e simulação de periféricos)
*   Tqdm (Barra de progresso e métricas de tempo de execução)

## Como Executar
1. Instale as dependências:
   ```bash
   pip install pyautogui pandas tqdm
   ```
2. Certifique-se de ter um arquivo `produtos.csv` na raiz do projeto com as colunas de dados.
3. Execute o script principal:
   ```bash
   python nome_do_seu_script.py
   ```
