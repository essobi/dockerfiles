FROM mediawiki:1.27  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG BLUESPICE_VERSION="2.27.2"  
  
ENV WIKI_URL="http://localhost:80"  
ENV WIKI_NAME="BlueSpice"  
ENV DB_USER="bluespice"  
ENV DB_PASS=""  
ENV DB_NAME="bluespice"  
ENV DB_PORT="3306"  
ENV DB_SERVER="mysql"  
ENV ADMIN_LOGIN="admin"  
ENV ADMIN_PASS="bluespice"  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="BlueSpice free" \  
org.label-schema.description="Simple PHP/Apache2 container for BlueSpice wiki"
\  
org.label-schema.url="https://bluespice.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kns-it/Docker-BlueSpice-Wiki" \  
org.label-schema.vendor="KNS" \  
org.label-schema.version="${BLUESPICE_VERSION}" \  
org.label-schema.schema-version="1.0" \  
maintainer="sebastian.kurfer@kns-it.de"  
  
COPY php.ini /usr/local/etc/php/php.ini  
COPY bluespice-entrypoint.sh /bluespice-entrypoint.sh  
  
RUN apt-get update && \  
apt-get install -y unzip \  
libtidy-dev \  
libpng12-dev\  
libjpeg-dev \  
libfreetype6-dev\  
libmcrypt-dev \  
libgd-dev && \  
apt-get clean all && \  
docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-freetype-dir=/usr/include/freetype2 \  
\--with-png-dir=/usr/include \  
\--with-jpeg-dir=/usr/include && \  
docker-php-ext-install tidy gd && \  
curl -L -o /tmp/bluespice.zip
https://sourceforge.net/projects/bluespice/files/BlueSpice-
free-${BLUESPICE_VERSION}.zip/download && \  
unzip /tmp/bluespice.zip -d /tmp/ && \  
cp -rf /tmp/bluespice-free/extensions/* /var/www/html/extensions/ && \  
cp -rf /tmp/bluespice-free/settings.d /var/www/html/ && \  
cp -rf /tmp/bluespice-free/skins /var/www/html/ && \  
cp -f /tmp/bluespice-free/installcheck.php /var/www/html/ && \  
cp -f /tmp/bluespice-free/LocalSettings.BlueSpice.php /var/www/html/ && \  
mv /var/www/html/extensions/BlueSpiceFoundation/data.template
/var/www/html/extensions/BlueSpiceFoundation/data && \  
mv /var/www/html/extensions/BlueSpiceFoundation/config.template
/var/www/html/extensions/BlueSpiceFoundation/config && \  
rm -rf /tmp/* && \  
chown -R www-data:www-data /var/www/html/  
  
VOLUME [ "/config" ]  
VOLUME [ "/extensions" ]  
VOLUME [ "/data" ]  
  
CMD [ "/bluespice-entrypoint.sh" ]  

