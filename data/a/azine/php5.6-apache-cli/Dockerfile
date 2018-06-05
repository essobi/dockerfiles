FROM ubuntu:16.04  
  
ENV TERM="xterm" \  
LANG='en_US.UTF-8' \  
LANGUAGE='en_US:en' \  
LC_ALL='en_US.UTF-8'  
  
RUN echo "Europe/Zurich" > /etc/timezone \  
# update package repositories  
&& apt-get update \  
# install some packages required for next step  
&& apt-get install -y wget software-properties-common tzdata debconf locales \  
# generate locales & set timezone  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure -f noninteractive tzdata \  
# add php5-repo and mysql-5.6 repos & update package repositories  
&& add-apt-repository -y ppa:ondrej/php \  
&& add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe' \  
&& apt-get update \  
&& apt-get upgrade -y \  
# install from package list & clear chache  
&& apt-get install -y \  
acl \  
apache2 \  
apache2-utils \  
bash-completion \  
curl \  
git \  
graphviz \  
imagemagick \  
libapache2-mod-php5.6 \  
libmagickwand-dev \  
libsqlite3-dev \  
php-common \  
php-file-iterator \  
php-geoip \  
php-gettext \  
php-imagick \  
php-pear \  
php-phpseclib \  
php-tcpdf \  
php-xdebug \  
php5.6 \  
php5.6-cli \  
php5.6-common \  
php5.6-curl \  
php5.6-dev \  
php5.6-gd \  
php5.6-intl \  
php5.6-json \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-mysql \  
php5.6-opcache \  
php5.6-readline \  
php5.6-sqlite3 \  
php5.6-xml \  
php5.6-zip \  
realpath \  
sqlite3 \  
ssl-cert \  
sudo \  
supervisor \  
unzip \  
vim \  
nano \  
wget \  
zip \  
&& apt-get clean  
  
# add apache php & xdebug configuration  
ADD config/php.ini /etc/php/5.6/cli/php.ini  
ADD config/php.ini /etc/php/5.6/apache2/php.ini  
ADD config/xdebug.ini /etc/php/5.6/mods-available/xdebug.ini  
ADD config/application.apache.conf /etc/apache2/sites-
available/000-application.conf  
ADD config/application-ssl.apache.conf /etc/apache2/sites-
available/000-application-ssl.conf  
  
RUN mkdir /app \  
# enable xdebug  
&& phpenmod -s ALL xdebug \  
# create ssl-cert, enable mod_ssl, mod_vhost_alias, mod_rewrite  
&& make-ssl-cert generate-default-snakeoil --force-overwrite \  
&& chmod -f a+rx /etc/ssl/private/* /etc/ssl/certs/* \  
&& a2enmod ssl vhost_alias rewrite \  
# enable the right apache vhosts  
&& a2dissite default-ssl.conf \  
&& a2dissite 000-default.conf \  
&& a2ensite 000-application-ssl.conf \  
&& a2ensite 000-application.conf  
  
  
# Docker Entrypoints  
COPY /docker-entrypoint.sh /  
COPY /docker-entrypoint.d /docker-entrypoint.d/  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# default-command  
CMD ["/bin/bash"]  
  
# initial directory when staring the container  
WORKDIR /app  
  
# exposed ports.  
EXPOSE 80 443 9000  

