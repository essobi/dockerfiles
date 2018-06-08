FROM alpine  
MAINTAINER Rafael <rafael@faztodadiferenca.com.br>  
  
  
RUN echo @testing http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
echo /etc/apk/respositories && \  
apk update && \  
apk add --no-cache bash \  
gettext \  
vim \  
mariadb-client \  
openssh-client \  
wget \  
supervisor \  
curl \  
git \  
php5-fpm \  
php5-pdo \  
php5-pdo_mysql \  
php5-mysql \  
php5-mysqli \  
php5-mcrypt \  
php5-ctype \  
php5-zlib \  
php5-gd \  
php5-exif \  
php5-intl \  
php5-sqlite3 \  
php5-pgsql \  
php5-xml \  
php5-xsl \  
php5-curl \  
php5-openssl \  
php5-iconv \  
php5-json \  
php5-phar \  
php5-soap \  
php5-dom \  
php5-zip \  
php5-cli \  
python \  
python-dev \  
py-pip \  
augeas-dev \  
openssl-dev \  
ca-certificates \  
dialog \  
gcc \  
musl-dev \  
linux-headers \  
sed \  
bash \  
libffi-dev  
  
RUN ln -s /usr/bin/php5 /usr/bin/php  
  
RUN mkdir -p /etc/nginx && \  
mkdir -p /var/www/app && \  
mkdir -p /run/nginx && \  
mkdir -p /var/log/supervisor &&\  
# php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" &&
\  
#php -r "if (hash_file('SHA384', 'composer-setup.php') === '${composer_hash}')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
#php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
#php -r "unlink('composer-setup.php');" && \  
pip install -U pip && \  
pip install -U certbot && \  
mkdir -p /etc/letsencrypt/webrootauth && \  
apk del gcc musl-dev linux-headers libffi-dev augeas-dev python-dev  
  
RUN mkdir -p /var/www/html/wordpress  
  
ADD files /attachment  
  
RUN cp -rp /attachment/supervisord.conf /etc/supervisord.conf; \  
cp -rp /attachment/deploy.sh /usr/bin/deploy.sh; \  
cp -rp /attachment/update.sh /usr/bin/update.sh; \  
cp -rp /attachment/webhook /usr/bin/webhook; \  
chmod 777 /usr/bin/*;  
  
EXPOSE 80  
  
WORKDIR /var/www/html/wordpress  
VOLUME /var/www/html/wordpress  
CMD /usr/bin/python /usr/bin/supervisord -n -c /etc/supervisord.conf

