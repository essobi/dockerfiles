FROM hitalos/laravel  
MAINTAINER maizhongwen <yshxinjian@gmail.com>  
  
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g'
/etc/apk/repositories  
ADD install-php-ext.sh /build-docker/  
RUN chmod +x /build-docker/install-php-ext.sh && /build-docker/install-php-
ext.sh  
  
RUN crontab -l | { cat; echo "* * * * * php /var/www/artisan schedule:run >>
/var/log/cron.log 2>&1"; } | crontab -  
  
ADD run.sh /build-docker/  
RUN chmod +x /build-docker/run.sh  
  
WORKDIR /var/www  
EXPOSE 80  
CMD ["/build-docker/run.sh"]  

