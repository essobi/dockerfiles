FROM debian:latest  
MAINTAINER Camille Baronnet <git@camillebaronnet.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install apache2 php5 php5-mysql libapache2-mod-php5 php5-curl
php5-gd php5-mcrypt ssmtp cron curl locales && \  
apt-get clean && \  
rm -R /var/www && \  
rm -R /etc/apache2/sites-available && rm /etc/apache2/sites-enabled/*  
  
COPY ./locales /etc/locale.gen  
RUN locale-gen  
  
COPY ./home /home  
COPY ./default.vhost /etc/apache2/sites-enabled/000-default  
COPY ./apache2.conf /etc/apache2/apache2.conf  
  
RUN a2enmod rewrite && a2dismod autoindex -f  
  
RUN rm /etc/ssmtp/ssmtp.conf && ln -s /home/conf/ssmtp.conf /etc/ssmtp/  
RUN rm /etc/crontab && ln -s /home/conf/crontab.conf /etc/crontab  
RUN rm /etc/php5/cli/php.ini && ln -s /home/conf/php.ini /etc/php5/cli/  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_USER_UID 0  
RUN mkdir -p /etc/apache2/conf.d/ && \  
touch /etc/apache2/conf.d/server.conf && \  
touch /etc/apache2/conf.d/security  
  
RUN echo "ServerName localhost" > /etc/apache2/conf.d/server.conf && \  
sed -i 's/expose_php = On/expose_php = Off/' /etc/php5/apache2/php.ini && \  
sed -i 's/ServerSignature On/ServerSignature Off/'
/etc/apache2/conf.d/security && \  
sed -i 's/ServerTokens OS/ServerTokens Prod/' /etc/apache2/conf.d/security  
  
COPY ./startup.sh /root/startup.sh  
  
EXPOSE 80  
VOLUME ["/home"]  
ENTRYPOINT ["/root/startup.sh"]  
CMD ["/usr/sbin/apache2 -D FOREGROUND"]  

