FROM mysql:5.6  
MAINTAINER Przemek Szalko <przemek@rentcars.pl>  
  
# Copy maintenance scripts  
COPY maintenance /maintenance  
COPY conf /conf  
COPY mysql-prod-entrypoint.sh /mysql-prod-entrypoint.sh  
  
# Add Volume for logs  
VOLUME /var/log/mysql  
  
RUN apt-get update \  
&& apt-get install -y logrotate \  
cron \  
python \  
python-pip \  
&& pip install s3cmd  
  
# Enable cronjob to do maintenance tasks  
# Configure MySQL for production  
RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime \  
&& crontab /conf/crontab.in \  
&& mv /conf/mysql/* /etc/mysql/ \  
&& mv /conf/logrotate.d/* /etc/logrotate.d/ \  
&& rm -rf /conf  
  
ENTRYPOINT ["/mysql-prod-entrypoint.sh"]  
  
CMD ["mysqld"]

