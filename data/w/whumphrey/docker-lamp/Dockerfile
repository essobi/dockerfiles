FROM ubuntu:trusty  
#FROM phusion/baseimage:0.9.10  
MAINTAINER Wayne Humphrey <wayne@humphrey.za.net>  
  
LABEL version="1.0"  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV NOTVISIBLE "in users profile"  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
RUN apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen php-apc php5-mcrypt php5-curl php5-gd openssh-server mlocate
&& \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Add image configuration and scripts  
ADD scripts/start-apache.sh /etc/supervisor/start-apache.sh  
ADD scripts/start-mysql.sh /etc/supervisor/start-mysql.sh  
ADD scripts/mysql_init.sh /mysql_init.sh  
ADD scripts/init /sbin/init  
ADD configs/config-mysql.cnf /etc/mysql/conf.d/my.cnf  
ADD configs/config-apache.cnf /etc/apache2/sites-available/000-default.conf  
#ADD configs/sv-apache.cnf /etc/supervisor/conf.d/apache.conf  
#ADD configs/sv-mysql.cnf /etc/supervisor/conf.d/mysql.conf  
ADD configs/supervisord.conf /etc/supervisor/supervisord.conf  
RUN chmod 755 /sbin/init  
RUN chmod 755 /mysql_init.sh  
RUN chmod 755 /etc/supervisor/*.sh  
  
#COPY  
#ENTRYPOINT  
#USER  
#WORKDIR  
#ARG  
#ONBUILD  
#STOPSIGNAL  
#HEALTHCHECK  
#SHELL  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# config to enable .htaccess  
RUN a2enmod rewrite  
  
# Configure /app folder with sample app  
RUN rm -fr /var/www/html/* && git clone https://github.com/nitr8/hello-world-
lamp.git /var/www/html/  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 25M  
ENV PHP_POST_MAX_SIZE 25M  
  
# SSH login fix  
RUN mkdir /var/run/sshd  
RUN echo 'root:toor' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Add volumes for MySQL  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/www/html/" ]  
  
EXPOSE 22 80 3306 9001  
# Use baseimage-docker's init system.  
CMD ["/sbin/init"]  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

