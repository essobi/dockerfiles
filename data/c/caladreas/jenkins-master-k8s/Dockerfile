FROM jenkins/jenkins:2.107.3-slim  
  
MAINTAINER Joost van der Griendt <joostvdg@gmail.com>  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="2.107.3-slim-1"  
LABEL description="Docker container for Jenkins Master For Kubernetes"  
  
ENV JENKINS_OPTS "$JENKINS_OPTS --prefix=/jenkins"  
ENV JAVA_OPTS "-Djenkins.install.runSetupWizard=false -server
-XX:+AlwaysPreTouch"  
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  

