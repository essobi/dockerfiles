FROM ubuntu:latest  
MAINTAINER writtic <writtic@gmail.com>  
RUN apt-get update; apt-get install -y unzip openjdk-8-jre-headless curl
supervisor docker.io openssh-server  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
RUN echo 'root:ijinow' | chpasswd  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
EXPOSE 22  

