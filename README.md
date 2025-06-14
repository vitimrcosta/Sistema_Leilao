# 🕹️ Sistema de Leilões

Este é um projeto de sistema de controle de leilões, desenvolvido como parte de um trabalho acadêmico. O objetivo principal é implementar as funcionalidades de cadastro e controle de leilões, com **testes unitários cobrindo 100% do código**.

---

## 📌 Funcionalidades Implementadas

- ✅ Cadastro de participantes com validação de CPF e e-mail
- ✅ Cadastro de leilões com nome, lance mínimo, data de início e término
- ✅ Controle de estados do leilão: `INATIVO`, `ABERTO`, `FINALIZADO`, `EXPIRADO`
- ✅ Regras de transição entre estados validadas via exceções
- ✅ Adição de lances respeitando o valor mínimo
- ✅ Filtro de leilões por estado e período
- ✅ Envio automático ao vencedor do leilão
- ✅ Configuração via SMTP do Gmail
- ✅ Tratamento de erros de conexão
- ✅ Uso de senhas de app para serviços Google
- ✅ Remoção de participantes apenas se não houverem lances associados
- ✅ Testes unitários com cobertura total
---

## 🗂️ Estrutura do Projeto

```
Sistema de Leilões
├── Leilão
│   ├── Estados: INATIVO, ABERTO, FINALIZADO, EXPIRADO
│   ├── Lances (ordem crescente)
│   └── Métodos: abrir(), finalizar(), identificar_vencedor()
│
├── Participante
│   ├── Validações: CPF, e-mail
│   └── Restrição: não pode ser removido se tiver lances
│
└── Gerenciador
    ├── Filtros: por estado, data
    └── Controle: participantes e leilões
```

## 🧪 Testes

Os testes foram escritos com [Pytest](https://docs.pytest.org/) e cobrem os seguintes cenários:

- Validação de CPF e e-mail de participantes
- Criação de leilão com estado `INATIVO`
- Abertura e encerramento de leilões de acordo com regras de data
- Registro de lances válidos e rejeição de lances abaixo do mínimo
- Listagem de leilões por estado e por intervalo de datas
- Proibição de remoção de participantes com lances existentes
- Envio simulado de e-mail e verificação de saída via `capsys`

### 🔧 Rodando os testes

1. Ative seu ambiente virtual (fora da pasta do projeto):
   ```bash
   python -m venv venv         # Cria o ambiente virtual
   venv\Scripts\activate       # Ativa no Windows
   
2. Instalar as bibliotecas
   ```bash
   pip install pytest
   pip install python-dotenv pytest

3. Comandos do pytest para rodar o programa
   ```bash
   pytest -v                                      # Executa todos os testes com mais detalhes
   pytest tests/nome_do_arquivo.py -v             # Executa os testes de um arquivo específico
   pytest tests/nome_do_arquivo.py::test_funcao   # Executa uma função de teste específica
   pytest --cov=models --cov-report=term-missing  # Executa os testes com relatório de cobertura

## 📎 Requisitos

- Python 3.10+

- Crie um arquivo .env na raiz do projeto
 
   ```bash
   EMAIL_USER=seuemail@gmail.com
   EMAIL_PASSWORD=sua_senha_de_app

## 🎓 Objetivo Acadêmico

Este sistema foi desenvolvido com o propósito de aplicar e demonstrar:

- Princípios de programação orientada a objetos
- Tratamento de exceções
- Boas práticas com testes unitários automatizados
- Separação de responsabilidades entre entidades, serviços e regras de negócio

## 👨‍💻 Autor

Desenvolvido por Victor, Roberta, Luiz.
Para dúvidas ou sugestões, envie um e-mail para victor.rcosta@outlook.com.

