FROM docker.io/fedora:28 as loader  
RUN cd /opt \  
&& mkdir matomo \  
&& curl https://builds.matomo.org/piwik-3.4.0.tar.gz | tar zxv --strip 1 -C
matomo  
FROM docker.io/matrixdotorg/base-php  
ENV APPDIR=/matomo \  
DISPLAY_ERRORS=On \  
MEMORY_LIMIT=256M  
RUN apk add --no-cache \  
bash \  
php7-pdo_mysql \  
php7-session \  
php7-json \  
php7-curl \  
php7-gd \  
php7-xml \  
php7-mbstring \  
php7-ctype \  
php7-iconv \  
php7-dom \  
php7-simplexml \  
php7-redis \  
php7-opcache  
VOLUME /config  
COPY root /  
COPY \--from=loader /opt/matomo /matomo  

