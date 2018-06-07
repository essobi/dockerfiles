FROM jaggman/php  
  
RUN apt-get update && \  
apt-get install -y supervisor && \  
ln -sf /dev/stdout /var/log/supervisor/supervisord.log  
  
ADD service.sh /etc/my_init.d/service.sh  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
RUN chmod a+x /etc/my_init.d/service.sh  
  
VOLUME [ "/etc/supervisor/conf.d/", "/etc/cron.d/" ]

