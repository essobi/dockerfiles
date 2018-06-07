# DOCKER-VERSION 1.0.0  
FROM datenbetrieb/debian:jessie  
MAINTAINER Peter Niederlag "peter.niederlag@datenbetrieb.de"  
# install deployer  
RUN curl -L -o /usr/local/bin/dep http://deployer.org/deployer.phar && \  
chmod +x /usr/local/bin/dep  
  
# install robo.li  
RUN curl -L -o /usr/local/bin/robo http://robo.li/robo.phar && \  
chmod +x /usr/local/bin/robo  
  
# regular php stuff  
RUN apt-get update && \  
apt-get install -y php5-fpm php5-cli php5-gd php5-json php5-ldap php5-mcrypt
php5-sqlite php5-xdebug php5-curl php5-ldap php5-mysqlnd php5-xsl php5-&& \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
rm -rf /var/lib/apt/lists/*  
  
#COPY 100-local-development.ini /etc/php5/fpm/conf.d  
COPY php-fpm.conf /etc/php5/fpm  
  
EXPOSE 9000  
RUN usermod -u 1000 www-data  
  
#ENTRYPOINT ["php5-fpm"]  
CMD ["php5-fpm", "-F"]  

