FROM debian:latest  
MAINTAINER Curtis Baldwinson <curtisbaldwinson@gmail.com>  
  
# Apache2  
RUN apt-get clean && apt-get update && apt-get -y install apache2 wget  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN apt-get clean && apt-get update && apt-get upgrade -y  
RUN apt-get install -y apache2 python-software-properties  
  
# PHP 7  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list  
RUN echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list  
RUN wget https://www.dotdeb.org/dotdeb.gpg  
RUN apt-key add dotdeb.gpg  
RUN apt-get update  
RUN apt-get install -y php7.0 php7.0-common php-pear php7.0-mysql
php7.0-opcache php7.0-json php7.0-curl php7.0-gd php7.0-imap php7.0-ldap
php7.0-dev php7.0-cgi  
RUN apt-get install -y libapache2-mod-php7.0  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Enable mass dynamic virtual hosts  
RUN a2enmod rewrite  
RUN a2dissite 000-default  
RUN a2enmod vhost_alias  
ADD ./catchall /etc/apache2/sites-available/000-catchall.conf  
RUN a2ensite 000-catchall.conf  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

