# we cannot use mainline nginx image, is uses alpine 3.5 and it causes an
openssl issue (wget https://www.baidu.com will receive SIGKILL), which we
haven't found the root cause yet.  
FROM nginx:1.11.8-alpine  
  
MAINTAINER ngineered <support@ngineered.co.uk>  
  
ENV php_conf /etc/php5/php.ini  
ENV fpm_conf /etc/php5/php-fpm.conf  
ENV php_vars /etc/php5/conf.d/docker-vars.ini  
ENV composer_hash
544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061  
  
RUN echo @testing http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
echo /etc/apk/respositories && \  
apk update && \  
apk add --no-cache bash \  
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
pip install -U pip && \  
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
  
# tweak php-fpm config  
RUN sed -i \  
-e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" \  
-e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" \  
-e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" \  
-e "s/variables_order = \"GPCS\"/variables_order = \"EGPCS\"/g" \  
${php_conf} && \  
sed -i \  
-e "s/;daemonize\s*=\s*yes/daemonize = no/g" \  
-e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" \  
-e "s/pm.max_children = 5/pm.max_children = 100/g" \  
-e "s/pm.start_servers = 2/pm.start_servers = 10/g" \  
-e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 10/g" \  
-e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 30/g" \  
-e "s/pm.max_requests = 500/pm.max_requests = 200/g" \  
-e "s/user = nobody/user = nginx/g" \  
-e "s/group = nobody/group = nginx/g" \  
-e "s/;listen.mode = 0660/listen.mode = 0666/g" \  
-e "s/;listen.owner = nobody/listen.owner = nginx/g" \  
-e "s/;listen.group = nobody/listen.group = nginx/g" \  
-e "s/listen = 127.0.0.1:9000/listen = \/var\/run\/php-fpm.sock/g" \  
-e "s/^;clear_env = no$/clear_env = no/" \  
${fpm_conf} && \  
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
  
# modify timezone  
RUN apk add tzdata \  
&& ls /usr/share/zoneinfo \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& echo "date.timezone = Asia/Shanghai" >> ${php_vars} \  
&& date  
  
# ssl certificate file  
ADD conf/cacert.pem /cacert.pem  
ADD conf/cacert.pem /etc/ssl/cert.pem  
RUN echo "curl.cainfo=/cacert.pem" >> ${php_vars}  
# 配置Node版本  
ARG NODE_VERSION=6.3.0  
WORKDIR /  
# 安装Nodejs  
ENV GPG_KEYS \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8  
ENV BUILD_PKGS="git curl make gcc g++ python linux-headers libgcc libstdc++
binutils-gold xz gnupg"  
RUN \  
apk --no-cache add ${BUILD_PKGS} \  
# && for key in $GPG_KEYS; do \  
# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
# done \  
&& curl -SLO
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.xz\  
# && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
# && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
# && grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \  
&& tar -xJf "node-v$NODE_VERSION.tar.xz" \  
&& cd /node-v${NODE_VERSION} \  
&& ./configure --prefix=/usr --without-snapshot --fully-static \  
&& make -j $(getconf _NPROCESSORS_ONLN) \  
&& make install  
  
#RUN npm install -g cnpm --registry=https://registry.npm.taobao.org  
# Don't defined the volume because we want to do composer install during our
project image build.  
# VOLUME /var/www/html  
EXPOSE 443 80  
#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
CMD ["/start.sh"]  

