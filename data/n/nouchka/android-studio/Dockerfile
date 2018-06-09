FROM yongjhih/android-studio:1.5.1  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-android-
studio"  
LABEL version="1.5.1"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
USER root  
RUN apt-get update --fix-missing && \  
apt-get update && \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
apt-get install nodejs  
  
RUN npm install -g react-native-cli  

