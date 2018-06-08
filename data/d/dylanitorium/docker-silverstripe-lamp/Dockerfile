FROM debian:jessie  
MAINTAINER Sam Minnee <sam@silverstripe.com>  
  
### SET UP  
RUN apt-get -qq update  
  
RUN apt-get -qqy install sudo wget lynx telnet nano curl make git-core locales
bzip2  
  
RUN echo "LANG=en_US.UTF-8\n" > /etc/default/locale && \  
echo "en_US.UTF-8 UTF-8\n" > /etc/locale.gen && \  
locale-gen  
  
# Known hosts  
ADD known_hosts /root/.ssh/known_hosts  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
wget -O- http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
# APACHE, MYSQL, PHP & SUPPORT TOOLS  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get -qqy install apache2 \  
mysql-client \  
php7.0 \  
php7.0-cli \  
libapache2-mod-php7.0 \  
php7.0-gd \  
php7.0-json \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite3 \  
php7.0-xml \  
php7.0-xsl \  
php7.0-zip \  
php7.0-soap \  
php7.0-fpm \  
php7.0-curl \  
php7.0-mcrypt \  
php7.0-cli \  
php7.0-dev \  
php7.0-intl \  
php-pear \  
libsasl2-dev \  
sendmail  
  
# - Phpunit, Composer, Phing, SSPak  
RUN wget https://phar.phpunit.de/phpunit-3.7.37.phar && \  
chmod +x phpunit-3.7.37.phar && \  
mv phpunit-3.7.37.phar /usr/local/bin/phpunit && \  
wget https://getcomposer.org/composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
curl -sS https://silverstripe.github.io/sspak/install | php -- /usr/local/bin  
  
# SilverStripe Apache Configuration  
RUN a2enmod rewrite && \  
rm -r /var/www/html && \  
echo "date.timezone = Pacific/Auckland" >> /etc/php/7.0/fpm/php.ini  
  
ADD apache-foreground /usr/local/bin/apache-foreground  
ADD apache-default-vhost /etc/apache2/sites-available/000-default.conf  
  
####  
## These are not specifically SilverStripe related and could be removed on a
more optimised image  
# Ruby, RubyGems, Bundler  
RUN apt-get -qqy install ruby ruby-dev gcc && \  
gem install bundler && \  
gem install compass  
  
# NodeJS and common global NPM modules  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -qqy nodejs && \  
npm install -g grunt-cli gulp bower  
  
####  
## Commands and ports  
EXPOSE 80  
VOLUME /var/www  
  
# Run apache in foreground mode, because Docker needs a foreground  
WORKDIR /var/www  
CMD ["/usr/local/bin/apache-foreground"]  
  
ENV LANG en_US.UTF-8  

