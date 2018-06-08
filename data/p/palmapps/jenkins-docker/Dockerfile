FROM jenkins:2.32.1  
USER root  
RUN apt-get update && apt-get install -y httping  
  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
  
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt |
tr '\n' ' ')  
  

