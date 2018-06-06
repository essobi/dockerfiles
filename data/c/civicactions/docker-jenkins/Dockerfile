FROM jenkins/jenkins:lts  
  
USER root  
  
# Install various packages  
RUN apt-get update && apt-get install -y apt-transport-https dirmngr sudo && \  
apt-get autoclean && apt-get autoremove  
  
# Install Docker and Docker Compose  
RUN curl https://get.docker.com/ | bash  
RUN curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
# Configure docker group and jenkins user  
RUN usermod -aG docker jenkins && usermod -aG sudo jenkins && id jenkins  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
# Connect git-lfs repo  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash  
  
# Install rsync and git-lfs  
RUN apt-get update && apt-get install -y rsync git-lfs && apt-get autoclean &&
apt-get autoremove  
  
USER jenkins  
RUN git lfs install  
  
EXPOSE 8080  

