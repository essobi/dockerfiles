FROM ubuntu:14.04  
MAINTAINER ManuPrasad mmanuprasad@gmail.com  
  
user root  
  
RUN apt-get update && apt-get install -y openssh-server  
  
RUN mkdir -p /var/run/sshd  
  
RUN echo 'root:demo' | chpasswd  
  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
RUN sed -i 's/usePAM yes/usePAM no/g' /etc/ssh/sshd_config  
  

