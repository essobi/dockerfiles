##FROM jpetazzo/squid-in-a-can  
FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install squid3 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i "s/^#acl localnet/acl localnet/" /etc/squid3/squid.conf  
RUN sed -i "s/^#http_access allow localnet/http_access allow localnet/"
/etc/squid3/squid.conf  
RUN sed -i "s/^#acl localnet src 192.168.0.0\/16/acl localnet src
192.168.0.0\/16/" /etc/squid3/squid.conf  
RUN echo 'cache_peer privoxy parent 8118 0 default no-query no-digest no-
netdb-exchange' >> /etc/squid3/squid.conf  
RUN squid3 -z -N -F  
  
EXPOSE 3128  
CMD [ "squid3", "-N" ]  

