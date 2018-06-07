FROM jenkins/jenkins:2.107.2  
MAINTAINER Firdaws Aboulaye "aboufred@gmail.com"  
  
ENV DOCKER_OPTS="-H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock"  
  
USER root  
  
RUN apt-get update \  
&& apt-get install apt-transport-https ca-certificates curl software-
properties-common -y \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- \  
&& apt-key fingerprint 0EBFCD88 \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable" \  
&& apt-get update \  
&& apt-get install docker-ce -y \  
&& usermod -aG docker jenkins \  
&& rm -rf /var/lib/apt/lists/*  
  
USER jenkins  

