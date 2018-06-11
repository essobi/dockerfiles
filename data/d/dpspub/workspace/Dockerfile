FROM phusion/baseimage:latest  
  
MAINTAINER Thomas Albrighton <tom@dps.com.au>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
# Add the "PHP 7" ppa  
RUN add-apt-repository -y \  
ppa:ondrej/php  
  
# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT  
RUN apt-get update && apt-get install -y --force-yes \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-json \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite \  
php7.0-sqlite3 \  
php7.0-sybase \  
php7.0-zip \  
php7.0-gd \  
php7.0-xdebug \  
php-dev \  
python \  
libcurl4-openssl-dev \  
libedit-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
sqlite3 \  
libsqlite3-dev \  
git \  
curl \  
vim \  
nano \  
unzip \  
gnupg2 \  
  
&& apt-get clean  
  
# remove load xdebug extension (only load on phpunit command)  
RUN sed -i 's/^/;/g' /etc/php/7.0/cli/conf.d/20-xdebug.ini  
  
# Add bin folder of composer to PATH.  
RUN echo "export PATH=${PATH}:/var/www/laravel/vendor/bin" >> ~/.bashrc  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Load xdebug Zend extension with phpunit command  
RUN echo "alias phpunit='php -dzend_extension=xdebug.so
/var/www/laravel/vendor/bin/phpunit'" >> ~/.bashrc  
  
# Install stable node  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
COPY bash_aliases /root/.bash_aliases  
  
# Source the bash  
RUN . ~/.bashrc  
RUN chsh --shell /bin/bash  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -O https://storage.googleapis.com/kubernetes-
release/release/v1.3.3/bin/linux/amd64/kubectl \  
&& chmod +x kubectl \  
&& mv kubectl /usr/local/bin/kubectl  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "/tmp/awscli-
bundle.zip" \  
&& unzip /tmp/awscli-bundle.zip -d /tmp \  
&& /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& rm /tmp/awscli-bundle.zip \  
&& rm -R /tmp/awscli-bundle  
  
RUN gpg2 --keyserver pgp.mit.edu --recv-key FC8A365E \  
&& gpg2 --fingerprint FC8A365E \  
&& curl -L "https://github.com/coreos/coreos-
kubernetes/releases/download/v0.8.0/kube-aws-linux-amd64.tar.gz" -o
"/tmp/kube-aws-linux-amd64.tar.gz" \  
&& curl -L "https://github.com/coreos/coreos-
kubernetes/releases/download/v0.8.0/kube-aws-linux-amd64.tar.gz.sig" -o
"/tmp/kube-aws-linux-amd64.tar.gz.sig" \  
&& gpg2 --verify /tmp/kube-aws-linux-amd64.tar.gz.sig /tmp/kube-aws-linux-
amd64.tar.gz \  
&& tar zxvf /tmp/kube-aws-linux-amd64.tar.gz -C /tmp \  
&& mv /tmp/linux-amd64/kube-aws /usr/local/bin \  
&& rm /tmp/kube-aws-linux-amd64.tar.gz /tmp/kube-aws-linux-amd64.tar.gz.sig \  
&& rm -R /tmp/linux-amd64  
  
WORKDIR /var/www/laravel  
  
# RUN export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \  
# && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \  
# && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
# && mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so \  
# && printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
# Install optional software  
ARG INSTALL_PRESTISSIMO=false  
RUN if [ "$INSTALL_PRESTISSIMO" = true ] ; then \  
composer global require "hirak/prestissimo:^0.3"; \  
fi

