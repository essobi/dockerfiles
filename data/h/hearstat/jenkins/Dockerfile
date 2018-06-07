FROM jenkins  
MAINTAINER Hearst Automation Team  
  
COPY plugins.txt /plugins.txt  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  
  
RUN /usr/local/bin/install-plugins.sh $(cat plugins.txt)  

