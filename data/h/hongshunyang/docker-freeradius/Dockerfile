FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
RUN apk add --no-cache freeradius \  
freeradius-radclient \  
&& rm /etc/raddb/mods-enabled/eap  
  
COPY tmpl/_etc_raddb_mods-config_files_authorize /etc/raddb/mods-
config/files/authorize  
RUN chown root:radius /etc/raddb/mods-config/files/authorize  
  
VOLUME ["/etc/raddb","/var/log/radius"]  
  
EXPOSE 1812/udp 1813/udp  
  
#CMD ["radiusd", "-f", "-d", "/etc/raddb"]  
CMD ["radiusd", "-fl", "stdout"]  
#CMD ["radiusd" "-X"]  

