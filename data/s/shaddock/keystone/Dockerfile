FROM shaddock/seed:latest  
MAINTAINER Thibaut Lapierre <root@epheo.eu>  
  
RUN apt-get update &&\  
apt-get install -y --force-yes keystone apache2 libapache2-mod-wsgi  
  
RUN \  
(crontab -l -u keystone 2>&1 | grep -q token_flush) || \  
echo '@hourly /usr/bin/keystone-manage token_flush
>/var/log/keystone/keystone-tokenflush.log 2>&1' \  
>> /var/spool/cron/crontabs/keystone  
RUN \  
rm -f /var/lib/keystone/keystone.db  
  
ADD wsgi-keystone.conf /etc/apache2/sites-available/  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD keystone-start /usr/local/bin/  
ADD configparse.py /usr/local/bin/  
RUN ln -s /etc/apache2/sites-available/wsgi-keystone.conf /etc/apache2/sites-
enabled/  
RUN chmod +x /usr/local/bin/keystone-start  
RUN chmod +x /usr/local/bin/configparse.py  
  
VOLUME ["/var/log/keystone"]  
  
EXPOSE 35357  
EXPOSE 5000  
CMD ["keystone-start"]  

