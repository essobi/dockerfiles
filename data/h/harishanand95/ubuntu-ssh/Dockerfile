FROM ubuntu:16.04  
MAINTAINER Harish Anand "https://github.com/harishanand95"  
RUN apt-get update  
  
RUN apt-get install -y openssh-server sudo  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN mkdir ~/.ssh  
RUN apt-get install -y python  
EXPOSE 22  
EXPOSE 8000  
EXPOSE 8443  
EXPOSE 8001  
EXPOSE 8444  
CMD ["/usr/sbin/sshd", "-D"]  

