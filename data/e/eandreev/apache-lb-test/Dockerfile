FROM ubuntu:14.04  
# install apache  
RUN apt-get update  
RUN apt-get install apache2 collectd collectd-utils supervisor -y  
  
# Apache needs tese dirs  
RUN mkdir /var/lock/apache2  
RUN mkdir /var/run/apache2  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY collectd.conf /etc/collectd/collectd.conf  
COPY collectd.conf /etc/collectd/collectd.conf.orig  
  
COPY start.sh /start.sh  
  
# modify index.html  
RUN echo "<h1>Running from Docker on CoreOS "`date '+%Y-%m-%d
%H:%M:%S'`"</h1>" > /var/www/html/index.html  
  
EXPOSE 80  
CMD ["/start.sh"]  

