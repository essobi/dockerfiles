FROM daocloud.io/ubuntu:16.04  
# RUN sed -i 's/archive.ubuntu.com/cn.archive.ubuntu.com/g'
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install software-properties-common curl -y  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update  
RUN apt-get install gcc g++ nodejs fp-compiler python3 python3-psutil
openjdk-8-jdk mono-4.0 mono-mcs -y  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-get update  
RUN apt-get install dotnet-sdk-2.0.0 -y  

