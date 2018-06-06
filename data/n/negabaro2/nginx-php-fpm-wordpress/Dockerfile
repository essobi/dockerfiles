FROM nginx:mainline-alpine  
MAINTAINER negabaro <negabaro@gmail.com>  
  
ENV php_conf /etc/php5/php.ini  
ENV fpm_conf /etc/php5/php-fpm.conf  
ENV composer_hash
aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d  
ENV min_spare_servers_cnt 10  
ENV max_spare_servers_cnt 50  
ENV start_servers_cnt 10  
ENV max_children_cnt 100  
  
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
php5-memcache \  
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
php5-redis@testing \  
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
libffi-dev  
  
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
  
  
ADD files /attachment  
  
RUN rm -Rf /etc/nginx/nginx.conf ;\  
rm -Rf /var/www/* ;\  
rm -Rf /etc/nginx/conf.d/* ;\  
mkdir -p /var/www/html/wordpress ;\  
cp -rp /attachment/supervisord.conf /etc/supervisord.conf ;\  
cp -rp /attachment/nginx.conf /etc/nginx/nginx.conf ;\  
cp -rp /attachment/default.conf /etc/nginx/conf.d/default.conf ;\  
cp -rp /attachment/php-fpm.conf ${fpm_conf} ;\  
cp -rp /attachment/run_sh.sh /run_sh.sh  
  
RUN sed -i \  
-e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" \  
-e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" \  
-e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" \  
-e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g" \  
${php_conf}  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN cd /tmp && wget https://wordpress.org/latest.zip /var/www/html ;\  
unzip latest.zip -d /var/www/html  
  
VOLUME /var/www/html  
EXPOSE 443 80  
#CMD sh /run_sh.sh && /usr/bin/supervisord -c /etc/supervisord.conf  
CMD /usr/bin/python /usr/bin/supervisord -n -c /etc/supervisord.conf  

