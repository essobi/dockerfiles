FROM phusion/baseimage:latest  
  
LABEL maintainer="Harvey Chow <harvey@hcdesigns.nl>"  
  
RUN DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
locales \  
software-properties-common \  
python-software-properties \  
pkg-config \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
git \  
vim \  
nano  
  
#####################################  
# Install python (required for several npm builds)  
#####################################  
RUN apt-get install -y python  
  
#####################################  
# Set locales and set timezone  
#####################################  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
RUN ln -snf /usr/share/zoneinfo/CEST /etc/localtime && echo CEST >
/etc/timezone  
  
#####################################  
# PHP 7.1  
#####################################  
# Add the "PHP 7" ppa (after locales setting)  
RUN add-apt-repository ppa:ondrej/php && \  
apt-get update  
  
# Install "PHP Extentions", "libraries", "Software's"  
RUN apt-get install -y \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-intl \  
php7.1-json \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-zip \  
php7.1-bcmath \  
php7.1-memcached \  
php7.1-gd \  
php7.1-dev \  
php7.1-soap  
  
#####################################  
# Non-Root User:  
#####################################  
# Add a non-root user to prevent files being created with root permissions on
host machine.  
ENV PUID 1000  
ENV PGID 1000  
  
RUN groupadd -g ${PGID} hcdesigns && \  
useradd -u ${PUID} -g hcdesigns -m hcdesigns  
  
#####################################  
# Composer:  
#####################################  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
  
#####################################  
# Python, NodeJS, yarn  
#####################################  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - &&\  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - &&\  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && \  
apt-get install -y nodejs yarn  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
  
# Clean up  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set default work directory  
WORKDIR /var/www

