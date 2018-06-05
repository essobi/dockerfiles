FROM ubuntu:16.04  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y locales  
  
RUN mkdir .ssh  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN apt-get install -y software-properties-common ssh  
RUN ssh-keyscan bitbucket.org > /root/.ssh/known_hosts  
  
# LIBS  
RUN apt-get install -y curl git libmcrypt-dev libicu-dev libxslt-dev
libxml2-dev unzip\  
postgresql postgresql-common libpq-dev \  
openjdk-8-jre  
  
# PHP  
RUN add-apt-repository -y ppa:ondrej/php  
RUN apt-get update && apt-get install -y php7.1  
  
# PHP Extensions  
RUN apt-get install -y php7.1-mbstring php7.1-mcrypt php7.1-curl \  
php7.1-intl php7.1-bcmath php7.1-xml php7.1-xsl php7.1-zip php7.1-pgsql \  
php7.1-xdebug php7.1-sqlite php7.1-apc php7.1-redis  
  
# COMPOSER  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
  
# ELASTICSEARCH  
RUN wget
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.4.1/elasticsearch-2.4.1.deb  
RUN dpkg -i elasticsearch-2.4.1.deb  
  
# APACHE  
COPY apache2.conf /etc/apache2/apache2.conf  
RUN rm /etc/apache2/sites-available/* /etc/apache2/conf-enabled/*  
RUN a2enmod rewrite  
  
ADD pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf  
  
EXPOSE 80  
EXPOSE 9000  
COPY start_web.sh /usr/local/bin/start_web  

