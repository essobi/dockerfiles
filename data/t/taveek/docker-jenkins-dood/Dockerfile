FROM jenkins:latest  
  
USER root  
RUN apt-get update \  
&& apt-get install -y sudo \  
&& curl -sSL https://get.docker.com/ | sh \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
RUN usermod -G docker -a jenkins  
  
USER jenkins  

