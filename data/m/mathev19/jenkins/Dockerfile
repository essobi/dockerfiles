FROM jenkins/jenkins:lts  
  
USER root  
  
RUN apt-get update  
  
RUN apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
sudo \  
software-properties-common  
  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update  
RUN usermod -aG users jenkins  
  
RUN apt-get -y install docker-ce  
  
USER jenkins  

