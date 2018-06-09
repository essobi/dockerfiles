FROM php:7.1-alpine  
  
RUN apk update \  
&& apk upgrade \  
&& apk add git \  
&& echo "phar.readonly = 0\n" >> /usr/local/etc/php/php.ini \  
&& curl -LSs https://box-project.github.io/box2/installer.php | php \  
&& mv box.phar /usr/local/bin/box \  
&& chmod 0755 /usr/local/bin/box \  
&& box update  
  
WORKDIR /usr/src

