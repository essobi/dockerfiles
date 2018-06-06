FROM ubuntu:16.04  
## Define environmental variables  
ENV DOTNETCORE_VER 2.1.105  
## Install dependencies  
RUN apt-get -y update  
RUN apt-get -y install curl lsb-release  
  
## Update apt sources & install keys  
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/
xenial main" | tee /etc/apt/sources.list.d/azure-cli.list  
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys
52E16F86FEE04B979B07E28DB02C46DF417A0893  
RUN curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list  
  
## Install Azure CLI  
RUN apt-get -y install apt-transport-https  
RUN apt-get -y update && apt-get -y install azure-cli  
  
## Install PowerShell for Linux  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/microsoft.list  
RUN apt-get -y update && apt-get -y install powershell  
  
## Install .NET Core SDK  
RUN apt-get -y install dotnet-sdk-$DOTNETCORE_VER  
  
## Install node.js and npm  
RUN apt-get install -y nodejs npm  
  
## Install Azure PowerShell for .NET Core  
RUN pwsh -Command "& {Install-Module AzureRM.NetCore -Force -Confirm:\$False}"  
  
## Install PowerShell module for Visual Studio Team Services  
RUN pwsh -Command "& {Install-Module VSTeam -Force -Confirm:\$False}"  

