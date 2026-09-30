# Automação para Cadastro de Produtos (RPA)
# Dependências: pip install pyautogui pandas tqdm

import os
import subprocess
import time
import pyautogui
import pandas
from tqdm import tqdm

# Configurações de segurança e velocidade do PyAutoGUI
pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 0.5 

ARQUIVO_PROGRESSO = "produtos_restantes.csv"


# 1. CONTROLE DE FLUXO E RESILIÊNCIA (CHECKPOINT)


# Se já existe o arquivo de progresso, retoma dele. Caso contrário, inicia do zero.
if os.path.exists(ARQUIVO_PROGRESSO):
    tabela = pandas.read_csv(ARQUIVO_PROGRESSO)
    print("[INFO] Retomando cadastro de onde parou...")
else:
    tabela = pandas.read_csv("produtos.csv")
    print("[INFO] Iniciando novo cadastro do zero.")

quantidade_produtos = len(tabela)

if quantidade_produtos == 0:
    pyautogui.alert(text="Todos os produtos já foram cadastrados!", title="Fim")
    if os.path.exists(ARQUIVO_PROGRESSO):
        os.remove(ARQUIVO_PROGRESSO)
    exit()

# Alerta visual de início para o operador
pyautogui.alert(
    text=f"Automação Pronta!\n\nProdutos a cadastrar nesta sessão: {quantidade_produtos}.\n\nClique em OK para o robô abrir o navegador e começar.", 
    title="Robô de Cadastro"
)

# 2. INICIALIZAÇÃO DO NAVEGADOR E LOGIN


perfil_desejado = "--profile-directory=Profile 1"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Abre o navegador com o perfil específico caso tenha mais de uma conta 
subprocess.Popen([chrome_path, perfil_desejado])
time.sleep(3)

# Navega até o sistema da empresa
pyautogui.hotkey("ctrl", "l")
time.sleep(0.5) 
pyautogui.write("https://...com")
pyautogui.press("enter")
time.sleep(3)

# Executa o fluxo de autenticação (Substitua pelos seus dados locais com segurança)
pyautogui.press("tab")
time.sleep(0.2)
pyautogui.write("seu_email@exemplo.com") 
pyautogui.press("tab")
time.sleep(0.2)
pyautogui.write("sua_senha_aqui")
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.press("enter") #repete se seu navegador estiver configurado para clique duplo
time.sleep(4)

pyautogui.press("esc")
time.sleep(0.5)


# 3. LOOP DE CADASTRO COM PERSISTÊNCIA EM TEMPO REAL


indices_para_remover = []

for linha in tqdm(tabela.index, desc="Progresso do Cadastro", total=quantidade_produtos):
    # Clica no primeiro campo do formulário (Coordenadas locais da tela)
    pyautogui.click(x=682, y=301)
    
    # Extração e digitação dos dados armazenados no DataFrame do Pandas
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    
    # Envia o formulário
    pyautogui.press("enter")

    # Mecanismo de Resiliência: Atualiza a planilha de checkpoint em disco a cada iteração
    tabela_atualizada = tabela.drop(tabela.index[0:len(indices_para_remover) + 1])
    tabela_atualizada.to_csv(ARQUIVO_PROGRESSO, index=False)
    indices_para_remover.append(linha)

    # Retorna o scroll para o topo da página para a próxima inserção
    time.sleep(0.5)
    pyautogui.scroll(5000)
    time.sleep(0.5)

# Se o lote foi concluído sem interrupções, remove o arquivo de checkpoint
if os.path.exists(ARQUIVO_PROGRESSO):
    os.remove(ARQUIVO_PROGRESSO)

pyautogui.alert(
    text="Sucesso!\n\nO processamento acabou e todos os produtos foram inseridos com sucesso.", 
    title="Cadastro Finalizado"
)
