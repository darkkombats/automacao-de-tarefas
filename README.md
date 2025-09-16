# Automação de Tarefas para Cadastro Web
Este projeto é um programa de automação desenvolvido em Python que realiza o login em um site e cadastra usuários automaticamente com base em uma base de dados. A automação utiliza as bibliotecas **pandas** para manipulação dos dados e **pyautogui** para controlar o navegador e interagir com a interface gráfica.


## 📋 Funcionalidades
- Abre o navegador automaticamente.
- Acessa o site especificado.
- Realiza login com credenciais fornecidas.
- Lê uma base de dados (arquivo CSV, Excel, etc.) contendo os dados para cadastro.
- Preenche os formulários de cadastro no site com os dados da base.
- Executa o processo para todos os registros da base de dados.

## 🛠️ Tecnologias Utilizadas

- Python 3.13
- [pandas](https://pandas.pydata.org/) - para manipulação e leitura da base de dados.
- [pyautogui](https://pyautogui.readthedocs.io/en/latest/) - para automação da interface gráfica e controle do mouse/teclado.
- time (biblioteca nativa) - para controlar os intervalos de execução.

## ⚠️ Avisos Importantes

O uso do pyautogui exige que a tela e o navegador estejam visíveis durante a execução.

Certifique-se de usar intervalos de tempo para evitar bloqueios no site por excesso de requisições rápidas.

Este projeto é para fins educacionais. Não utilize para automatizar ações em sites sem permissão.

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Requisitos

- Python 3 instalado.
- Instalar as bibliotecas necessárias:

```bash
pip install pandas 
pip install pyautogui
