FROM jenkinsci/jnlp-slave  
MAINTAINER Nicolas Degardin <ndegardin@tribalnova.com>  
  
USER root  
  
# Docker installation  
RUN echo "deb http://http.debian.net/debian wheezy-backports main" >>
/etc/apt/sources.list.d/backports.list  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:11371 --recv-
keys 58118E89F3A912897C070ADBF76221572C52609D  
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >>
/etc/apt/sources.list.d/docker.list  
RUN apt-get update && apt-get install -y docker-engine  
RUN gpasswd -a jenkins docker  
  
# Docker-compose installation  
RUN curl -L https://github.com/docker/compose/releases/download/1.9.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
COPY files/startup.sh /opt/docker/startup.sh  
ENTRYPOINT ["/opt/docker/startup.sh"]  

