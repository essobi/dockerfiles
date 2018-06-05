FROM php:7.1-fpm  
MAINTAINER Alexander Schneider <alexanderschneider85@gmail.com>  
# Install modules  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-nss-dev \  
libxml2-dev \  
zlib1g-dev \  
libicu-dev \  
libpcre3-dev \  
lib32ncurses5 \  
g++ \  
git \  
wget \  
curl \  
mysql-client \  
libpq-dev \  
vim  
  
# Install php extensions  
ADD extensions /tmp/php/extensions  
RUN chmod +x /tmp/php/extensions/install_extensions.sh  
RUN /tmp/php/extensions/install_extensions.sh /tmp/php/extensions/  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install tideways  
RUN echo 'deb http://s3-eu-west-1.amazonaws.com/qafoo-profiler/packages debian
main' > /etc/apt/sources.list.d/tideways.list  
RUN wget -qO - https://s3-eu-west-1.amazonaws.com/qafoo-
profiler/packages/EEB5E8F4.gpg | apt-key add - -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
tideways-php \  
tideways-daemon  
  
ENV APP_DIR '/var/www/app'  
ENV DB_HOST 'mysql'  
ENV DB_USER 'root'  
ENV DB_PASS 'root'  
ENV DB_NAME 'app'  
ENV DB_DUMP ''  
ENV BACKUP_URL ''  
ENV BACKUP_USER ''  
ENV BACKUP_PASS ''  
ENV PROJECT_URL ''  
ENV PROJECT_TYPE ''  
ENV USER_MAIL 'dev@local.docker'  
ENV USER_PASS 'root'  
ENV FILE_PERMISSIONS ''  
ADD projects /usr/bin/projects  
ADD run.sh /usr/bin/run  
RUN chmod +x /usr/bin/run  
WORKDIR /var/www/app  
EXPOSE 22 9000  
CMD ["/bin/bash", "/usr/bin/run"]

