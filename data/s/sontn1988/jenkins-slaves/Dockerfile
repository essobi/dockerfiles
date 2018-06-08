FROM ubuntu:14.04  
MAINTAINER SONTN  
  
RUN apt-get update  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get install git wget openssh-server openjdk-8-jdk -y  
  
RUN useradd jenkins -m -d /home/jenkins -s /bin/bash  
  
RUN mkdir /home/jenkins/.ssh  
  
COPY /files/authorized_keys /home/jenkins/.ssh/authorized_keys  
COPY /files/config /home/jenkins/.ssh/config  
  
RUN chown -R jenkins: /home/jenkins  
RUN chmod 600 /home/jenkins/.ssh/authorized_keys  
RUN chmod 644 /home/jenkins/.ssh/config  
RUN chmod 700 /home/jenkins/.ssh  
  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> etc/sudoers  
  
RUN mkdir -p /var/run/sshd  
# Set Name Servers  
COPY /files/resolv.conf /etc/resolv.conf  
  

