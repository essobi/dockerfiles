FROM php:7  
RUN apt-get update \  
&& apt-get install -y cron \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkfifo --mode 0666 /var/log/cron.log  
  
# make pam_loginuid.so optional for cron  
# see https://github.com/docker/docker/issues/5663#issuecomment-42550548  
RUN sed --regexp-extended --in-place \  
's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' \  
/etc/pam.d/cron  
  
COPY start-cron /usr/sbin  
COPY mercury.php /mercury.php  
  
ENV SERVER_HOST influxdb  
ENV SERVER_PORT 8086  
ENV DB_NAME openhab_db  
ENV MEASUREMENT ElectricMeter  
  
CMD start-cron "\\* \\* \\* \\* \\* /usr/local/bin/php -f /mercury.php >>
/var/log/cron.log 2>&1"  

