FROM alpine:edge  
RUN apk update ; apk upgrade; apk add supervisor sqlite tzdata  
ADD
https://github.com/roundcube/roundcubemail/releases/download/1.3.4/roundcubemail-1.3.4-complete.tar.gz
/opt/  
WORKDIR /opt  
RUN tar zxvf roundcubemail*gz ; rm -rf roundcubemail*gz ; ln -s
/opt/roundcube* /roundcube  
RUN for pack in $(apk search php7); do apk add `echo $pack|cut -f1,2 -d"-"`;
done  
  
RUN cp -Rf /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
RUN echo "Europe/Berlin" > /etc/timezone  
ENV TZ Europe/Berlin  
  
#RUN echo "php-fpm7 -F -O -R -c /etc/php7/php.ini -y /etc/php7/php-fpm.conf"
>/etc/supervisor/conf.d/php.conf  
#CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  
WORKDIR /roundcube  
CMD ["php", "-S", "0.0.0.0:80", "-t", "/roundcube/"]  

