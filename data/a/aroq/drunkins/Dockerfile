FROM jenkins/jenkins:2.107.1-alpine  
  
USER root  
RUN apk update && \  
apk add bash git openssh rsync procps && \  
rm -rf /var/cache/apk/*  
  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt |
tr '\n' ' ')  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  

