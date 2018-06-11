FROM ubuntu:xenial  
  
ADD https://getcomposer.org/composer.phar /usr/local/bin/composer  
ADD files/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz /usr/  
  
RUN \  
export TERM=xterm ;\  
groupadd -g 999 docker ;\  
cp -R /usr/wkhtmltox/* /usr/ ;\  
rm -rf /usr/wkhtmltox ;\  
ln -s /usr/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf ;\  
apt-get update ;\  
apt-get -y install language-pack-en-base software-properties-common ;\  
export LC_ALL=en_US.UTF-8 ;\  
export LANG=en_US.UTF-8 ;\  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php ;\  
apt-get update ;\  
apt-get -y install libxrender1 libxext6 wget supervisor nginx php7.1-mysqlnd
php7.1-xml php7.1-fpm php7.1-intl php7.1-mbstring php7.1-zip php7.1-bz2 php-
mongodb php7.1-xsl php7.1-mcrypt php7.1-curl php7.1-json php7.1-gd
php7.1-opcache php7.1-soap varnish nodejs npm curl mariadb-client git
libsodium-dev php-pecl-http php-pear php7.1-dev letsencrypt php7.1-dev vim
php-xml libssl-dev=1.0.2g-1ubuntu4.* ;\  
apt-get clean ;\  
pecl install libsodium ;\  
npm install gulp -g ;\  
ln -s /usr/bin/nodejs /usr/bin/node ;\  
mkdir -p /var/log/supervisor /run/php /data/log/supervisor /data/nginx/sites
/etc/letsencrypt /var/www/letsencrypt/.well-known/acme-challenge ;\  
chmod +x /usr/local/bin/composer ;\  
usermod -aG docker www-data ;\  
chmod -R 777 /var/lib/php/sessions ;\  
cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime ;\  
service cron start ;\  
rm /etc/alternatives/php ;\  
ln -s /usr/bin/php7.1 /etc/alternatives/php  
# END RUN  
COPY files/libsodium.ini /etc/php/7.1/mods-available/libsodium.ini  
COPY files/libsodium.ini /etc/php/7.2/mods-available/libsodium.ini  
COPY files/php.ini /etc/php/7.1/fpm/php.ini  
COPY files/php.ini /etc/php/7.2/fpm/php.ini  
COPY files/php-cli.ini /etc/php/7.1/cli/php.ini  
COPY files/php-cli.ini /etc/php/7.2/cli/php.ini  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
COPY files/www.conf /etc/php/7.2/fpm/pool.d/www.conf  
COPY files/default.vcl /etc/varnish/default.vcl  
COPY files/supervisord.conf /etc/supervisor/supervisord.conf  
COPY files/ssl.conf /etc/nginx/snippets/ssl.conf  
COPY files/letsencrypt.conf /etc/nginx/snippets/letsencrypt.conf  
  
RUN phpenmod libsodium  
RUN supervisorctl restart php7-fpm  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord"]  

