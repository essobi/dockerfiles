FROM php:7.2.5-apache  
ENV RAINLOOP_VERSION=1.12.0  
RUN GPG_KEYS=3B797ECE694F3B7B70F311A4ED7C49D987DA4591 \  
&& apt-get update && apt-get install -y --no-install-recommends unzip gnupg
dirmngr \  
&& rm -r /var/lib/apt/lists/* \  
&& cd /var/www/html/ \  
&& curl -fSL -o rainloop.zip https://github.com/RainLoop/rainloop-
webmail/releases/download/v${RAINLOOP_VERSION}/rainloop-
community-${RAINLOOP_VERSION}.zip \  
&& curl -fSL -o rainloop.zip.asc https://github.com/RainLoop/rainloop-
webmail/releases/download/v${RAINLOOP_VERSION}/rainloop-
community-${RAINLOOP_VERSION}.zip.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify rainloop.zip.asc rainloop.zip \  
&& rm -r "$GNUPGHOME" rainloop.zip.asc; \  
unzip rainloop.zip \  
&& rm rainloop.zip \  
&& chown -R www-data:www-data . \  
&& find . -type d -exec chmod 755 {} \; \  
&& find . -type f -exec chmod 644 {} \; \  
&& /bin/echo -e "Order deny,allow\nAllow from all" > /var/www/html/.htaccess \  
&& /bin/echo -e "Order deny,allow\nDeny from all" >
/var/www/html/data/.htaccess  
COPY upload.ini /usr/local/etc/php/conf.d/  

