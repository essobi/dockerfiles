FROM ubuntu:16.04  
RUN apt-get update  
RUN echo "Installing curl ..."  
RUN apt-get install -y curl  
RUN echo "Adding dotnet core 2.0.0 sdk repository key ..."  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN echo "Adding repository to sources list ..."  
RUN sh -c 'echo "deb [arch=amd64]
http://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list'  
RUN echo "Updating packages list ..."  
RUN apt-get update  
RUN echo "Installing dotnet core SDK 2.0.0"  
RUN apt-get install -y dotnet-sdk-2.0.0  
RUN apt-get install -y git  
RUN mkdir docker-cloud-app  
WORKDIR docker-cloud-app  
CMD git clone https://shrijit1991@bitbucket.org/shrijit1991/docker-cloud-
app.git . && dotnet restore && dotnet build && dotnet run

