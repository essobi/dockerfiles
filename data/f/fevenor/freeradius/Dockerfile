FROM alpine  
  
MAINTAINER fevenor <fevenor@outlook.com>  
  
  
# Set up runing environment  
RUN apk add --update freeradius freeradius-mysql \  
&& rm -rf /var/cache/apk/* \  
  
# Configure FreeRADIUS  
&& set -x \  
&& sed -i "s/allow_vulnerable_openssl.*/allow_vulnerable_openssl = yes/"
/etc/raddb/radiusd.conf \  
&& sed -i "s/ipaddr = 127.0.0.1/ipaddr = 0.0.0.0\/0/" /etc/raddb/clients.conf
\  
&& sed -i 's/# read_clients/ readclients/' /etc/raddb/clients.conf \  
&& ln -s /etc/raddb/mods-available/sql /etc/raddb/mods-enabled/sql \  
&& chmod 777 /var/log/radius/  
  
ADD config.sh /root/  
  
ENV DB_HOST_VALUE=localhost  
ENV DB_PORT_VALUE=3306  
ENV DB_USER_VALUE=radius  
ENV DB_PASS_VALUE=radpass  
ENV DB_NAME_VALUE=radius  
  
EXPOSE 1812/udp  
EXPOSE 1813/udp  
  
CMD /root/config.sh;radiusd -X  

