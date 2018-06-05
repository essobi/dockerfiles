FROM php:7.0-apache  
MAINTAINER Tim Woodby<timwoodby@gmail.com>  
  
LABEL php_version="7.0.8" \  
instantclient_version="12.1.0.2.0"  
  
#
------------------------------------------------------------------------------  
# The basic Install Update and setup of PHP  
#
------------------------------------------------------------------------------  
RUN apt-get update && \  
apt-get install -y alien=8.92 \  
php-pear=5.6.23+dfsg-0+deb8u1 \  
libaio1=0.3.110-1 && \  
apt-get clean -y  
  
#
------------------------------------------------------------------------------  
# Install the OCI8 Oracle Client  
#
------------------------------------------------------------------------------  
ADD oracle-instantclient12.1-*.rpm /tmp/  
RUN alien -i /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm && \  
alien -i /tmp/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm && \  
alien -i /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm && \  
echo 'instantclient,/usr/lib/oracle/12.1/client64/lib' | pecl install
oci8-2.1.1 && \  
mkdir -p /usr/local/etc/php/conf.d && \  
echo "extension=oci8.so" > /usr/local/etc/php/conf.d/oci8.ini && \  
echo '/usr/lib/oracle/12.1/client64/lib/' > /etc/ld.so.conf.d/oracle.conf && \  
chmod o+r /etc/ld.so.conf.d/oracle.conf && \  
ldconfig  

