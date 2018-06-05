FROM qinyuguang/yafbase:fpm  
  
VOLUME ["/www/bigscreen", "/home/logs/project/bigscreen",
"/home/logs/php/bigscreen"]  
  
COPY ./ /www/bigscreen/  
COPY ./conf/online/php.ini /usr/local/etc/php/php.ini  
COPY ./conf/online/fpm.conf /usr/local/etc/php-fpm.d/bigscreen.conf  
  
WORKDIR /www/bigscreen  
  
RUN docker-php-ext-install bcmath  
  
CMD /www/bigscreen/start.sh  
  

