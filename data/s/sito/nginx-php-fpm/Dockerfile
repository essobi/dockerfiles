FROM alpine:3.4  
  
MAINTAINER SitoCH <sito@grignola.ch>  
  
ENV php_conf /etc/php5/php.ini  
ENV fpm_conf /etc/php5/php-fpm.conf  
ENV composer_hash
544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061  
  
RUN apk add --no-cache bash \  
openssh-client \  
wget \  
nginx \  
supervisor \  
curl \  
git \  
php5-apcu \  
php5-fpm \  
php5-pdo \  
php5-pdo_mysql \  
php5-mysql \  
php5-mysqli \  
php5-mcrypt \  
php5-ctype \  
php5-zlib \  
php5-gd \  
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
libffi-dev &&\  
mkdir -p /etc/nginx && \  
mkdir -p /var/www/app && \  
mkdir -p /run/nginx && \  
mkdir -p /var/log/supervisor &&\  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') === '${composer_hash}')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
pip install -U certbot && \  
mkdir -p /etc/letsencrypt/webrootauth && \  
apk del gcc musl-dev linux-headers libffi-dev augeas-dev python-dev  
  
  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
# Copy our nginx config  
RUN rm -Rf /etc/nginx/nginx.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
  
# nginx site conf  
RUN mkdir -p /etc/nginx/sites-available/ && \  
mkdir -p /etc/nginx/sites-enabled/ && \  
mkdir -p /etc/nginx/ssl/ && \  
rm -Rf /var/www/* && \  
mkdir /var/www/html/  
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf  
ADD conf/nginx-site-ssl.conf /etc/nginx/sites-available/default-ssl.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
  
# add www-data group / user  
RUN deluser xfs && \  
delgroup www-data && \  
addgroup www-data -g 33 && \  
adduser -u 33 -g 33 -H -S www-data  
  
# tweak php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" ${php_conf} && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
${php_conf} && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" ${php_conf} && \  
sed -i -e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g"
${php_conf} && \  
sed -i -e "s/short_open_tag = Off/short_open_tag = On/g" ${fpm_conf} && \  
sed -i -e "s/short_open_tag = Off/short_open_tag = On/g" ${php_conf} && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" ${fpm_conf} && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
${fpm_conf} && \  
sed -i -e "s/pm.max_children = 4/pm.max_children = 4/g" ${fpm_conf} && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" ${fpm_conf} && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" ${fpm_conf}
&& \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" ${fpm_conf}
&& \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" ${fpm_conf} && \  
sed -i -e "s/user = nobody/user = www-data/g" ${fpm_conf} && \  
sed -i -e "s/group = nobody/group = www-data/g" ${fpm_conf} && \  
sed -i -e "s/;listen.mode = 0660/listen.mode = 0666/g" ${fpm_conf} && \  
sed -i -e "s/;listen.owner = nobody/listen.owner = www-data/g" ${fpm_conf} &&
\  
sed -i -e "s/;listen.group = nobody/listen.group = www-data/g" ${fpm_conf} &&
\  
sed -i -e "s/listen = 127.0.0.1:9000/listen = \/var\/run\/php-fpm.sock/g"
${fpm_conf} &&\  
sed -i -e "s/^;clear_env = no$/clear_env = no/" ${fpm_conf} &&\  
ln -s /etc/php5/php.ini /etc/php5/conf.d/php.ini && \  
find /etc/php5/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g'
{} \;  
# Add Scripts  
ADD scripts/start.sh /start.sh  
ADD scripts/pull /usr/bin/pull  
ADD scripts/push /usr/bin/push  
ADD scripts/letsencrypt-setup /usr/bin/letsencrypt-setup  
ADD scripts/letsencrypt-renew /usr/bin/letsencrypt-renew  
RUN chmod 755 /usr/bin/pull && chmod 755 /usr/bin/push && chmod 755
/usr/bin/letsencrypt-setup && chmod 755 /usr/bin/letsencrypt-renew && chmod
755 /start.sh  
  
# copy in code  
ADD src/ /var/www/html/  
ADD errors/ /var/www/errors/  
  
EXPOSE 443 80  
#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
CMD ["/start.sh"]  

