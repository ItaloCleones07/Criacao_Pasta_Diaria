# 📁 Criador Automático de Pastas

Automação desenvolvida em Python para criação e organização de diretórios por data, utilizando uma estrutura padronizada de ano, mês e dia. O projeto tem como objetivo simplificar tarefas repetitivas e otimizar a organização de arquivos.

## Funcionalidades

- Criação automática de pastas com base na data atual.
- Organização hierárquica por ano, mês e dia.
- Verificação de diretórios existentes.
- Notificações de status por caixas de diálogo do Windows.
- Tratamento de exceções durante a execução.

## Tecnologias

- **Python 3**
- `datetime` — obtenção da data atual.
- `os` — manipulação de caminhos e diretórios.
- `ctypes` — exibição de mensagens nativas do Windows.

## Estrutura de diretórios

```text
Criacao_Pasta/
└── AAAA/
    └── MES MM/
        └── DD.MM.AAAA/
```

## Como executar

1. Instale o Python 3.
2. Configure o diretório de destino na variável `pasta_raiz`.
3. Execute o script pelo terminal:

```bash
python criar_pasta.py
```

## Requisitos

- Windows 10 ou superior.
- Python 3 instalado.
- Permissão de escrita no diretório de destino.
