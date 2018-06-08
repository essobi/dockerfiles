FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C  
  
RUN echo 'deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main' >>
/etc/apt/sources.list && \  
apt-get -y -q update && \  
apt-get -y -q install apt-utils build-essential curl wget locales git vim && \  
apt-get -y -q install --no-install-recommends libxrender1 php7.1 php7.1-apcu
php7.1-apcu-bc php7.1-bcmath php7.1-cgi php7.1-cli php7.1-common php7.1-curl
php7.1-dev php7.1-fpm php7.1-gd php7.1-imagick php7.1-imap php7.1-intl
php7.1-json php7.1-ldap php7.1-mcrypt php7.1-memcached php7.1-mysqlnd
php7.1-pgsql php7.1-readline php7.1-sybase php7.1-xmlrpc php7.1-xsl
php7.1-mbstring php7.1-soap php-xdebug php7.1-zip php7.1 libapache2-mod-php7.1
&& \  
apt-get -y -q install nodejs -y && \  
apt-get install -y -q ruby-dev && \  
apt-get -y -q install npm && \  
mkdir -p /run/php/ && \  
apt-get -y -q autoremove && \  
apt-get -y -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require hirak/prestissimo  
  
RUN mkdir -p /tmp/wkhtml && cd /tmp/wkhtml && \  
wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
tar vxf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
cp wkhtmltox/bin/wk* /usr/local/bin/ && rm -rf /tmp/wkhtml  
  
RUN echo Europe/Brussels > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN locale-gen nl_BE && \  
locale-gen fr_BE && \  
locale-gen en_GB && \  
locale-gen es_ES && \  
locale-gen nl_NL && \  
locale-gen fr_FR && \  
locale-gen en_US && \  
locale-gen nl_BE.UTF-8 && \  
locale-gen fr_BE.UTF-8 && \  
locale-gen en_GB.UTF-8 && \  
locale-gen es_ES.UTF-8 && \  
locale-gen nl_NL.UTF-8 && \  
locale-gen fr_FR.UTF-8 && \  
locale-gen en_US.UTF-8  
  
COPY ./configs/opcache.ini /etc/php/7.1/mods-available/opcache.ini  
RUN phpenmod opcache  
  
COPY ./configs/apcu.ini /etc/php/7.1/mods-available/apcu.ini  
RUN phpenmod apcu  
  
COPY ./configs/php_conf.ini /etc/php/7.1/mods-available/php_conf.ini  
RUN phpenmod php_conf  
  
COPY ./configs/xdebug.ini /etc/php/7.1/mods-available/xdebug.ini  
RUN phpdismod xdebug  
  
COPY ./configs/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
  
EXPOSE 9000  
COPY ./configs/run.sh /scripts/run.sh  
RUN chmod -R 755 /scripts  
  
CMD ["/scripts/run.sh", "php-fpm7.1"]  
  
WORKDIR /app  

