FROM google/cloud-sdk:latest  
  
RUN apt-get update  
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg2
software-properties-common wget  
  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update && apt-get install -y gettext docker-ce  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get
> get_helm.sh && \  
chmod 700 get_helm.sh && \  
./get_helm.sh

