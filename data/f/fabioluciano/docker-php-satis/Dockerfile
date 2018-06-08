FROM fabioluciano/docker-php-alpine:latest  
  
MAINTAINER Fábio Luciano <fabio.goisl@ctis.com.br>  
  
RUN apk update && \  
apk upgrade && \  
apk add --update git  
  
ENV COMPOSER_HOME /usr/share/composer  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& /usr/local/bin/composer global require hirak/prestissimo \  
&& printf "\n" | /usr/local/bin/composer create-project playbloom/satisfy:dev-
master --stability=dev \  
&& chmod -R 777 /satisfy \  
&& rm -rf $COMPOSER_HOME/cache/*  
  
ADD files/nginx.conf /etc/nginx/nginx.conf  
ADD files/satis.php /satisfy/app/config.php  
ADD files/satis.json /satisfy/app/config.json  
RUN chmod a+rw /satisfy/app/config.json  

