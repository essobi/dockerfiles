FROM jenkins/jenkins:lts-alpine  
USER root  
RUN apk --no-cache --update add docker git curl wget bash sudo  
RUN echo "%jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
USER jenkins  
  

