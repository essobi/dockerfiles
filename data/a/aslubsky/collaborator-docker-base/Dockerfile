FROM debian:9.4-slim  
  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get install -y \  
wget \  
curl \  
dialog \  
bsdutils \  
make \  
g++ \  
gnupg \  
cron \  
unzip \  
git \  
supervisor \  
catdoc \  
certbot \  
poppler-utils \  
libav-tools \  
gpac  
  
RUN cd /tmp && wget https://github.com/htacg/tidy-
html5/releases/download/5.4.0/tidy-5.4.0-64bit.deb && dpkg -i
tidy-5.4.0-64bit.deb  
  
RUN echo "deb http://nginx.org/packages/debian/ stretch nginx" >
/etc/apt/sources.list.d/nginx.list  
RUN echo "deb-src http://nginx.org/packages/debian/ stretch nginx" >>
/etc/apt/sources.list.d/nginx.list  
RUN cd /tmp && wget http://nginx.org/keys/nginx_signing.key && apt-key add
nginx_signing.key  
RUN apt-get update && apt-get install -y nginx logrotate  
  
RUN apt-get install -y php7.0 php7.0-mysql php7.0-xml php7.0-curl php7.0-gd
php7.0-mcrypt php7.0-intl php7.0-zip php7.0-mbstring php7.0-fpm php7.0-sqlite
php7.0-ldap  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin  
RUN /usr/bin/composer.phar self-update  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN npm install -g bower forever node-gyp gulp  
  
#  
# Remove the packages that are no longer required after the package has been
installed  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -q -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoclean -y -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get clean -y  
  
# Remove all non-required information from the system to have the smallest  
# image size as possible  
# ftp://cgm_gebraucht%40used-forklifts.org:bZAo6dH1cyxhJpgJwO@ftp.strato.com/  
RUN rm -rf /usr/share/doc/* /usr/share/man/?? /usr/share/man/??_*
/usr/share/locale/* /var/cache/debconf/*-old /var/lib/apt/lists/* /tmp/*  
  

