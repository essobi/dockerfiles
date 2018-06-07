# DbFace On-premises  
#  
# VERSION 7.6 (20180526)  
FROM ubuntu:16.04  
MAINTAINER DbFace "support@dbface.com"  
# Upgrade system  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
RUN apt-get update  
  
# Setup system and install tools  
RUN apt-get -qqy install passwd supervisor sudo unzip wget curl cron apt-
transport-https  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add
-  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/mssql-
server-2017.list | sudo tee /etc/apt/sources.list.d/mssql-server-2017.list  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo
tee /etc/apt/sources.list.d/mssql-tools.list  
  
RUN apt-get -qqy update  
RUN ACCEPT_EULA=Y apt-get -qqy install mssql-tools  
RUN sudo apt-get -qqy install unixodbc-dev  
  
# Setup ssh  
RUN apt-get -qqy install openssh-server  
RUN mkdir -p /var/run/sshd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN echo 'root:root' | chpasswd  
  
# Generate a host key before packing.  
RUN service ssh start; service ssh stop  
  
# Create SSL cert  
RUN mkdir /root/ssl; \  
openssl genrsa -out /root/ssl/local.key 1024; \  
openssl req -new -key /root/ssl/local.key -out /root/ssl/local.csr -subj
"/C=DE/ST=BW/L=FREIBURG/O=Jankowfsky AG/OU=Development/CN=localhost"; \  
openssl x509 -req -days 365 -in /root/ssl/local.csr -signkey
/root/ssl/local.key -out /root/ssl/local.crt  
  
# Install apache  
RUN apt-get -qqy install apache2 apache2-utils  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN mkdir -p /etc/apache2/conf.d/  
RUN echo "ServerName localhost" | tee /etc/apache2/conf.d/fqdn  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
ADD conf/apache/000-default /etc/apache2/sites-enabled/000-default.conf  
  
# Install php  
RUN apt-get -qqy install php-pear php7.0 mcrypt php7.0-mcrypt php7.0-dev
php7.0-cli php7.0-mysql php7.0-sqlite php7.0-interbase php7.0-pgsql
php7.0-curl php7.0-mbstring php7.0-gd php7.0-xml libapache2-mod-php7.0  
  
RUN apt-get -qqy install libssl-dev pkg-config libaio-dev  
  
# MongoDB support  
RUN pecl install mongodb && \  
echo "extension=mongodb.so" >> /etc/php/7.0/cli/php.ini && \  
echo "extension=mongodb.so" >> /etc/php/7.0/apache2/php.ini  
  
# SQL Server Support  
RUN pecl install sqlsrv pdo_sqlsrv && \  
echo "extension= pdo_sqlsrv.so" >> /etc/php/7.0/cli/php.ini && \  
echo "extension= pdo_sqlsrv.so" >> /etc/php/7.0/apache2/php.ini && \  
echo "extension= sqlsrv.so" >> /etc/php/7.0/cli/php.ini && \  
echo "extension= sqlsrv.so" >> /etc/php/7.0/apache2/php.ini  
  
# Install Oracle Instantclient  
RUN mkdir /opt/oracle \  
&& cd /opt/oracle \  
&& wget https://s3-ap-southeast-1.amazonaws.com/download-dbface/instantclient-
basiclite-linux.x64-12.2.0.1.0.zip \  
&& wget https://s3-ap-southeast-1.amazonaws.com/download-dbface/instantclient-
sdk-linux.x64-12.2.0.1.0.zip \  
&& unzip /opt/oracle/instantclient-basiclite-linux.x64-12.2.0.1.0.zip -d
/opt/oracle \  
&& unzip /opt/oracle/instantclient-sdk-linux.x64-12.2.0.1.0.zip -d /opt/oracle
\  
&& ln -s /opt/oracle/instantclient_12_2/libclntsh.so.12.1
/opt/oracle/instantclient_12_2/libclntsh.so \  
&& ln -s /opt/oracle/instantclient_12_2/libclntshcore.so.12.1
/opt/oracle/instantclient_12_2/libclntshcore.so \  
&& ln -s /opt/oracle/instantclient_12_2/libocci.so.12.1
/opt/oracle/instantclient_12_2/libocci.so \  
&& rm -rf /opt/oracle/*.zip  
  
RUN echo 'instantclient,/opt/oracle/instantclient_12_2/' | pecl install oci8
&& \  
echo "extension= oci8.so" >> /etc/php/7.0/cli/php.ini && \  
echo "extension= oci8.so" >> /etc/php/7.0/apache2/php.ini  
  
# Download ioncube loader  
RUN cd /var/www/html && \  
wget http://s3-ap-southeast-1.amazonaws.com/download-
dbface/ioncube_loaders_lin_x86-64.tar.gz && \  
tar zxvf ioncube_loaders_lin_x86-64.tar.gz && \  
rm ioncube_loaders_lin_x86-64.tar.gz && \  
echo "zend_extension = /var/www/html/ioncube/ioncube_loader_lin_7.0.so" >>
/etc/php/7.0/apache2/php.ini && \  
echo "zend_extension = /var/www/html/ioncube/ioncube_loader_lin_7.0.so" >>
/etc/php/7.0/cli/php.ini  
  
RUN rm -rf /var/www/index.html  
RUN wget https://s3-ap-southeast-1.amazonaws.com/download-
dbface/v8/dbface_php5.6.zip -O /tmp/dbfacephp.zip && unzip -d /var/www
/tmp/dbfacephp.zip && rm /tmp/dbfacephp.zip  
  
RUN chown -R www-data:www-data /var/www  
RUN chmod -R 755 /var/www/user  
  
# crontab  
# steup crontab 5min  
# Add crontab file in the cron directory  
ADD conf/dbface /etc/cron.d/dbface  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/dbface  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cronlog.log  
  
# Run  
# Add supervisor config  
ADD conf/supervisor/startup.conf /etc/supervisor/conf.d/startup.conf  
  
ADD conf/scripts/startup.sh /usr/bin/startup_container  
RUN chmod +x /usr/bin/startup_container  
  
# Cleanup  
RUN apt-get clean -y; \  
apt-get autoclean -y; \  
apt-get autoremove -y; \  
rm -rf /var/www/index.html; \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
VOLUME /var/www/user  
EXPOSE 22 80 443  
CMD ["/bin/bash", "/usr/bin/startup_container"]  

