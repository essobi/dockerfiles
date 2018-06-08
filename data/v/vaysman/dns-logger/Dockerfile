# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.17  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN apt-get install -y pdns-recursor  
  
RUN sed -i 's/quiet=yes/quiet=no/' /etc/powerdns/recursor.conf && \  
sed -i 's/# logging-facility=/logging-facility=0/' /etc/powerdns/recursor.conf
&& \  
sed -i 's/local-address=127.0.0.1/local-address=0.0.0.0/'
/etc/powerdns/recursor.conf && \  
sed -i 's/# daemon=yes/daemon=no/' /etc/powerdns/recursor.conf  
  
RUN mkdir /etc/service/pdns-recursor  
RUN echo '#!/bin/sh' > /etc/service/pdns-recursor/run  
RUN echo 'exec /sbin/setuser root /usr/sbin/pdns_recursor
>>/var/log/pdns_recursor.log 2>&1' >> /etc/service/pdns-recursor/run  
RUN chmod +x /etc/service/pdns-recursor/run  
  
EXPOSE 53/udp  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

