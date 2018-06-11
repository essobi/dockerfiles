FROM php:fpm  
  
MAINTAINER Wilton Garcia <wiltonog@gmail.com>  
  
RUN apt-get update && apt-get install -y unixodbc libgss3 odbcinst devscripts
debhelper dh-exec dh-autoreconf \  
libreadline-dev libltdl-dev unixodbc-dev wget unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo  
  
RUN cd /usr/local/src/ && dget -ux
http://http.debian.net/debian/pool/main/u/unixodbc/unixodbc_2.3.1-3.dsc \  
&& cd unixodbc-2.3.1/ && apt-get update && dpkg-buildpackage -uc -d -us -B &&
cp ./exe/odbc_config /usr/local/bin/  
  
RUN cd /usr/local/src/ \  
&& wget
"https://meetsstorenew.blob.core.windows.net/contianerhd/Ubuntu%2013.0%20Tar/msodbcsql-13.0.0.0.tar.gz?st=2016-10-18T17%3A29%3A00Z&se=2022-10-19T17%3A29%3A00Z&sp=rl&sv=2015-04-05&sr=b&sig=cDwPfrouVeIQf0vi%2BnKt%2BzX8Z8caIYvRCmicDL5oknY%3D"
-O msodbcsql-13.0.0.0.tar.gz \  
&& tar xf msodbcsql-13.0.0.0.tar.gz && cd msodbcsql-13.0.0.0/ \  
&& ldd lib64/libmsodbcsql-13.0.so.0.0; echo "RET=$?" \  
&& sed -i 's/$(uname -p)/"x86_64"/g' ./install.sh \  
&& ./install.sh install --force --accept-license  
  
RUN pecl install pdo_sqlsrv && docker-php-ext-enable pdo_sqlsrv  
  
# Install xdebug  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
# Install Redis  
RUN pecl install redis && docker-php-ext-enable redis  
  
RUN apt-get install -y locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen  
  
RUN groupadd -r php -g 1000 && useradd -u 1000 -r -g php -m -d /var/www/html
-s /sbin/nologin -c "App user" php  
  

