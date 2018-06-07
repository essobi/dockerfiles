# Container from running phpcpd  
#  
# docker run -it --rm --name phpcpd \  
# -v [path/to/code]:/app \  
# gruen/phpcpd[:tag] [path/relative/to/app] [options]  
#  
FROM php:5.6-alpine  
MAINTAINER Darren Green <darren@gruen.site>  
WORKDIR /usr/local/bin  
RUN apk --no-cache --progress --update add \  
wget \  
&& wget https://phar.phpunit.de/phpcpd.phar -O phpcpd \  
&& chmod 700 ./phpcpd  
  
WORKDIR /app  
  
ENTRYPOINT [ "phpcpd" ]  

