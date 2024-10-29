# Inicializa um repositório Git
git init

# Adiciona o diretório atual como seguro para evitar avisos de propriedade
git config --global --add safe.directory 'E:/Executavel Touch/Rotina de Testes Integrada/TestecomDiretorioeFrontV6.0'

# Adiciona todos os arquivos ao índice do Git
git add .

# Faz um commit inicial
git commit -m "Commit inicial: configuração do repositório"

# Adiciona o repositório remoto
git remote add origin https://github.com/WigoWigo10/Testes-Integrados-Prometheus.git

# Faz o push do commit inicial para o repositório remoto
git push -u origin master

# -------------------------------------
# A partir daqui, são os passos para atualizações de arquivos:

# Após fazer alterações em arquivos ou adicionar novos arquivos, execute os seguintes passos:

# Adiciona todos os arquivos modificados ao índice do Git
git add .

# Adicionar arquivos individualmente
git add arquivo1.txt arquivo2.txt arquivo3.txt

# Adicionar um diretório específico
git add nome-do-diretorio/

# Adicionar arquivos por padrão (padrão de nome ou extensão)
git add *.txt

# Faz um commit com uma mensagem descritiva
git commit -m "Descrição das alterações realizadas"

# Faz o push das alterações para o repositório remoto
git push origin master
