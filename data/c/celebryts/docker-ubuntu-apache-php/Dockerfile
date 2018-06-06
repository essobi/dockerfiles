FROM ubuntu:16.04  
  
LABEL maintainer "docker@celebryts.com"  
  
ARG CELY_PHP_VERSION=7.0  
  
ENV CELY_PHP_VERSION=$CELY_PHP_VERSION  
# Set the minimum Ubuntu environment  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common \  
locales -y && \  
DEBIAN_FRONTEND=noninteractive locale-gen en_US.UTF-8 pt_BR.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \  
DEBIAN_FRONTEND=noninteractive apt-get install language-pack-en-base -y && \  
DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository
ppa:ondrej/php -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 \  
php$CELY_PHP_VERSION \  
libapache2-mod-php$CELY_PHP_VERSION && \  
DEBIAN_FRONTEND=noninteractive apt-get purge unzip -y && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \  
DEBIAN_FRONTEND=noninteractive apt-get clean -y  
  
WORKDIR /var/wwww/html  
  
EXPOSE 80  
  
COPY ./cely-ubuntu-apache-php-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT ["cely-ubuntu-apache-php-entrypoint.sh"]  
  
CMD ["apache2ctl", "-D", "FOREGROUND", "-e", "debug"]

