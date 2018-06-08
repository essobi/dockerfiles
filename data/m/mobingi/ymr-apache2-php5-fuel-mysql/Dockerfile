FROM ubuntu:14.04  
MAINTAINER david.siaw@mobingi.com  
  
RUN apt-get update  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
  
RUN apt-get install -y apache2  
RUN mkdir -p /var/lock/apache2 /var/run/apache2  
  
RUN apt-get install -y curl git php5 libapache2-mod-php5 php5-cli php5-dev
php5-mysql php5-xmlrpc php5-curl php5-gd php-apc php-pear php5-imap
php5-mcrypt php5-pspell php5-redis  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN curl get.fuelphp.com/oil | sh  
  
RUN apt-get install -y phpMyAdmin  
RUN echo "Include /etc/phpmyadmin/apache.conf" >> /etc/apache2/apache2.conf  
  
COPY config-db.php /etc/phpmyadmin/config-db.php  
COPY config.inc.php /etc/phpmyadmin/config.inc.php  
  
RUN a2enmod rewrite  
RUN php5enmod mcrypt  
  
ADD run.sh /run.sh  
ADD startup.sh /startup.sh  
RUN chmod 755 /*.sh  
  
RUN locale-gen ja_JP.UTF-8  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
COPY config /config  
COPY sudoers /etc/sudoers  
  
COPY token.enc /token.enc  
COPY passphrase /passphrase  
  
ENV FUEL_ENV production  
  
EXPOSE 22 80  
CMD ["/run.sh"]  

