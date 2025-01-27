![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/brunombs)
[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/brunombs?tab=repositories)

[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Python Mini Projetos <img src="https://i.pinimg.com/originals/d8/5d/f0/d85df08df1212c0f8b219e779c5ebc46.gif" align="right" width="120" />

 > Uma coleção de pequenos e fáceis projetos em Python para ajudar você a melhorar suas habilidades de programar.

![Issues](https://img.shields.io/github/issues/ndleah/python-mini-project?style=social&logo=github)
![Pull Requests](https://img.shields.io/github/issues-pr/ndleah/python-mini-project?style=social&logo=github)
![Forks](https://img.shields.io/github/forks/ndleah/python-mini-project?style=social&logo=github)
![Stars](https://img.shields.io/github/stars/ndleah/python-mini-project?style=social&logo=github)
[![License](https://img.shields.io/github/license/ndleah/python-mini-project?style=social&logo=github)](https://github.com/ndleah/python-mini-project/blob/main/LICENSE)

<!-- omit in toc -->
## Tabela de conteúdo
  - [Objetivo do projeto](#-objetivo-do-projeto)
  - [Contribuindo](#-contribuindo)
  - [README Modelo para os scripts](#-readme-modelo-para-os-scripts)
  - [Projetos](#-projetos)
  - [Feedback](#-feedback)

## ![image](IMG/aiming.svg) Objetivo do projeto

Como um iniciante em Python, eu compreendo os problemas que as pessoas enfrentam quando começam a estudar e tentar entender vários conceitos de Data Science, particularmente Python. Este projeto foi desenvolvido para pessoas que estão apenas começando com os princípios do Python e explorando o GitHub como "colaboradores".

Meu objetivo é construir um playground comum onde todos, de iniciantes a especialistas, possam aprender e compartilhar conhecimento, e espero que você aproveite sua estadia aqui!

Vamos criar coisas incríveis juntos! 👉

## ![image](IMG/game-ps.svg) Contribuindo 

<details>
<summary>
Passo 1: Dê uma estrela no repositório (Star)
</summary>

Clique na estrela no repositório pressionando o botão superior direito para iniciar sua jornada maravilhosa

![star repo](https://docs.github.com/assets/images/help/stars/starring-a-repository.png)

</details>

---

<details>
<summary>
Passo 2: Faça um fork
</summary>

Na página do GitHub deste repositório (https://github.com/brunombs/mini-projetos-python) clique no botão "**Fork**".
 
![fork image](https://www.earthdatascience.org/images/earth-analytics/git-version-control/githubguides-bootcamp-fork.png)

</details>

---

<details>
<summary>
Step 3: Clone o projeto
</summary>

* **Método 1:** GitHub Desktop

> ⚠️ **OBSERVAÇÃO:** Se você não estiver familiarizado com o Git, usar o **GitHub Desktop** é um melhor começo. Se você escolher este método, certifique-se de baixá-lo antes de continuar a leitura.
> 
> ❗❗ Acesse o link para fazer o download [**aqui**](https://desktop.github.com).

Saiba mais sobre como clonar o repositório remoto em sua máquina local usando o **GitHub Desktop** [aqui](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository).

* **Método 2:** Git

Clone o repositório que fez o fork. Abra o git bash e digite:

```bash
git clone https://github.com/<seu-user-github>/mini-projetos-python.git
```

> Isso faz uma cópia local do repositório em seu computador.
> 
⚠️ **Substituir \<seu-user-github\>!**

Saiba mais sobre isso [forking](https://docs.github.com/pt/get-started/quickstart/fork-a-repo).

</details>

---

<details>
<summary>
Step 4: Crie sua própria branch
</summary>

Sempre mantenha sua cópia local do repositório atualizada com o repositório original.
Antes de fazer qualquer alteração e/ou em um intervalo apropriado, siga os seguintes passos:
 
* **Método 1:** GitHub Desktop

Saiba mais sobre como criar sua nova branch [aqui]([https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/managing-branches#creating-a-branch](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)) e como buscar e puxar a origem de/para sua máquina local (fetch and pull) [aqui](https://docs.github.com/pt/desktop/contributing-and-collaborating-using-github-desktop/keeping-your-local-repository-in-sync-with-github/syncing-your-branch).

Saiba mais sobre como buscar (fetch) e puxar (pull) a origem de/para sua máquina local usando **GitHub Desktop** [aqui](https://docs.github.com/pt/desktop/contributing-and-collaborating-using-github-desktop/keeping-your-local-repository-in-sync-with-github/syncing-your-branch).

* **Método 2:** Git

Execute os seguintes comandos ***com cuidado*** para atualizar seu repositório local

```sh
# Se você clonou há algum tempo, obtenha as últimas alterações do upstream
git checkout <master>
git pull upstream <master>

# Faça uma ramificação (branch) de recurso (sempre verifique se sua ramificação (branch) atual está atualizada antes de criar uma nova ramificação para evitar conflitos de mesclagem (merge))
git checkout -b <branch-name>

#
```
</details>

---
<details>
<summary>
Step 6: Preparar, Apontar, Começar...
</summary>

Depois de concluir essas etapas, você estará pronto para começar a contribuir com o projeto e criar **pull requests**.
 
- Crie uma pasta dentro do:
  [diretório do projeto](https://github.com/brunombs/mini-projetos-python) de acordo com o nome do seu projeto.
> O nome da pasta deve ter o seguinte formato "Nome_do_seu_projeto_aqui". Por exemplo: Simulador_de_dado
- Escreva seu código e adicione à respectiva pasta no diretório de projetos, localmente.
- Não esqueça de adicionar um `README.md` em sua pasta, de acordo com o
   [MODELO_README.](https://github.com/Python-World/python-mini-projects/blob/master/README_TEMPLATE.md)

* **Método 1:** GitHub Desktop

Saiba mais como fazer pull request de sua máquina local usando o **GitHub Desktop** para o repositório principal[aqui](https://docs.github.com/pt/desktop/contributing-and-collaborating-using-github-desktop/working-with-your-remote-repository-on-github-or-github-enterprise/viewing-a-pull-request-in-github-desktop).

* **Método 2:** Git

Adicione as alterações usando os comandos `git add`, `git commit`:

```bash
git add -A
git commit -m "<sua mensagem>"
```

Envie o código *para o seu repositório*.

```bash
git push origin <nome-da-branch>
```
</details>

---

<details>
<summary>
Step 7: Pull Request
</summary>

Vá para a página do GitHub de seu_fork_ e **faça um pull request**:

![pull request image](https://docs.github.com/assets/cb-26223/images/help/pull_requests/pullrequest-send.png)

Leia mais sobre pull requests na [página de ajuda do GitHub](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

Agora espere, até que *seu Pull Request* seja aprovado! Se houver algum conflito, você receberá uma notificação.

</details>

<br>

## ![image](IMG/bookmark.svg) README Modelo para os scripts

por favor, certifique-se de adicionar um arquivo `README.md` que siga a mesma construção deste modelo para consistência.

[Modelo README](https://github.com/brunombs/mini-projetos-python/blob/main/README_TEMPLATE.md)

## ![image](IMG/like.svg) Projetos 

SR No   | Projeto | Descrição | Autor  
--- | --- | --- | --- | 
1 | [Simulador de rolamento de dados](https://github.com/brunombs/mini-projetos-python/tree/main/Dice_Rolling_Stimulator) |Este é um simulador de dados simples feito usando Python. | [Leah Nguyen](https://github.com/ndleah)
2 | [Dicionário](https://github.com/ndleah/python-mini-project/tree/main/Dictionary)| Um simulador de dicionário do Python no qual você pode inserir qualquer palavra e obterá a definição dela como saída. | [Leah Nguyen](https://github.com/ndleah)
3 | [Jogo da forca](https://github.com/ndleah/python-mini-project/tree/main/Hangman_Game) |Um simulador de jogo da forca usando Python no qual o jogador tem 10 tentativas para adivinhar a frase antes que o homem seja enforcado. | [Leah Nguyen](https://github.com/ndleah)
4 | [Jogo da velha](https://github.com/ndleah/python-mini-project/tree/main/Tic_Tac_Toe) |Um simples jogo da velha feito em Python. | [Leah Nguyen](https://github.com/ndleah)
5 | [Plotador](https://github.com/ndleah/python-mini-project/tree/main/Plotter) |Um programa de automação para plotar dados com diferentes visualizações por seleções do usuário. | [Leah Nguyen](https://github.com/ndleah)
6 | [Plotagem eográfica usando Folium](https://github.com/ndleah/python-mini-project/tree/main/Geo_Plot_Using_Folium) | Usando a biblioteca Folium para criar diferentes visualizações de dados de mapas. | [Leah Nguyen](https://github.com/ndleah)
7 | [Jogo da lagarta](https://github.com/ndleah/python-mini-project/tree/main/Caterpillar_Game) | Um simples jogo da lagarga desenvolvido em Python. | [Leah Nguyen](https://github.com/ndleah)
8 | [Jogo da memória](https://github.com/ndleah/python-mini-project/tree/main/Matchmaker) | Um simples jogo da memória feito em Python. | [Leah Nguyen](https://github.com/ndleah)
9 | [Calculadora inteligente](https://github.com/ndleah/python-mini-project/tree/main/Smart_Calculator) | Uma calculadora inteligente usada para questões básicas de matemática criada em Python.| [Leah Nguyen](https://github.com/ndleah)
10 | [Tela pet](https://github.com/ndleah/python-mini-project/tree/main/Screenpet) | Uma tela pet fofa com reações diferentes ao interagir na área de trabalho. | [Leah Nguyen](https://github.com/ndleah)
11 | [Apanhador de Ovos](https://github.com/ndleah/python-mini-project/tree/main/Egg_Catcher) | Jogo de pegar ovos feito em Python.| [Leah Nguyen](https://github.com/ndleah)
12 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Number%20Guessing">Adivinhar número | Jogo de adivinhar número | [Shruti Solani](https://github.com/ShrutiSolani)
13 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Madlibs">Biblioteca desorganizada | Jogo da biblioteca desorganizada | [Shruti Solani](https://github.com/ShrutiSolani)
14 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Caesar_Cipher">Cifra de César | Encriptador e decodificador simples Caesar Cipher feito com python | [FH089](https://github.com/FH089)
15 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Email%20Slicer">Fatiador de email | Fatiador de email em Python | [Shruti Solani](https://github.com/ShrutiSolani)
16 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Speaking_Dictionary">Dicionário falado | Programa Python que permite ao usuário encontrar o significado de uma palavra em inglês falando diretamente para o dispositivo | [19lyaejin](https://github.com/19lyaejin)
17 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Cat_command">Comando do gato | Este projeto é uma implementação básica do comando linux cat | [Alexander Monterrosa](https://github.com/Alex108-lab)
18 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Sqlite-crud">Sqlite-crud | Um simples crud implementado em python usando sqlite. | [Alexander Monterrosa](https://github.com/Alex108-lab)
19 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Binary_tree">Árvore binária | Implementação de uma árvore binária em python | [Alexander Monterrosa](https://github.com/Alex108-lab)
20 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Socket_example">Socket | Implementação de um socket em python | [Alexander Monterrosa](https://github.com/Alex108-lab)
21 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Stack_structure">Estrutura da pilha |  Implementação de uma estrutura de pilha em python | [Alexander Monterrosa](https://github.com/Alex108-lab)
22 | <a href="https://github.com/brunombs/mini-projetos-python/tree/main/Math_Game">Jogo de matemática | É apenas um jogo de matemática simples. Melhore suas habilidades matemáticas | [Pargorn Ruasijan (xNewz)](https://github.com/xNewz)
23 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Password%20Generator">Gerador de senhas |  Crie senhas seguras impossíveis de decifrar. | [Pargorn Ruasijan (xNewz)](https://github.com/xNewz)
24 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Demerge_pdfs">Desmembrar PDF |  Programa Python para converter um arquivo pdf grande em vários arquivos pdf de tamanhos diferentes sem qualquer alteração no arquivo grande. | [Darpan-Balar](https://github.com/Darpan-Balar)
25 | <a href="https://github.com/vivekthedev/python-mini-project/tree/main/QR%20Code%20Genrator">Gerador de QR Code |  GUI com Tkinter para converter texto em um QR Code PNG. | [Vivek Kumar Singh](https://github.com/vivekthedev)
26 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Crud_in_flask">Flask Crud |  Crud usando flask and sqlite3 | [Alexander Monterrosa](https://github.com/Alex108-lab)
27 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Sudoku_solver">Solucionador Sudoku|  Este programa pode gerar e resolver o jogo Sudoku.| [Dominik Meurer](https://github.com/DMeurer)
28 | <a href="https://github.com/ndleah/python-mini-project/tree/main/QR%20Code%20Genrator">Confere email | Confere email é um script em python que permite que você leia seus assuntos do Gmail de contas específicas do Gmail diretamente do terminal sem precisar fazer login todas as vezes! | [Siddharth Pradeep](https://github.com/thirt33n)
29 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Whatsapp_Bot">Whatsapp Bot |  Whatsapp Bot é um bot simples feito em Python para mandar mensagem pelo whatsapp| [Anish Lohiya](https://github.com/AnishLohiya)
30 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Youtube_video_download">YouTube Video Downloader |  YouTube Video Downloader te permite baixar vídeos do youtube. | [Alexander Monterrosa](https://github.com/Alex108-lab)
31 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Face_Recognition">Reconhecimento facial|  Um projeto de reconhecimento de rosto desenvolvido usando o módulo OpenCV em Python que exibe um quadro de retângulo azul ao redor de rostos. | [Anish Lohiya](https://github.com/AnishLohiya) 
32 | <a href="https://github.com/vivekthedev/python-mini-project/tree/main/Slideshare%20to%20PDF">Slideshare para PDF |  Baixe qualquer apresentação do slideshare para um PDF sem qualquer inscrição ou login | [Vivek](https://github.com/vivekthedev)
33 | <a href="https://github.com/ndleah/python-mini-project/tree/main/Rock_Paper_Scissors_Spock">Pedra Papel Tesoura Spock | Pedra Papel Tesoura Spock tem etapas extras que adicionam um pouco de tempero e criatividade ao jogo genérico Pedra Papel Tesoura que todos conhecemos e amamos. O jogador pode escolher entre Pedra, Papel, Tesoura, Lagarto ou Spock. Se eles escolherem corretamente, então o jogador ganha. Divirta-se e boa sorte! | [Anokh1](https://github.com/Anokh1)
 
 
 ## ![image](IMG/like.svg) Nossos contribuidores
 
<a href="https://github.com/ndleah/python-mini-project/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ndleah/python-mini-project" />
</a>

 
 ## ![image](IMG/muscle.svg) Feedback

Se você tiver algum comentário ou ideia para melhorar este projeto, sinta-se à vontade para entrar em contato comigo via

<a href="https://www.linkedin.com/in/ndleah/">
  <img align="left" alt="Reeha's Linkdein" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />

</a>
<a href="https://github.com/ndleah">
  <img align="left" alt="Reeha's Github" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>
