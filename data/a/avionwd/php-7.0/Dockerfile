#  
# Phalcon Application Core  
#  
# Pull base image  
FROM debian:8  
WORKDIR /var/www/phalcon  
  
# Set up the application directory  
VOLUME ["/var/www/phalcon"]  
  
RUN echo "START!..."  
  
RUN apt-get update && apt-get install -y \  
wget \  
curl \  
apt-utils \  
upstart \  
vim \  
git \  
monit \  
locales \  
zip \  
unzip \  
gzip \  
amqp-tools \  
cron \  
build-essential  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list
\  
&& echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list \  
&& cd /usr/local/src \  
&& wget https://www.dotdeb.org/dotdeb.gpg \  
&& apt-key add dotdeb.gpg  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main 9.5"
>> /etc/apt/sources.list.d/postgresql.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
RUN apt-get install -y postgresql-client  
  
# Install phalcon  
RUN curl -s
https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh |
bash  
  
# Install PHP 7.0  
RUN apt-get install -y php7.0-fpm php7.0-cli php7.0-phalcon php7.0-redis \  
php7.0-pgsql php7.0-mcrypt php7.0-gd php7.0-curl \  
php7.0-memcache php7.0-geoip php7.0-json php7.0-xsl \  
php7.0-soap php7.0-bcmath php7.0-mbstring php7.0-xdebug \  
php7.0-zip  
  
RUN locale  
RUN dpkg-reconfigure locales  
RUN export LANGUAGE="en_US.UTF-8" && export LANG="en_US.UTF-8" && export
LC_ALL="en_US.UTF-8"  
RUN locale-gen uk_UA.UTF-8 && locale-gen ru_RU.UTF-8  
RUN echo "UTC" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# Install global packages for npm  
RUN npm install -g bower grunt-cli  
  
# Install PHP composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php7.0 -r "unlink('composer-setup.php');"  
  
# Clean all data  
RUN cd /tmp \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/var/log \  
/var/cache  
  
EXPOSE 9000  
EXPOSE 9001

