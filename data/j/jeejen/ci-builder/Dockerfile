FROM jeejen/jdk  
  
RUN apt-get update && \  
apt-get -y install \  
ansible \  
docker.io \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
\  
$(lsb_release -cs) \  
stable" && \  
apt-get update && \  
apt-get -y install docker-ce && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean all  

