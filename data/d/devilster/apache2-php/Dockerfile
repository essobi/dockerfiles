FROM phusion/baseimage  
  
LABEL maintainer="Devil.Ster.1"  
LABEL version="1.0.1"  
  
ARG PHP_VER=7.0  
ENV DEBIAN_FRONTEND noninteractive  
  
# START Locales Install  
RUN apt-get update && apt-get install -y --no-install-recommends \  
locales && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
# END Locales Install  
ENV TERM xterm  
  
# START Install Apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV WEB_DOCUMENT_ROOT /var/www/  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
\--allow-downgrades --allow-remove-essential --allow-change-held-packages \  
apache2 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# END Install Apache2  
# START Configure Apache2  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
RUN mkdir /etc/apache2/ssl  
COPY ssl-certs /etc/apache2/ssl  
  
COPY apache-default-sites /etc/apache2/sites-available  
RUN a2ensite default-ssl  
  
# Autostart  
RUN mkdir /etc/service/apache  
ADD apache_start.sh /etc/service/apache/run  
RUN chmod +x /etc/service/apache/run  
# END Configure Apache2  
# START Install Additional Soft  
RUN apt-get update && apt-get install -y --no-install-recommends \  
\--allow-downgrades --allow-remove-essential --allow-change-held-packages \  
wget \  
mcrypt \  
curl \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# END Install Additional Soft  
# START PHP INSTALL  
RUN apt-get update && apt-get install -y software-properties-common && add-
apt-repository -y ppa:ondrej/php  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
\--allow-downgrades --allow-remove-essential --allow-change-held-packages \  
libapache2-mod-php$PHP_VER \  
php$PHP_VER \  
php$PHP_VER-common \  
php$PHP_VER-cli \  
php$PHP_VER-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# END PHP INSTALL  
# START PHP Modules Install  
RUN apt-get update && apt-get install -y --no-install-recommends \  
\--allow-downgrades --allow-remove-essential --allow-change-held-packages \  
php$PHP_VER-curl \  
php$PHP_VER-xmlrpc \  
php$PHP_VER-pspell \  
php$PHP_VER-gd \  
php$PHP_VER-pdo \  
php$PHP_VER-mbstring \  
php$PHP_VER-soap \  
php$PHP_VER-xml \  
php$PHP_VER-zip \  
php$PHP_VER-bcmath \  
php$PHP_VER-bz2 \  
php$PHP_VER-calendar \  
php$PHP_VER-opcache \  
php$PHP_VER-gettext \  
php$PHP_VER-iconv \  
php$PHP_VER-ldap \  
php$PHP_VER-odbc \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN if [ "$PHP_VER" = "7.2" ]; \  
then echo "7.2 DOES NOT SUPPORT PHP_MCRYPT YET"; \  
else \  
apt-get update && \  
apt-get install -y --no-install-recommends php$PHP_VER-mcrypt \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
fi  
  
COPY pages/* /var/www/html/.  
# END PHP Modules Install  
# START Composer Install  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
# END Composer Install  
WORKDIR /var/www  
  
EXPOSE 80  
EXPOSE 443  

