FROM ubuntu:16.04  
# set debian frontend to noninteractive mode.  
RUN export DEBIAN_FRONTEND=noninteractive  
  
RUN apt update && apt install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
  
RUN apt update && apt install -y \  
docker-ce  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  

