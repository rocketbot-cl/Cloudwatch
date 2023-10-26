# Cloudwatch
  
Módulo para conexão com o AWS Cloudwatch  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Conectar ao AWS  
Este comando permite que você se conecte à sua conta AWS, para isso você precisa do seu Access Key Id e do seu Secret Access Key, você pode obter esses dados no console da AWS, na seção Security Credentials.

2. Criar Grupo de Log  
Este comando permite criar um grupo de log no Cloudwatch. Você deve ter a permissão IAM: "logs: CreateLogGroup"

3. Excluir Grupo de Log  
Este comando permite excluir um grupo de log no Cloudwatch. Você deve ter a permissão IAM: "logs:DescribeLogGroups"

4. Criar Fluxo de Log  
Este comando permite criar um fluxo de log no Cloudwatch. Você deve ter a permissão IAM: "logs:CreateLogStream"

5. Excluir Fluxo de Log  
Este comando permite excluir um fluxo de log no Cloudwatch. Você deve ter a permissão IAM: "logs:DescribeLogStreams".

6. Carregar Eventos de Log  
Este comando permite carregar eventos de log em um fluxo de log no Cloudwatch. Você deve ter permissão IAM: "logs:PutLogEvents".

7. Obter Eventos de Log  
Este comando permite obter eventos de um fluxo de log em Cloudwatch. Você deve ter permissão IAM: "logs:GetLogEvents".  




----
### OS

- windows
- mac
- docker

### Dependencies
- [**boto3**](https://pypi.org/project/boto3/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)