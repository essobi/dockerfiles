FROM alpine:3.6  
RUN apk update && apk upgrade \  
&& apk add --update freeradius freeradius-eap openssl \  
&& rm /var/cache/apk/* \  
&& /etc/raddb/certs/bootstrap \  
&& chown -R radius:radius /etc/raddb \  
&& rm /etc/raddb/sites-enabled/* \  
&& ln -s /etc/raddb/sites-available/site /etc/raddb/sites-enabled/site \  
&& mkdir /tmp/radiusd /conf \  
&& touch /conf/users /conf/clients.conf \  
&& ln -sf /conf/clients.conf /etc/raddb/clients.conf \  
&& ln -sf /conf/users /etc/raddb/mods-config/files/authorize  
COPY radiusd.conf /etc/raddb/  
COPY eap /etc/raddb/mods-available  
COPY site /etc/raddb/sites-available  
CMD ["radiusd", "-f", "-l/proc/1/fd/1", "-xx"]  

