FROM ubuntu:14.04  
MAINTAINER Alvaro Rojas "https://github.com/AlvarRojas"  
RUN apt-get update  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN cd /home  
RUN wget http://dl.4players.de/ts/releases/3.0.11.4/teamspeak3-server_linux-
amd64-3.0.11.4.tar.gz  
RUN tar zxf teamspeak3-server_linux-amd64-3.0.11.4.tar.gz  
  
EXPOSE 22  
EXPOSE 9987/udp  
EXPOSE 30033  
EXPOSE 10011  
EXPOSE 8087  
CMD ["/usr/sbin/sshd", "-D"]  

