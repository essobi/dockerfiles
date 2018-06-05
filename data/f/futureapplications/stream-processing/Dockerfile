FROM ubuntu:trusty  
MAINTAINER Michael Czaja  
RUN apt-get update; apt-get install -y unzip openjdk-7-jre-headless wget
supervisor docker.io openssh-server nano gedit openssh-client  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
RUN echo 'root:root' | chpasswd  
  
#SSH as root... probably needs to be revised for security!  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
EXPOSE 22  

