FROM ubuntu:14.04  
MAINTAINER nekoya "ryo.studiom@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i 's/archive.ubuntu.com/ftp.jaist.ac.jp\/pub\/Linux/'
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
bind9 \  
bind9utils \  
dnsutils \  
unbound  
  
COPY named.conf.options /etc/bind/named.conf.options  
COPY unbound.conf /etc/unbound/unbound.conf  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 53/udp  
  
CMD ["/start.sh"]  

