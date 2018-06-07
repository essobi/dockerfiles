FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
#RUN mkdir -p /etc/raddb  
  
#VOLUME ["/etc/raddb","/var/log/radius"]  
  
RUN set -xe \  
&& apk add --no-cache freeradius \  
freeradius-radclient \  
freeradius-mysql \  
make \  
openssl \  
&& rm /etc/raddb/mods-enabled/eap  
  
COPY tmpl/_etc_raddb_mods-available_sql /etc/raddb/mods-available/sql  
RUN chown root:radius /etc/raddb/mods-available/sql  
RUN ln -sf /etc/raddb/mods-available/sql /etc/raddb/mods-enabled/sql  
  
COPY tmpl/_etc_raddb_sites-available_default /etc/raddb/sites-
available/default  
RUN chown root:radius /etc/raddb/sites-available/default  
  
COPY tmpl/_etc_raddb_sites-available_inner-tunnel /etc/raddb/sites-
available/inner-tunnel  
RUN chown root:radius /etc/raddb/sites-available/inner-tunnel  
  
## neet log in database /var/log/radius  
  
EXPOSE 1812/tcp  
EXPOSE 1813/tcp  
  
#CMD ["radiusd", "-f", "-d", "/etc/raddb"]  
CMD ["radiusd", "-fl", "stdout"]  

