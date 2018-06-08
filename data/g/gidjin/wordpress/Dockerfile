FROM debian:jessie  
MAINTAINER John Gedeon <js1@gedeons.com>  
  
# let debian know we are not interactive  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get -yq install curl php5 php5-cli php5-cgi php5-gd php5-mysql sudo \  
libphp-phpmailer libjs-cropper libjs-mediaelement php-getid3 \  
apache2 libapache2-mod-php5 mysql-client msmtp msmtp-mta ruby cron && \  
gem install daemons faraday whenever  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download wp-cli  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar  
# Install wp-cli  
RUN mv wp-cli.phar /usr/local/bin/wp  
RUN chmod +x /usr/local/bin/wp  
  
RUN rm /var/www/html/index.html  
RUN chown -R www-data:www-data /var/www/html  
WORKDIR /var/www/html  
RUN runuser -u www-data -- /usr/local/bin/wp core download  
  
# add utilities  
COPY bin/* /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
COPY schedule.rb /usr/local/lib/  
RUN whenever -u root -w -f /usr/local/lib/schedule.rb  
# COPY lib/* /usr/local/lib/  
# RUN /usr/local/bin/update_wp_config.sh  
COPY msmtprc.ini /etc/php5/apache2/conf.d/  
COPY templates /templates  
RUN mkdir /database-backups  
RUN chown www-data:www-data /database-backups  
RUN chmod 755 /database-backups  
  
VOLUME ["/database-backups", "/var/www/html/wp-content"]  
  
ENTRYPOINT ["/usr/local/bin/init.sh"]  
  
CMD ["/usr/sbin/apachectl -DFOREGROUND"]  

