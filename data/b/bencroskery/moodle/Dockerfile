# REQUIRED FILES TO BUILD THIS IMAGE  
# ----------------------------------  
# (1) oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm  
# (2) oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm  
# Download Oracle Instant Client for Linux x64  
# from http://www.oracle.com/technetwork/database/features/instant-
client/index-097480.html  
FROM centos:7  
MAINTAINER Ben Croskery <ben@irtech.com>  
LABEL Description="PHP 5.4 + Moodle." \  
License="Apache License 2.0" \  
Usage="docker run -d -p [HOST PORT NUMBER]:80 -v [HOST WWW DOCUMENT
ROOT]:/var/www/html bencroskery/moodle:php54" \  
Version="1.0"  
  
# Install Apache, PHP, GIT  
RUN yum update -y  
RUN yum install -y httpd  
RUN yum install -y \  
php \  
php-common \  
php-mysql \  
php-pgsql \  
php-gd \  
php-intl \  
php-mbstring \  
php-soap \  
php-xml \  
php-xmlrpc \  
php-devel \  
php-pear \  
gcc \  
make \  
git  
RUN yum clean all  
  
# Install PHP Oracle connector  
ADD ./oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm /tmp/oracle-
instantclient-basic.rpm  
ADD ./oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm /tmp/oracle-
instantclient-devel.rpm  
RUN yum install -y /tmp/oracle-instantclient-basic.rpm  
RUN yum install -y /tmp/oracle-instantclient-devel.rpm  
RUN rm -R /tmp/oracle-instantclient-*  
  
RUN pecl install oci8-2.0.10  
RUN echo 'extension=oci8.so' >> /etc/php.ini  
  
# Environment options.  
ENV INSTALL **Boolean**  
  
# Add scripts.  
COPY pullMoodle.sh runServer.sh /usr/local/bin/  
  
VOLUME /var/www/html  
  
EXPOSE 80  
CMD ["runServer.sh"]

