FROM php:7.0-alpine  
  
MAINTAINER Spencer Rinehart <anubis@overthemonkey.com>  
  
RUN apk add --no-cache --virtual .php-composer-deps git openssh  
  
RUN mkdir /code  
WORKDIR /code  
  
ENV COMPOSER_HOME $HOME/.composer  
  
# Setup and install composer into the composer global location. The  
# certificate is installed manually to get around open_basedir restrictions.  
RUN mkdir -p $COMPOSER_HOME/vendor/bin  
RUN curl -sSL https://getcomposer.org/installer | \  
php -- --install-dir=$COMPOSER_HOME/vendor/bin --filename=composer  
  
# Setup PATH to prioritize local composer bin and global composer bin ahead of  
# system PATH.  
ENV PATH vendor/bin:$COMPOSER_HOME/vendor/bin:$PATH  
  
CMD ["composer", "install"]  

