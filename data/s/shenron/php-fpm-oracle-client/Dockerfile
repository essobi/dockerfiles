FROM shenron/php-fpm:7.2  
  
ENV LD_LIBRARY_PATH /usr/local/instantclient_12_1/  
  
RUN apt-get update && \  
apt-get install -y \  
unzip \  
libaio-dev  
  
# install oracle client  
COPY /conf/ /tmp/  
  
RUN unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/ &&
\  
unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/ && \  
unzip /tmp/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip -d /usr/local/ && \  
ln -s /usr/local/instantclient_12_1 /usr/local/instantclient && \  
ln -s /usr/local/instantclient/libclntsh.so.12.1
/usr/local/instantclient/libclntsh.so && \  
ln -s /usr/local/instantclient/sqlplus /usr/bin/sqlplus && \  
rm /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/instantclient-sdk-
linux.x64-12.1.0.2.0.zip /tmp/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip
&&\  
echo 'instantclient,/usr/local/instantclient' | pecl install oci8 && \  
echo "extension=oci8.so" >> /usr/local/etc/php/php.ini  

