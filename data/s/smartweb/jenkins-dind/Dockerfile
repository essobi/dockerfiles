FROM jenkins/jenkins:lts  
  
USER root  
RUN wget -P /tmp/ https://get.docker.com/builds/Linux/x86_64/docker-1.13.0.tgz
\  
&& tar zxvf /tmp/docker-1.13.0.tgz -C /tmp \  
&& mv /tmp/docker/docker /usr/bin/docker \  
&& chmod +x /usr/bin/docker \  
&& rm -rf /tmp/docker \  
&& curl -L "https://github.com/docker/compose/releases/download/1.14.0/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose

