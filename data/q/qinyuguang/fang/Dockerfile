FROM qinyuguang/yafbase:fpm  
  
VOLUME ["/www/fang", "/home/logs/project/fang", "/home/logs/php/fang",
"/var/mail", "/tmp"]  
  
COPY ./ /www/fang/  
COPY ./src/conf/crontab /etc/cron.d/fang  
COPY ./conf/online/php.ini /usr/local/etc/php/php.ini  
COPY ./conf/online/fpm.conf /usr/local/etc/php-fpm.d/fang.conf  
  
WORKDIR /www/fang  
  
RUN chmod 0644 /etc/cron.d/fang \  
&& crontab /etc/cron.d/fang  
  
CMD /www/fang/start.sh  
  

