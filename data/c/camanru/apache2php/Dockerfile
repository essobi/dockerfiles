FROM debian:latest  
MAINTAINER Roman Zakharov <camanru@ya.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -y curl mc vim htop git openssh-server unzip wget &&\  
apt-get install -y apache2 php5 libapache2-mod-php5 &&\  
apt-get install -y sendmail &&\  
apt-get install -y php5-imagick php5-json php5-memcache php5-curl php5-mysql
php5-pgsql php5-mcrypt php5-gd &&\  
apt-get clean  
  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN echo ServerName localhost >> /etc/apache2/apache2.conf  
  
ADD apache-ports.conf /etc/apache2/ports.conf  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
EXPOSE 8080 443 25 21  
  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
CMD ["bash", "start.sh"]  
  
# CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]

