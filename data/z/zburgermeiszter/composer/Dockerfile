FROM php:7.0-cli  
  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
libicu-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip && \  
docker-php-ext-install -j$(nproc) bcmath mbstring sockets mcrypt zip bz2 intl  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Create user  
RUN useradd -u 1000 -mU user && \  
mkdir /app && \  
chown -R user:user /app  
  
USER user  
# Environmental Variables  
ENV COMPOSER_HOME /home/user/composer  
  
# Add global binary directory to path  
ENV PATH $COMPOSER_HOME/vendor/bin:$PATH  
  
VOLUME ["/app"]  
WORKDIR /app  
  
CMD ["-"]  
ENTRYPOINT ["composer", "--ansi"]

