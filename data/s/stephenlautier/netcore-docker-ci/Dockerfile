FROM microsoft/aspnetcore-build:1.0-1.1  
RUN apt-get update  
RUN apt-get install apt-transport-https ca-certificates curl gnupg2 software-
properties-common -y  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update  
RUN apt-get install docker-ce -y  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
RUN curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN sudo chmod +x /usr/local/bin/docker-compose

