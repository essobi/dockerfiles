FROM php:7-cli  
LABEL maintainer=Kingsquare<docker@kingsquare.nl>  
  
ENV TZ "Europe/Amsterdam"  
ENV NODE_VERSION 8.10.0  
ENV YARN_VERSION 1.5.1  
ENV COMPOSER_VERSION 1.6.3  
ENV NPM_CONFIG_LOGLEVEL info  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex; \  
if ! command -v gpg > /dev/null; then \  
fetchDeps="\  
dirmngr \  
gnupg \  
"; \  
fi; \  
apt-get update; \  
apt-get install -qy --no-install-recommends $fetchDeps; \  
for key in \  
# NODE KEYS  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
# YARN KEY  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
# PHPUNIT KEY  
0x4AA394086372C20A \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver pgp.uni-mainz.de --recv-keys "$key"; \  
done ; \  
groupadd --gid 1000 node; \  
useradd --uid 1000 \--gid node --shell /bin/bash --create-home node; \  
curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz"; \  
curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"; \  
gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc; \  
grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c
-; \  
tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1; \  
rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt; \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs; \  
curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz"; \  
curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc";
\  
gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz; \  
mkdir -p /opt/yarn; \  
tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1; \  
ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn; \  
ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg; \  
rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz; \  
# INSTALL COMPOSER  
curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer;
\  
php -r " \  
\$signature =
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}"; \  
php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION}; \  
rm /tmp/installer.php; \  
composer --ansi --version --no-interaction; \  
# CONFIGURE PHP  
apt-get update; \  
apt-get install -qy --no-install-recommends \  
libbz2-dev \  
zlib1g-dev \  
git \  
openssh-client \  
rsync; \  
docker-php-ext-install zip bz2 mbstring; \  
docker-php-ext-enable opcache; \  
echo "opcache.enable_cli = On" > /usr/local/etc/php/conf.d/opcache-cli.ini; \  
echo "date.timezone = $TZ" > /usr/local/etc/php/conf.d/timezone.ini; \  
echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini; \  
# INSTALL PHPUNIT  
curl -fSLO --compressed "https://phar.phpunit.de/phpunit.phar"; \  
curl -fSLO --compressed "https://phar.phpunit.de/phpunit.phar.asc"; \  
gpg --batch --verify phpunit.phar.asc phpunit.phar; \  
rm phpunit.phar.asc; \  
mkdir -p /opt/phpunit; \  
mv phpunit.phar /opt/phpunit.phar; \  
chmod +x /opt/phpunit.phar; \  
ln -s /opt/phpunit.phar /usr/local/bin/phpunit.phar; \  
ln -s /opt/phpunit.phar /usr/local/bin/phpunit; \  
# CLEANUP  
apt-get -qq clean; \  
rm -rf /tmp/* /var/tmp/* /var/cache/apt/*; \  
apt-get purge -yq --auto-remove -o APT::AutoRemove::RecommendsImportant=false  

