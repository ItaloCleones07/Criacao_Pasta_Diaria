import datetime
import os
import ctypes

agora = datetime.datetime.now()
pasta_mes = f"MES {agora.month:02d}"
pasta_dia = f"{agora.day:02d}.{agora.month:02d}.{agora.year}"

pasta_raiz = r"C:\Users\italo\OneDrive\Documentos\Projetos\Criacao_Pasta"
caminho_final = os.path.join(pasta_raiz, str(agora.year), pasta_mes, pasta_dia)

try:
    if os.path.exists(caminho_final):
        ctypes.windll.user32.MessageBoxW(0, f"Pasta já existe!", "Informação", 64)
    else:
        ctypes.windll.user32.MessageBoxW(0, f"Pasta Criadas!", "Informação", 64)
        os.makedirs(caminho_final, exist_ok=True)
except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, f"Erro: {e}", "ERRO", 16)