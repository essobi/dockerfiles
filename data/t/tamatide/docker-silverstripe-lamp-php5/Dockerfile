FROM debian:jessie  
MAINTAINER Sam Minnee <sam@silverstripe.com>  
  
### SET UP  
RUN apt-get -qqy update  
  
RUN apt-get -qqy install apt-utils cron sudo wget lynx telnet nano curl make
git-core locales bzip2  
  
RUN echo "LANG=en_US.UTF-8\n" > /etc/default/locale && \  
echo "en_US.UTF-8 UTF-8\n" > /etc/locale.gen && \  
locale-gen  
  
# Known hosts  
ADD known_hosts /root/.ssh/known_hosts  
  
# APACHE, MYSQL, PHP & SUPPORT TOOLS  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install apache2 mysql-client \  
php5-cli libapache2-mod-php5 php5-mysqlnd php5-mcrypt php5-tidy php5-curl
php5-gd php-pear sendmail sendmail-bin  
  
# - Phpunit, Composer, Phing, SSPak  
RUN wget https://phar.phpunit.de/phpunit-3.7.37.phar && \  
chmod +x phpunit-3.7.37.phar && \  
mv phpunit-3.7.37.phar /usr/local/bin/phpunit && \  
wget https://getcomposer.org/composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer && \  
pear channel-discover pear.phing.info && \  
pear install phing/phing && \  
curl -sS https://silverstripe.github.io/sspak/install | php -- /usr/local/bin  
  
# SilverStripe Apache Configuration  
RUN a2enmod rewrite && \  
rm -r /var/www/html && \  
echo "date.timezone = Pacific/Auckland" >
/etc/php5/apache2/conf.d/timezone.ini && \  
echo "date.timezone = Pacific/Auckland" > /etc/php5/cli/conf.d/timezone.ini  
  
ADD apache-foreground /usr/local/bin/apache-foreground  
  
####  
## Commands and ports  
EXPOSE 80  
VOLUME /var/www  
  
####  
## Personal stuff  
RUN echo 'alias ll="ls -al"' >> ~/.bashrc  
RUN a2dissite 000-default.conf && \  
a2dissite default-ssl.conf  
RUN chown -Rf www-data:www-data /var/www  
  
# Run apache in foreground mode, because Docker needs a foreground  
WORKDIR /var/www  
CMD ["/usr/local/bin/apache-foreground"]history  
  
ENV LANG en_US.UTF-8  

