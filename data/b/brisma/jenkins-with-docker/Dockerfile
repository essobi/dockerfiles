FROM jenkins  
  
MAINTAINER Manuel Valentino <brisma@gmail.com>  
  
USER root  
RUN apt-get -qq update \  
&& apt-get -qq -y install \  
curl  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
RUN usermod -aG docker jenkins  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
  
RUN chmod +x /usr/local/bin/docker-compose  
  
USER jenkins  

