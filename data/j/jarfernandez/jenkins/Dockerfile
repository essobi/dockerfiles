FROM jenkins/jenkins  
  
USER root  
RUN apt-get -y update && apt-get install -y maven  
  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

