FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Configured timezone.  
ENV TZ=Australia/Adelaide  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Ensure UTF-8.  
ENV LANG en_AU.UTF-8  
ENV LC_ALL en_AU.UTF-8  
# Add php7.2 repo to apt. Remove once we update to the next Ubuntu LTS.  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >
/etc/apt/sources.list.d/php.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv E5267A6C  
  
# Upgrade all currently installed packages and install web server packages.  
RUN apt-get update \  
&& apt-get -y install locales \  
&& locale-gen en_AU.UTF-8 \  
&& apt-get -y dist-upgrade \  
&& apt-get -y install apache2 php7.2-common libapache2-mod-php7.2 mysql-client
php-apcu php7.2-curl php7.2-gd php7.2-ldap php7.2-mysql php7.2-opcache
php7.2-mbstring php7.2-bcmath php7.2-xml php7.2-zip php7.2-soap libedit-dev
php-redis \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get clean && rm -rf
/var/lib/apt/lists /tmp/* /var/tmp/*  
  
# Apache config.  
COPY ./files/apache2.conf /etc/apache2/apache2.conf  
  
# PHP config.  
COPY ./files/php_custom.ini /etc/php/7.2/mods-available/php_custom.ini  
  
# Configure apache modules, php modules, logging.  
RUN a2enmod rewrite \  
&& a2dismod vhost_alias \  
&& a2disconf other-vhosts-access-log \  
&& a2dissite 000-default \  
&& phpenmod -v ALL -s ALL php_custom  
  
# Add /code /shared directories and ensure ownership by web user.  
RUN mkdir -p /code /shared && chown www-data:www-data /code /shared  
  
# Configure default bash setup.  
COPY ./files/bashrc /etc/skel/.bashrc  
COPY ./files/bashrc /root/.bashrc  
  
# Add in bootstrap script.  
COPY ./files/apache2-foreground /apache2-foreground  
RUN chmod +x /apache2-foreground  
  
# Web port.  
EXPOSE 80  
# Set working directory.  
WORKDIR /code  
  
# Start the web server.  
CMD ["/apache2-foreground"]  

