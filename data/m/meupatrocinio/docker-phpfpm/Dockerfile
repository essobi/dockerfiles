FROM romeoz/docker-phpfpm:5.4  
RUN apt-get update \  
&& apt-get install -y git cron supervisor rsyslog\  
&& rm -rf /var/lib/apt/lists/*  
  
ADD supervisord.conf /etc/supervisor/conf.d/  
  
WORKDIR /var/www  
  
EXPOSE 9000  
CMD /usr/bin/supervisord

