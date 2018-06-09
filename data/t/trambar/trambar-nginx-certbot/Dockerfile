FROM nginx:1.13  
  
#install certbot  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >>
/etc/apt/sources.list  
RUN apt-get -y update && apt-get -y install python-certbot-nginx -t stretch-
backports  
  
#install cron  
RUN apt-get -y update && apt-get -y install cron  
  
# copy configuration  
COPY conf.d /etc/nginx/conf.d  
  
# copy www files  
COPY client /var/www/trambar/client  
COPY admin /var/www/trambar/admin  
  
# copy scripts  
COPY scripts/ssl-* /usr/local/bin/  
RUN chmod 744 /usr/local/bin/ssl-*  
  
# place crontab file into cron.d  
ADD crontab /etc/cron.d/certbot  
RUN chmod 0644 /etc/cron.d/certbot  
  
# launch cron, script for obtaining certificates, and nginx  
CMD cron & ssl-obtain & nginx -g "daemon off;"  

