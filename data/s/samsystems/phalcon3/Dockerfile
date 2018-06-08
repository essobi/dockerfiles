FROM debian:jessie  
  
VOLUME ["/var/www"]  
VOLUME ["/tmp"]  
  
# install packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install \  
apache2 \  
libapache2-mod-php5 \  
php5 \  
php5-common \  
php5-cli \  
php5-curl \  
php5-gd \  
imagemagick \  
php5-imagick \  
php5-mysql \  
php5-xdebug \  
wkhtmltopdf \  
xvfb \  
pdftk \  
git \  
php5-dev \  
libpcre3-dev \  
gcc \  
make \  
curl  
  
COPY script.deb.sh /tmp/  
RUN bash /tmp/script.deb.sh  
RUN apt-get update && apt-get install php5-phalcon  
  
RUN /usr/sbin/a2enmod rewrite  
  
ADD 000-phalcon.conf /etc/apache2/sites-available/  
ADD 001-phalcon-ssl.conf /etc/apache2/sites-available/  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-phalcon 001-phalcon-ssl  
  
WORKDIR /tmp  
# Run build process on one line to avoid generating bloat via intermediate
images  
RUN /usr/bin/apt-get -y purge git php5-dev libpcre3-dev gcc make && apt-get -y
autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN /bin/echo 'extension=phalcon.so' >/etc/php5/mods-available/phalcon.ini  
RUN /usr/sbin/php5enmod phalcon  
WORKDIR /var/www/phalcon/public  
RUN /bin/echo '<html><body><h1>It works!</h1></body></html>' >
/var/www/phalcon/public/index.html  
  
# xdebug configuration (port must match phpstorm xdebug configuration)  
RUN echo "xdebug.remote_enable=on \n\  
xdebug.remote_host=172.19.0.1 \n\  
xdebug.remote_port=10000 \n\  
xdebug.remote_connect_back=Off \n\  
xdebug.remote_autostart=on" >> /etc/php5/mods-available/xdebug.ini  
  
# alias for cli debugging (serverName must match phpstorm configured server)  
RUN echo "alias phpdb='export XDEBUG_CONFIG=\"idekey=PHPSTORM\"; export
PHP_IDE_CONFIG=\"serverName=docker\"; php '" >> ~/.bashrc  
  
# needed to stop re-running the container on osx  
RUN rm -f /var/run/apache2/apache2.pid  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR /var/www  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

