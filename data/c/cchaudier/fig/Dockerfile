FROM ubuntu:14.04  
MAINTAINER Christophe Chaudier "chaudier.christophe@gmail.com"  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
RUN apt-get install -y curl  
RUN apt-get install -y docker.io  
RUN ln -sf /usr/bin/docker.io /usr/local/bin/docker  
  
#Install fig  
RUN curl -L https://github.com/orchardup/fig/releases/download/0.4.1/linux >
/usr/local/bin/fig  
RUN chmod +x /usr/local/bin/fig  

