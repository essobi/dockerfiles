FROM ubuntu:14.04  
MAINTAINER Eugene Ware <eugene@noblesamurai.com>  
  
RUN locale-gen en_US.UTF-8  
RUN export LANG=en_US.UTF-8  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Add APT repo  
RUN apt-get update  
RUN apt-get install -yy software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:ondrej/php  
RUN apt-get update  
RUN apt-get -y --force-yes upgrade  
  
# Basic Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install python-
setuptools curl git unzip vim-tiny  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install mysql-server
mysql-client apache2 libapache2-mod-php5.6 php5.6-mysql php-apc  
  
# Wordpress Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install php5.6-curl
php5.6-gd php5.6-intl php5.6-mbstring php-pear php5.6-imagick php5.6-imap
php5-mcrypt php5.6-memcache php5.6-ps php5.6-pspell php5.6-recode
php5.6-sqlite php5-tidy php5.6-xmlrpc php5.6-xsl php-pear  
  
# Mail function  
RUN DEBIAN_FRONTEND=noninteractive pear install Mail Net_SMTP Auth_SASL
Mail_Mime  
  
# mysql config  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
RUN chmod 664 /etc/mysql/conf.d/my.cnf  
  
# apache config  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN chown -R www-data:www-data /var/www/  
  
# php config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/5.6/apache2/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/5.6/apache2/php.ini  
RUN sed -i -e "s/short_open_tag\s*=\s*Off/short_open_tag = On/g"
/etc/php/5.6/apache2/php.ini  
RUN sed -i -e 's/;opcache.enable/opcache.enable/' /etc/php/5.6/apache2/php.ini  
  
# fix for php5-mcrypt and mod_rewrite  
RUN /usr/sbin/php5enmod mcrypt  
RUN /usr/sbin/a2enmod rewrite  
RUN curl -o /etc/apache2/apache2.conf
https://raw.githubusercontent.com/vmgamer/docker-apache-
php/master/apache2.conf  
  
# Supervisor Config  
RUN mkdir /var/log/supervisor/  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
  
# Initialization Startup Script  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
EXPOSE 3306  
EXPOSE 80  
# volume to preserve files  
VOLUME ["/var/lib/mysql"]  
  
CMD ["/bin/bash", "/start.sh"]  

