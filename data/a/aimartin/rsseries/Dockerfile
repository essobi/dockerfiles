FROM aimartin/django-nginx-uwsgi  
  
MAINTAINER Aitor Martin <aitor@martinh.es>  
  
ENV HOME /root  
  
ADD rsseries_nginx.conf /etc/nginx/conf.d/rsseries_nginx.conf  
  
ADD rsseries.ini /var/uwsgi/rsseries.ini  
  
ADD rSSeries /var/www/html  
  
ADD init.sh /usr/bin/init.sh  
  
RUN virtualenv /var/rsseries  
  
ADD requirements.txt /var/rsseries/requirements.txt  
  
RUN source /var/rsseries/bin/activate && pip install -r
/var/rsseries/requirements.txt  
  
RUN yum install -y cronie crontabs  
  
RUN echo "0 * * * * nginx curl -I http://127.0.0.1/series/refrescar" >>
/etc/crontab  

