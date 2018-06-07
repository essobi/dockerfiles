  
FROM ubuntu:14.04  
MAINTAINER H.Y. Leung <hy.leung@gmail.com>  
  
#Update the package repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt.sources.list  
RUN apt-get update  
  
#Install SSHD  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
  
#Install the JDK  
RUN apt-get install -y --no-install-recommends openjdk-7-jdk  
  
#Add the jenkins user (passwd jenkins)  
RUN useradd -d /home/jenkins jenkins  
RUN mkdir -p /home/jenkins  
RUN chown jenkins /home/jenkins  
  
RUN echo "jenkins:jenkins" | chpasswd  
  
##Expose the SSHD port  
EXPOSE 22  
#Install Git  
RUN apt-get install -y git  
  
CMD ["/usr/sbin/sshd","-D"]  
  

