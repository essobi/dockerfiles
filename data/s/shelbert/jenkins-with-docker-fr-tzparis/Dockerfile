FROM shelbert/jenkins-fr-tzparis:2.60.3  
  
USER root  
  
RUN curl -sSL https://get.docker.com/ | sh \  
&& curl -L https://github.com/docker/compose/releases/download/1.17.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& rm -rf /var/lib/apt/lists/* \  
&& usermod -aG docker jenkins  
  
USER jenkins  

