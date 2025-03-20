COMO USAR GIT E GITHUB

Git bash here
    Terminal de comando utilizado para utilizar git

- Caracteristicas git bash here
    - o texto em amarelo mostra a pasta que está sendo configurado
    - ela pode ser usada como terminal de comando como power shell, mas o power shell e outros terminais de comando não tem integração com o git
    - toda vez que vai utilizar algum comando que mexe com versionamento informar "git" e depois o próximo comando

- Comandos
    * git config
        - local de armazenamento
            - --global = configura para todo o usuário
            - --system = configura para todo o sistema operacional
            - --local  = configura somente a pasta local

            - user.name  = mostra o nome do usuário que fazer o commit
            - user.email = mostra o email cadastrado que fazer o commit
            - se informar alguma informação correspondente após esses dois comandos, ela vai ser substituida
        
        - git config init.defaultBranch
            Informa o nome do branch que está utilizando

            - git config --global init.defaultBranch main = altera o nome do branch inicial para os futuros gits que forem criados para "main"

        - git config --global --list
            Informa todas as configurações feitas em todo o usuário em relação a git inicial

        - git config --global --show-origin nome_da_informação
            Informa o local onde as alterações estão sendo salvas
    
    * git clone
        - copia códigos salvas dentro de alguma plataforma de versionamento para a pasta onde o git está informando
            - para códigos abertos não tem problemas
            - mas códigos fechados precisam utilizar tokens ou fazer cópia a partir de método SSD
                - criando token
                    - configurações -> settings -> developer settings -> personal access tokens -> tokens -> generete new token -> classic
                        - descrever o motivo da utilização do token
                        - informar a data de inspiração do token
                        - informar a limitação que esse token libera 
                        - generete token
                        - copiar o código que foi gerado (a chave vai estar disponível somente depois de dar generete token, não tem mais nenhuma instância que permite recuperar o token gerado)(o token vai se tornar a senha para clonar o código)

                - criando SSH
                    - configurações -> settings -> SSH and GPG keys -> new SSH key
                    - verificar se já existe chave SSH
                        código terminal: ls -a ~/.ssh
                        - se existir, arquivo .pub -> chave pública

                    - criando chave SSH
                        ssh-keygen -t ed25519 -C "endereço_email_github"
                        informar o local que será salva a chave SSH (só dá enter que será tudo salva no mesmo local)
                        criar uma palavra chave 

                        -armazenar a chave SSH de forma segura
                            código: eval " $(ssh-agent -s)"
                        
                        - adicionando a chave privada SSH
                            código: ssh-add ~/.ssh/id_ed25519
                            - informar a palavra chave
                        
                        - configurações -> settings -> SSH and GPG keys -> new SSH key
                        - preencher:
                            - title
                            - key tipe: authentication key
                            - key: informar a chave

                            - como recuperar a chave
                                1. cd ~/.ssh
                                2. ls arquivo.pub
                                3. cat arquivo.pub
                        
                        - para clonar:
                            - código no github -> clicar no code -> SSH
                            - copiar o código
                            - no terminal: git clone colar o código
                            - informar a palavra chave

                salvar o usuário para não precisar informar mais dados de acesso login e senha
                    - git config --global credential.helper cache -> temporário
                    - git config --global credential.helper store -> permanentemente

                    - git config --global credential.helper -> informa qual crédencial está salva

        - se informar um nome depois do endereço do código copiado, o nome da pasta onde o repositório que será clonado vai ser alterado

        - se quiser clonar somente os arquivos de branch específico
            git clone URL --branch branch_a_clonar --single-branch
            * se não informar branch_a_clonar --single-branch, vai ser clonado somente o branch main

    * git init
        inicializa um nova repositório na máquina

        - .git (pasta invisível)
            pasta com as configurações para vinculação com git
            se informar "ls" após acessar a pasta, mostra os arquivos que estão dentro da pasta .git

        - para desfazer o git init
            rm -rf .git

    * git remote -V
        informa os repositórios que já estão vinculados

    * git add nome_arquivo (ou git add . para importar todos os arquivos dentro da pasta)
        colocar na fila o arquivo alterado para ser vinculado com o repositório

        - adiciona somente arquivos e pastas com arquivos dentro
        - adiciona pasta vazia somente se possuir arquivo .gitkeep, pois a pasta pode ter sido criada vazia com algum objetivo

    * git log
        informa os arquivos que estão sendo encaminhadas para a fila e também algumas informações especificas para os comandos feitas para antes de serem comitadas

    * git restore nome_arquivo
        permite recuperar o arquivo que foi excluido ou alterado

    * git commit -m "mensagem informada sobre o motivo do commit"
        empacota os arquivos que estão na fila para serem enviadas para o repositório

        - se quiser alterar a mensagem do commit
            git commit --amend -m "mensagem alterada"

            git commit --amend
            - vai abrir um nova janela, onde está editavel
            - após alterar a mensagem, discar Esc -> : -> W

    * git reset
        retorna os arquivos dentro do commit para status antes de ser commitado
        
        --soft codigo_commit = desfaz somente o commit informado
        --mixed (ou nada) = desfaz os commits posteriores ao que foi indicado
        -- hard = apaga todos os arquivos salvas no commit salva

    * git reflog
        informa o histórico de commits que foram realizadas

    * git remote add origin (endereço do repositório) (somente para primeira vinculação com o repositório)
        cria um novo repositório remoto

    * git push -u origin main (somente para primeira vinculação com o repositório)
        encaminha pela primeira vez os arquivos codados para o repositório

    * git push origin main
        encaminha os arquivos commitados para o repositório vinculado no Github

    * git status
        é a área de preparação, informa todos os arquivos que foram agrupadas para serem enviados para github

    * git pull
        puxa as alterações feitas em todos os arquivos no repositório do github para o repositório local

        - git pull upstream main
            atualiza o código puxado de um git clone

    * git checkout -b novo_branch
        cria um novo branch
        criada para não sobrecarregar e deixar confuso a linha de tempo das alterações feitas por todos os colaboradores do projeto
        depois que o projeto no novo branch estiver certo, faz um merge com o branch main, para atualizar o projeto que estava salva no branch main com o projeto que foi alterado com o novo_branch

        * git checkout branch
            altera para branch existente

    * git branch
        mostra os branchs existentes no repositorio
        
        - git branch -v
            observa os ultimos commits de cada branch

        - git branch -d branch_a_ser_excluido
            exclui o branch selecionado

    * git merge branch_que_sera_fundida_com_o_branch_atual
        pega o branch atual e o branch que foi chamada para complementar o código e arquivos para complementarem o branch atual

    * git fetch
        baixa as alterações salvas no repositório github, porém não mescla com os arquivos do repositório local

    * git diff main origin/main
        observa a diferença dos arquivos do repositório local com o repositório github

        - assim que quiser fazer o merge
            git merge main origin/main

    * git stash
        arquivo as alterações feitas no arquivo dentro de um branch

        - git stash list
            mostra as alterações arquivadas

        - git stash pop
            devolve as alterações arquivadas e exclui a ultima alteração depois de arquivar as alterações do branch

- Atalhos git bash here
    Ctrl + L = limpar o terminal            


GITHUB
    Plataforma de versionamento do git



UTILIDADES TERMINAL DE COMANDO 
- cat nome_arquivo
    abre o arquivo no terminal de comando se arquivo e o terminal tiverem compatibilidade

- ls
    listar os arquivos

    -a 
        exiba todos os arquivos

- cd nome_pasta/
    altera a pasta que está utilizando no terminal git

    - cd..
        volta uma pasta pra trás

- mkdir nome_pasta
    cria nova pasta

- touch arquivo.tipo_de_arquivo
    cria um novo arquivo com a extensão informada, como .md, .py, .html, ...

- echo informação > .arquivo_editavel
    insere dentro de um arquivo editavel alguma informação

    - echo > .arquivo_editavel
        apaga todas as informações dentro do arquivo editavel

- rm
    apaga o arquivo ou pasta selecionada

    - -rf apaga a força o arquivo