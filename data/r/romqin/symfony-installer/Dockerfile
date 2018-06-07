FROM php:5-cli  
  
RUN curl -LsS http://symfony.com/installer > /usr/local/bin/symfony && \  
chmod +x /usr/local/bin/symfony && \  
echo "date.timezone = Europe/Paris" >> /usr/local/etc/php/conf.d/symfony.ini  
  
ENTRYPOINT ["symfony"]  

