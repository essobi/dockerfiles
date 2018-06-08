FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y \  
mysql-client \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common  
  
# dotnet core repo  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893  
  
# install dotnet  
RUN apt-get update  
RUN apt-get install -y dotnet-dev-1.0.0-preview2-003156  

