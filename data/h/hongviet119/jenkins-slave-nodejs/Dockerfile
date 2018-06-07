FROM node:9.3.0  
MAINTAINER Viet Nguyen <hongviet119@gmail.com>  
  
# Add backports  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list  
  
# Upgrade and Install packages  
RUN apt-get update && apt-get -y upgrade && apt-get install -y git openssh-
server && apt-get -t jessie-backports install -y openjdk-8-jdk  
  
# Prepare container for ssh  
RUN mkdir /var/run/sshd && adduser --quiet jenkins && echo "jenkins:jenkins" |
chpasswd  
  
RUN npm install -g gulp && npm install -g bower  
  
ENV CI=true  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  
  

