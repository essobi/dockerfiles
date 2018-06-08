FROM debian:testing  
LABEL maintainer="Tonnerre LOMBARD <tonnerre@ancient-one.com>"  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold update  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold install prosody prosody-modules lua-zlib lua-
dbi-postgresql  
  
VOLUME ["/etc/prosody", "/var/lib/prosody"]  
EXPOSE 80 443 5222 5269 5347 5280 5281  
USER prosody  
ENV __FLUSH_LOG yes  
CMD ["/usr/bin/prosody"]  

