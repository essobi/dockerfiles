FROM wordpress:fpm  
RUN apt-get -y update && apt-get -y install sendmail sendmail-bin mailutils  
COPY ./*.sh /usr/local/bin/  
COPY ./php_mail.ini /usr/local/etc/php/conf.d/mail.ini  
RUN chmod a+x /usr/local/bin/*.sh  
ENTRYPOINT ["start_sendmail_mta.sh"]  
CMD ["php-fpm"]

