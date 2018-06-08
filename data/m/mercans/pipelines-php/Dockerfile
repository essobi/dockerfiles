FROM alpine:3.4  
MAINTAINER anton.pelesev@mercans.ee  
  
COPY phpmd-rules.xml /phpmd/rules.xml  
  
RUN apk update && apk add --no-cache \  
bash \  
curl \  
git \  
php5-bz2 \  
php5-cli \  
php5-ctype \  
php5-dom \  
php5-json \  
php5-openssl \  
php5-phar \  
php5-xml  
  
RUN curl -Lso /usr/local/bin/phpmd
http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x /usr/local/bin/phpmd  
  
RUN curl -Lso /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar \  
&& chmod +x /usr/local/bin/phpunit  
  
RUN curl -LsS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
CMD ["/bin/bash"]  
  
RUN rm -rf /var/cache/apk/*  

