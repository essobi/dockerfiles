#  
# Derives from https://github.com/jenkinsci/docker/blob/master/Dockerfile-
alpine  
#  
FROM jenkins/jenkins:2.60.3-alpine AS base  
  
# For kubernetes permission errors  
USER root  
  
VOLUME [ "/var/jenkins_home" ]  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
FROM base AS build-deps  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 50001  
# RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  

