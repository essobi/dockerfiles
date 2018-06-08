FROM jenkins:latest  
  
USER root  
  
RUN apt-get update; apt-get install -y \  
curl \  
sudo  
  
RUN curl -sSL https://get.docker.com/ | sh && \  
usermod -aG docker jenkins  
  
RUN sed -i 's!/bin/bash!/bin/bash\n\nsudo /etc/init.d/docker start\nsudo chown
-R jenkins.jenkins \/var\/jenkins_home\nsleep 15!g' /usr/local/bin/jenkins.sh  
  
RUN echo 'jenkins ALL = NOPASSWD: /etc/init.d/docker' >> /etc/sudoers && \  
echo 'jenkins ALL = NOPASSWD: /bin/chown' >> /etc/sudoers  
  
USER jenkins  

