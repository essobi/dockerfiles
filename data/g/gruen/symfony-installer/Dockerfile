###########################################################  
# Run the symfony installer inside a container  
#  
# Refer to
(http://symfony.com/doc/current/book/installation.html)[http://symfony.com/doc/current/book/installation.html]  
#  
# Usage  
# docker run -it -rm \  
# -v [/path/to/symfony/directory]:/project \  
# --name symfony-installer \  
# gruen/symfony-installer \  
# new [directory] [commands]  
###########################################################  
FROM alpine:3.3  
MAINTAINER Darren Green <darren@gruen.site>  
COPY ./symfony /usr/local/bin/symfony  
RUN apk --no-cache --update add \  
php-common \  
php-cli \  
php-curl \  
php-json \  
php-phar \  
php-zlib \  
php-ctype \  
&& chmod 777 /usr/local/bin/symfony  
VOLUME [ "/project" ]  
  
WORKDIR /project  
  
ENTRYPOINT [ "symfony" ]  
  
# CMD [ "new", "symfony", "2.8" ]  

