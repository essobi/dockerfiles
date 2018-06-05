FROM centos:centos7  
MAINTAINER Roberto Jung Drebes <drebes@gmail.com>>  
RUN yum -y install deltarpm && yum -y update && yum -y install bind  
RUN curl -L -o confd
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 && chmod a+x confd  
ADD confd /etc/confd  
ADD startup.sh .  
RUN mkdir -p /var/named/dynamic  
VOLUME /var/named/dynamic  
EXPOSE 53/udp  
ENV BIND_DOMAIN_FORWARD=example.com.  
ENV BIND_DOMAIN_REVERSE=1.168.192.in-addr.arpa.  
ENV BIND_UPSTREAM=8.8.8.8,8.8.4.4  
ENV BIND_KEY_SECRET="c3VwZXJzZWNyZXQ="  
ENV BIND_KEY_ALGORITHM="hmac-md5"  
CMD ./startup.sh  

