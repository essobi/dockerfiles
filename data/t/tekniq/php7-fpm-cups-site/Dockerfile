FROM ubuntu:14.04  
MAINTAINER Tyler Griesbach <tgriesbach@tekniq.com>  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# Add the ondrej php repo  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >
/etc/apt/sources.list.d/ondrej-php-trusty.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C  
  
RUN \  
apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends --no-
install-suggests install \  
php7.1 \  
php7.1-fpm \  
php7.1-gd \  
php7.1-apcu \  
php7.1-sqlite \  
php7.1-pgsql \  
php7.1-mysql \  
php7.1-intl \  
php7.1-simplexml \  
php7.1-sybase \  
php7.1-geoip \  
php7.1-gmp \  
php7.1-readline \  
php7.1-mcrypt \  
php7.1-xmlrpc \  
php7.1-json \  
php7.1-curl \  
php7.1-soap \  
php7.1-zip \  
php7.1-mbstring \  
php7.1-bcmath \  
php-pear \  
php-apcu-bc \  
ruby2.0 \  
ruby2.0-dev \  
build-essential \  
openssh-client \  
wget \  
curl \  
exim4 \  
cups \  
supervisor \  
&& curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get -f -y -q
install yarn nodejs \  
&& gem2.0 install sass --no-user-install \  
&& apt-get clean  
  
# Configure Exim4, our SMTP server  
RUN rm -rf /etc/exim4 && mkdir -p /etc/exim4  
ADD exim4.conf /etc/exim4/exim4.conf  
  
VOLUME ["/hosting_files"]  
  
EXPOSE 9000  
EXPOSE 25  
  
ADD run.sh /start  
RUN chmod +x /start  
  
ENTRYPOINT ["/start"]

