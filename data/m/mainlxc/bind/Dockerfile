FROM mainlxc/ubuntu  
MAINTAINER Asokani "https://github.com/asokani"  
RUN apt-get update && \  
apt-get -y install bind9 dnsutils  
  
RUN mkdir /etc/service/bind  
ADD bind.sh /etc/service/bind/run  
  
# allow zone list using HTTP  
RUN mkdir /etc/service/http  
ADD http.sh /etc/service/http/run  
  
RUN mkdir -p /opt/bind-http/cgi-bin  
ADD http-zone-list.sh /opt/bind-http/cgi-bin/zone-list.sh  
RUN chown www-user:www-user /opt/bind-http/cgi-bin/zone-list.sh  
RUN chmod 0750 /opt/bind-http/cgi-bin/zone-list.sh  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

