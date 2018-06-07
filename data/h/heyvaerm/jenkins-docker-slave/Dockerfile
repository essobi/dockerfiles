FROM ubuntu:14.04  
MAINTAINER Michaël Heyvaert  
  
# Install git and ssh server  
RUN apt-get update -q  
RUN apt-get install -y openssh-server git-core openjdk-7-jre-headless  
RUN mkdir -p /var/run/sshd  
  
# setup user  
RUN useradd -m jenkins -s /bin/bash  
RUN echo "jenkins:jenkins" | chpasswd  
  
CMD ["/usr/sbin/sshd", "-D"]  
EXPOSE 22  

