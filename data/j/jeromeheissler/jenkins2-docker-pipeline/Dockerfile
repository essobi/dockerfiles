FROM jenkinsci/jenkins:lts  
  
# Install sudo and make jenkins sudoer to be able to call docker with sudo
from inside jenkins container  
USER root  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
# This will install docker client to be able to call docker from docker  
RUN curl -fsSL https://get.docker.com/ | sh  
  
RUN usermod -aG docker jenkins  
  
RUN apt-get update && apt-get install -y jq fontconfig libfontconfig  
  
USER jenkins  

