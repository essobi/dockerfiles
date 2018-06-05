FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg2
software-properties-common wget  
  
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/
wheezy main" | \  
tee /etc/apt/sources.list.d/azure-cli.list  
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 417A0893  
  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update && apt-get install -y gettext azure-cli docker-ce jq  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/v1.7.12/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl  

