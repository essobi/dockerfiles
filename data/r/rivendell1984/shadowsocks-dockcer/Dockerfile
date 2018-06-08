# shadowsocks  
FROM ubuntu:14.04.3  
MAINTAINER Rivendell <rivendell1984@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:toor' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
RUN apt-get install -y python python-pip python-m2crypto libnet1-dev
libpcap0.8-dev git  
  
RUN pip install shadowsocks  
  

