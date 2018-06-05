FROM debian:stable-slim  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
CAKEBOX_VERSION=latest \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_KEEP_ENV=1 \  
S6_READ_ONLY_ROOT=1  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& export BUILD_DEPS="curl git gnupg php-cli php-zip" \  
&& apt-get install --no-install-recommends --yes \  
${BUILD_DEPS} \  
ca-certificates \  
gettext \  
nginx \  
php-fpm \  
\  
# Install nodejs  
\  
&& curl \--location "https://deb.nodesource.com/setup_4.x" | bash - \  
&& apt-get install --no-install-recommends --yes \  
nodejs \  
\  
# Install bower  
\  
&& npm install -g \  
bower \  
\  
# Install composer  
\  
&& curl \--location "https://getcomposer.org/installer" | php -- --install-dir
/usr/bin \  
&& mv /usr/bin/composer.phar /usr/bin/composer \  
\  
# Install cakebox/cakebox  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/cakebox/cakebox/${CAKEBOX_VERSION}" | xargs) \  
&& git clone https://github.com/cakebox/cakebox /opt/cakebox \  
&& git -C /opt/cakebox checkout "v${CAKEBOX_VERSION}" \  
&& composer install --no-dev --optimize-autoloader --working-dir /opt/cakebox
\  
&& sh -c "cd /opt/cakebox && bower --allow-root install" \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl \--location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/s6-overlay/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl \--location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/syslog-stdout/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
\  
# Clean  
\  
&& apt-get remove --purge --yes \  
${BUILD_DEPS} \  
&& apt-get autoremove --purge --yes \  
&& rm \--force --recursive \  
/etc/nginx/sites-available/default \  
/opt/cakebox/.git \  
/opt/cakebox/config/default.php.dist \  
/root/.cache \  
/root/.config \  
/root/.composer \  
/root/.local \  
/root/.npm \  
/tmp/* \  
/usr/bin/composer \  
/usr/lib/node_modules \  
/var/lib/apt/lists/*  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "/init" ]  

