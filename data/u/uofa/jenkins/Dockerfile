FROM jenkins:1.651.1  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
# copy plugins  
COPY ./files/plugins.txt /usr/share/jenkins/plugins.txt  
  
# run plugins.sh  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

