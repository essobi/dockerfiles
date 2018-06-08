FROM gaozhi/php7-fpm-phalcon3  
  
RUN \  
apt-get update && \  
apt-get install -y libgearman-dev tesseract-ocr libglib2.0-dev
libcurl4-openssl-dev cron imagemagick libc-client-dev libkrb5-dev  
  
RUN \  
cd /tmp && \  
git clone https://github.com/wcgallego/pecl-gearman.git && \  
cd pecl-gearman && \  
phpize && \  
./configure && \  
make && make install && \  
rm -rf /tmp/pecl-gearman  
  
RUN \  
pecl install mongodb && \  
docker-php-ext-enable mongodb && \  
pecl install mailparse && \  
docker-php-ext-enable mailparse && \  
pecl clear-cache  
  
RUN \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-install imap  
  
RUN \  
cd /tmp && \  
curl -L 'https://megatools.megous.com/builds/megatools-1.9.98.tar.gz' >
megatools-1.9.98.tar.gz && \  
tar -zxf megatools-1.9.98.tar.gz && \  
cd megatools-1.9.98 && \  
./configure --disable-docs && \  
make && make install && \  
chmod ug+s /usr/local/bin/mega* && \  
rm -rf /tmp/megatools-1.9.98 && \  
rm /tmp/megatools-1.9.98.tar.gz && \  
apt-get clean && \  
rm -rf /var/lib/apt/list/*  
  
RUN \  
docker-php-ext-enable gearman.so && \  
mkdir -p ${HOME}/php-default-conf && \  
cp -R /usr/local/etc/* ${HOME}/php-default-conf  
  
VOLUME ["/var/spool/cron/crontabs", "/var/www", "/usr/local/etc"]  
  
ADD ["./docker-entrypoint.sh", "/root/"]  
  
ENTRYPOINT ["sh", "-c", "${HOME}/docker-entrypoint.sh"]

