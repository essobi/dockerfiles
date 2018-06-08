FROM ubuntu:14.04  
MAINTAINER Olokz "https://github.com/Olokz"  
ENV ROOT_PASS="@hyujG667$r"  
RUN apt-get update  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo root:"$ROOT_PASS" | chpasswd  
  
RUN chage -d 0 root  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 587/tcp  
EXPOSE 53/tcp  
EXPOSE 1023/tcp  
EXPOSE 12443/tcp  
EXPOSE 11443/tcp  
EXPOSE 11444/tcp  
EXPOSE 8443/tcp  
EXPOSE 8447/tcp  
EXPOSE 8880/tcp  
EXPOSE 80/tcp  
EXPOSE 443/tcp  
EXPOSE 21/tcp  
EXPOSE 22/tcp  
EXPOSE 25/tcp  
EXPOSE 110/tcp  
EXPOSE 995/tcp  
EXPOSE 993/tcp  
EXPOSE 143/tcp  
EXPOSE 106/tcp  
EXPOSE 3306/tcp  
EXPOSE 5432/tcp  
EXPOSE 9008/tcp  
EXPOSE 9080/tcp  
EXPOSE 137/udp  
EXPOSE 138/udp  
EXPOSE 139/tcp  
EXPOSE 445/tcp  
EXPOSE 1194/udp  
  
CMD ["/usr/sbin/sshd", "-D"]  

