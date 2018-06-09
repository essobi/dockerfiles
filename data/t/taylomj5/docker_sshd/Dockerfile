# Version: -1.0.1  
#Ubuntu 13.04 image  
FROM ubuntu:14.04  
#Set Maintainer  
MAINTAINER Matthew Taylor "taylomj5@student.op.ac.nz"  
#updates  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install openssh-server  
RUN mkdir /var/run/sshd  
#Create new user  
RUN useradd -m -G sudo user  
#cHANGE pASSWORD  
RUN echo 'user:P@ssw0rd' | chpasswd  
#Install sshd  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]  

