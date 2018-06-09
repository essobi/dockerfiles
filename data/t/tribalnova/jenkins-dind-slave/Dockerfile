FROM docker:1.12.3-dind  
MAINTAINER Nicolas Degardin <ndegardin@tribalnova.com>  
  
ENV DOCKER_HOST tcp://0.0.0.0:2375  
ENV HOME /home/jenkins  
  
# Install requirements  
RUN apk --update add curl git openjdk8-jre sudo openssh bash  
  
# Add jenkins user  
RUN adduser -D -h $HOME -u 10000 -g 10000 -s /bin/sh jenkins jenkins \  
&& chmod a+rwx $HOME  
RUN echo "jenkins ALL=(ALL) NOPASSWD: /usr/local/bin/docker" >
/etc/sudoers.d/00jenkins \  
&& chmod 440 /etc/sudoers.d/00jenkins  
  
# Docker-compose installation  
RUN curl -L https://github.com/docker/compose/releases/download/1.9.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
COPY files/startup.sh /usr/local/bin/jenkins-slave  
  
RUN mkdir /home/jenkins/.jenkins  
WORKDIR /home/jenkins  
  
ENTRYPOINT ["jenkins-slave"]  

