# msphpsql  
# PHP runtime with sqlservr and pdo_sqlsrv to connect to SQL Server  
FROM ubuntu:16.04  
#MAINTAINER SQL Server Connectivity Team  
MAINTAINER Jonas De Kegel (jonas+docker@jlss.eu)  
  
# apt-get and system utilities  
RUN apt-get update && apt-get install -y \  
curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5\  
&& rm -rf /var/lib/apt/lists/*  
  
# adding custom MS repository  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# install SQL Server drivers  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y unixodbc-dev msodbcsql  
  
# install SQL Server tools  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
RUN /bin/bash -c "source ~/.bashrc"  
  
# php libraries  
RUN apt-get update && apt-get install -y \  
apache2 php7.0 libapache2-mod-php7.0 mcrypt php7.0-mcrypt php-mbstring php-
pear php7.0-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# install necessary locales  
RUN apt-get update && apt-get install -y locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen  
  
# install SQL Server PHP connector module  
RUN pecl install sqlsrv pdo_sqlsrv  
  
# initial configuration of SQL Server PHP connector  
#RUN echo "extension=/usr/lib/php/20151012/sqlsrv.so" >>
/etc/php/7.0/cli/php.ini  
#RUN echo "extension=/usr/lib/php/20151012/pdo_sqlsrv.so" >>
/etc/php/7.0/cli/php.ini  
RUN echo "extension=pdo_sqlsrv.so" >>
/etc/php/7.0/apache2/conf.d/30-pdo_sqlsrv.ini  
RUN echo "extension=sqlsrv.so" >> /etc/php/7.0/apache2/conf.d/20-sqlsrv.ini  
  
# install additional utilities  
RUN apt-get update && apt-get install gettext nano vim -y  
  
# add sample code  
RUN mkdir /code  
ADD . /code  
WORKDIR /code  
  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND", "-k", "start" ,"-e", "debug"]  
  
#enable rewriteengine  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y php-ldap php-gd php-soap  
  
# enable overrides  
#RUN sed -i -e 's/None/All/g' /etc/apache2/apache2.conf  
RUN echo '<Directory "/var/www/html">\n\  
allow from all\n\  
Options IncludesNOEXEC FollowSymLinks\n\  
Require all granted\n\  
AllowOverride None\n\  
</Directory>\n\  
RewriteEngine On\n\  
<DirectoryMatch "/var/www/html/.*/">\n\  
RewriteCond %{REQUEST_FILENAME} !-f\n\  
RewriteCond %{REQUEST_FILENAME} !-d\n\  
RewriteCond $1 !^(index\\.php|images|assets|sass|js|robots\\.txt)\n\  
RewriteRule ^/var/www/html/(.*?)/(.*)$ /var/www/html/$1/index.php/$2 [L]\n\  
</DirectoryMatch>' >> /etc/apache2/apache2.conf  

