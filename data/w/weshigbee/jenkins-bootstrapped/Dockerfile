# FYI image docs are here:  
# https://github.com/jenkinsci/docker/blob/master/README.md  
FROM jenkins/jenkins:lts-alpine  
  
USER root  
RUN apk -U add tree docker  
USER jenkins  
  
RUN install-plugins.sh \  
git \  
dockerhub-notification \  
blueocean  
  
COPY ref /usr/share/jenkins/ref/.

