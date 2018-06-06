# https://github.com/jwilder/nginx-proxy  
FROM toshiclick/gitlab-ci-php-base  
  
# 作成者情報  
MAINTAINER toshi <toshi@toshi.click>  
  
ENV PHAN_VERSION=0.8.8  
RUN pecl install ast-0.1.6  
RUN docker-php-ext-enable ast  
RUN curl -L
https://github.com/phan/phan/releases/download/${PHAN_VERSION}/phan.phar -o
/usr/bin/phan  
RUN chmod 755 /usr/bin/phan  

