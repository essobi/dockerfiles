#  
#--------------------------------------------------------------------------  
# Image Setup  
#--------------------------------------------------------------------------  
#  
FROM phusion/baseimage:latest  
  
  
MAINTAINER Melchor O. Abcede <melchor.abcede@loannotify.com>  
  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
  
# Add the "PHP 7" ppa  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Install "PHP Extentions", "libraries", "Software's"  
RUN apt-get update && \  
apt-get install -y --force-yes \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-json \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-sqlite \  
php7.1-sqlite3 \  
php7.1-zip \  
php7.1-memcached \  
php7.1-gd \  
php7.1-dev \  
pkg-config \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
libsqlite3-dev \  
sqlite3 \  
git \  
curl \  
vim \  
nano \  
postgresql-client \  
&& apt-get clean  
  
RUN apt-get -y install php7.1 mcrypt php7.1-mcrypt php-mbstring php-pear
php7.1-dev php7.1-xml  
  
#Set up pre requisite  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
ENV ACCEPT_EULA=Y  
  
  
RUN apt-get update  
RUN apt-get -y install msodbcsql mssql-tools  
RUN apt-get -y install unixodbc-dev  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
RUN echo 'source ~/.bashrc'  
  
RUN pear config-set php_ini `php --ini | grep "Loaded Configuration" | sed -e
"s|.*:\s*||"` system  
RUN pecl install sqlsrv  
RUN pecl install pdo_sqlsrv  
  
#####################################  
# Composer:  
#####################################  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
  
# Source the bash  
RUN . ~/.bashrc  
  

