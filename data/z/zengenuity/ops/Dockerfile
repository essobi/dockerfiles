FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get install -y unzip \  
gzip \  
curl \  
git \  
lsb-release \  
wget \  
openssh-client \  
rsync \  
php-cli \  
php-curl \  
php-xml \  
php-gd \  
php-db \  
php-zip \  
&& sh -c "echo 'precedence ::ffff:0:0/96 100' >> /etc/gai.conf" \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& curl -O https://raw.githubusercontent.com/pantheon-systems/terminus-
installer/master/builds/installer.phar \  
&& php installer.phar install \  
&& php -r "unlink('installer.phar');" \  
&& curl -sS https://platform.sh/cli/installer | php \  
&& wget https://pkg.tarsnap.com/tarsnap-deb-packaging-key.asc \  
&& apt-key add tarsnap-deb-packaging-key.asc \  
&& sh -c 'echo "deb http://pkg.tarsnap.com/deb/$(lsb_release -s -c) ./" >>
/etc/apt/sources.list.d/tarsnap.list' \  
&& rm tarsnap-deb-packaging-key.asc \  
&& apt-get update \  
&& apt-get -y install tarsnap python-setuptools \  
&& easy_install tarsnapper \  
&& git clone https://gitlab.com/zengenuity/zen-cli.git \  
&& cd zen-cli \  
&& composer install \  
&& cd .. \  
&& mv zen-cli /usr/local/share \  
&& cd /usr/local/share/zen-cli \  
&& ln -s /usr/local/share/zen-cli/zen /usr/local/bin \  
&& chmod a+x /usr/local/share/zen-cli/zen \  
&& composer clear-cache \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/cache/* \  
&& rm -rf /var/lib/log/* && rm -rf /tmp/*  
  
VOLUME ["/app"]  
WORKDIR /app  

