FROM mitcdh/hiawatha-php  
MAINTAINER Mitchell Hewes <me@mitcdh.com>  
  
RUN apk --update add \  
curl \  
git && \  
rm -rf /var/cache/apk/*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY src/ /www/src  
COPY index.php /www  
COPY composer.json /www  
COPY scripts/postshare.sh /scripts/pre-run/01_postshare  
  
WORKDIR /www  
  
RUN composer install --prefer-source --no-interaction  
  
EXPOSE 80  
CMD ["/scripts/run.sh"]  
  

