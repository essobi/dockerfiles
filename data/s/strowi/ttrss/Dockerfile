FROM alpine:latest  
  
ENV TTRSS_VERSION=17.4  
  
RUN apk \--update \--no-cache add \  
git \  
curl \  
&& mkdir -p /app \  
&& curl -sL https://git.tt-rss.org/git/tt-rss/archive/${TTRSS_VERSION}.tar.gz
|tar -xvz \--strip-components=1 -C /app  
# && git clone --depth=1 https://github.com/sepich/tt-rss-mobilize.git
/app/plugins/mobilize \  
# && git clone --depth=1 https://github.com/hrk/tt-rss-newsplus-plugin.git
/app/plugins/api_newsplus \  
# && git clone --depth=1 https://github.com/m42e/ttrss_plugin-feediron.git
/app/plugins/feediron \  
# && git clone --depth=1 https://github.com/levito/tt-rss-feedly-theme.git
/app/themes/feedly-git \  
# && find . -name '.git*' |xargs rm -fr  
  
  
FROM nginx:1.13.5-alpine  
# Expose default database credentials via ENV in order to ease overwriting.  
  
RUN apk \--update \--no-cache add \  
supervisor \  
ca-certificates \  
curl \  
php7 \  
php7-fpm \  
php7-curl \  
php7-dom \  
php7-gd \  
php7-json \  
php7-mcrypt \  
php7-pcntl \  
php7-pdo \  
php7-pdo_pgsql \  
php7-pgsql \  
php7-pdo_mysql \  
php7-mysqli \  
php7-posix \  
php7-mbstring \  
php7-iconv \  
php7-session \  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add \--no-cache \--virtual .gettext gettext \  
&& ln -s /usr/bin/php7 /usr/bin/php \  
&& mv /usr/bin/envsubst /tmp/ \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--update \--no-cache \--virtual .nginx-rundeps $runDeps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
&& apk del \--progress \--purge \  
&& rm -rf /var/cache/apk/*  
  
COPY \--from=0 /app /var/www/ttrss  
RUN chown -R nginx:nginx /var/www/ttrss  
# Copy root file system.  
ADD src/ /  
  
# Expose Nginx ports.  
EXPOSE 8080  
  
CMD ["/docker-entrypoint.sh"]  

