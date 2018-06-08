FROM alpine:3.5  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="syspass-recovery" \  
org.label-schema.description="sysPass recovery image" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/syspass-recovery" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd=""  
  
ENV TZ "Europe/Berlin"  
# Install NGINX and PHP 7  
RUN apk update && apk --no-cache add \  
bash \  
tzdata \  
curl \  
ca-certificates \  
s6 \  
ssmtp \  
mysql-client \  
nginx \  
nginx-mod-http-headers-more \  
&& ln -sf "/usr/share/zoneinfo/$TZ" /etc/localtime \  
&& echo "$TZ" > /etc/timezone && date \  
&& apk --no-cache add \  
php7 php7-phar php7-curl php7-fpm php7-json php7-zlib php7-gd \  
php7-xml php7-dom php7-ctype php7-opcache php7-zip php7-iconv \  
php7-pdo php7-pdo_mysql php7-mysqli php7-mbstring php7-session \  
php7-mcrypt php7-openssl php7-sockets php7-posix php7-mbstring php7-gettext
openssl \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /usr/bin/php7 /usr/bin/php \  
&& rm -f /etc/php7/php-fpm.d/www.conf \  
&& touch /etc/php7/php-fpm.d/env.conf \  
&& rm -rf /var/www  
  
# Copy Config  
COPY conf/services.d /etc/services.d  
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY conf/php/php-fpm.conf /etc/php7/  
COPY conf/php/conf.d/php.ini /etc/php7/conf.d/zphp.ini  
  
WORKDIR /var/www  
  
# Download and install the latest sysPass stable release from GitHub  
RUN wget https://github.com/nuxsmin/sysPass/archive/master.zip \  
&& unzip master.zip \  
&& mv sysPass-master sysPass \  
&& chmod 750 sysPass/config sysPass/backup \  
&& chown nginx:nginx -R sysPass/ \  
&& rm master.zip \  
&& sed -i "s/\/var\/www/\/var\/www\/sysPass/" /etc/nginx/nginx.conf  
  
# Permissions  
RUN mkdir /var/session \  
&& chown -R nginx:nginx /var/www \  
&& chown -R nginx:nginx /var/session \  
&& chmod 750 /var/www -R  
  
EXPOSE 80  
ENTRYPOINT ["/bin/s6-svscan", "/etc/services.d"]  

