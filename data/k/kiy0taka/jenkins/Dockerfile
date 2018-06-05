FROM jenkins/jenkins:lts  
MAINTAINER Kiyotaka Oku  
  
USER root  
RUN apt-get update && \  
apt-get install -y fonts-ipafont-gothic && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
USER jenkins  
COPY src/script /usr/share/jenkins/ref/init.groovy.d  

