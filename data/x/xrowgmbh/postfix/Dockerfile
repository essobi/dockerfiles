# docker run --privileged --name smtp -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p
25:25 -d xrowgmbh/postfix:latest  
# Ideas from https://github.com/eea/eea.docker.postfix  
FROM xrowgmbh/systemd  
  
MAINTAINER "Björn Dieding" <bjoern@xrow.de>  
  
ENV container=docker  
ENV term=xterm  
  
RUN yum -y install postfix; yum clean all; systemctl enable postfix  
RUN postconf -e 'mynetworks = 127.0.0.1/32 192.168.0.0/16 172.16.0.0/12
10.0.0.0/8 [::1]'  
RUN postconf -e 'mynetworks_style = class'  
RUN postconf -e 'inet_interfaces = all'  
  
ADD postfix.sh /postfix.sh  
RUN chmod 755 /postfix.sh  
  
EXPOSE 25  
CMD [ "/usr/sbin/init" ]  

