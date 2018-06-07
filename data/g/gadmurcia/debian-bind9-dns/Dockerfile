FROM debian:latest  
RUN rm /etc/apt/sources.list  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update && apt-get -y install bind9 bind9-doc dnsutils nano zip
unzip  
COPY delsas.zip /etc/bind/debianDNS.zip  
RUN rm /etc/bind/named.conf.local && unzip /etc/bind/debianDNS.zip -d
/etc/bind/  
EXPOSE 53:53  
ENTRYPOINT /etc/init.d/bind9 restart && cp /etc/bind/resolv.conf
/etc/resolv.conf && bash  

