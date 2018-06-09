FROM nginx:1.13  
#install certbox  
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >>
/etc/apt/sources.list  
RUN apt-get -y update && apt-get -y install python-certbot-nginx -t stretch-
backports  
  
#install cron  
RUN apt-get -y update && apt-get -y install cron  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/certbot  
RUN chmod 0644 /etc/cron.d/certbot  
  
# copy shell scripts  
COPY scripts/ssl-* /usr/local/bin/  
RUN chmod 744 /usr/local/bin/ssl-*  
  
# copy Nginx config  
COPY conf.d /etc/nginx/conf.d  
  
# create folders for certbot  
RUN mkdir -p /var/www/certbot  
  
# launch cron, script for obtaining certificates, and nginx  
CMD cron & ssl-obtain & nginx -g "daemon off;"  

