#  
# ementux/datastore  
#  
# Datastore to keep volumes for scalable WP site  
#  
# See https://github.com/ementux/docker  
#  
FROM busybox  
MAINTAINER Michal Grna <michal.grna@ementux.org>  
  
# prepare volumes for web, db & haproxy  
VOLUME [ "/var/lib/mysql" , "/srv/certs", "/srv/www/logs" ,
"/srv/www/public_html" ]  
  
# add start script  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
  
# print info to STDOUT and exit  
CMD [ "/run.sh" ]  
  

