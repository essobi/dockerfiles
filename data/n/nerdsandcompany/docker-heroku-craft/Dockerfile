# Inherit from Heroku's stack  
FROM heroku/heroku:18  
MAINTAINER Bob Olde Hampsink <b.oldehampsink@nerds.company>  
  
# Internally, we arbitrarily use port 3000  
ENV PORT 3000  
# Which versions?  
ENV PHP_VERSION 7.2.6  
ENV REDIS_EXT_VERSION 4.0.2  
ENV IMAGICK_EXT_VERSION 3.4.3  
ENV HTTPD_VERSION 2.4.33  
ENV NGINX_VERSION 1.8.1  
ENV NODE_ENGINE 8.11.2  
ENV COMPOSER_VERSION 1.6.5  
ENV YARN_VERSION 1.6.0  
# Create some needed directories  
RUN mkdir -p /app/.heroku/php /app/.heroku/node /app/.profile.d  
WORKDIR /app/user  
  
# Locate our binaries  
ENV PATH
/app/.heroku/php/bin:/app/.heroku/php/sbin:/app/.heroku/node/bin/:/app/user/node_modules/.bin:/app/user/vendor/bin:$PATH  
  
# Install Apache  
RUN curl --silent --location https://lang-php.s3.amazonaws.com/dist-
heroku-18-stable/apache-$HTTPD_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Config  
RUN curl --silent --location https://raw.githubusercontent.com/heroku/heroku-
buildpack-
php/5a770b914549cf2a897cbbaf379eb5adf410d464/conf/apache2/httpd.conf.default >
/app/.heroku/php/etc/apache2/httpd.conf  
# FPM socket permissions workaround when run as root  
RUN echo "\n\  
Group root\n\  
" >> /app/.heroku/php/etc/apache2/httpd.conf  
  
# Install Nginx  
RUN curl --silent --location https://lang-php.s3.amazonaws.com/dist-
heroku-18-stable/nginx-$NGINX_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Config  
RUN curl --silent --location https://raw.githubusercontent.com/heroku/heroku-
buildpack-
php/5a770b914549cf2a897cbbaf379eb5adf410d464/conf/nginx/nginx.conf.default >
/app/.heroku/php/etc/nginx/nginx.conf  
# FPM socket permissions workaround when run as root  
RUN echo "\n\  
user nobody root;\n\  
" >> /app/.heroku/php/etc/nginx/nginx.conf  
  
# Install PHP  
RUN curl --silent --location https://lang-php.s3.amazonaws.com/dist-
heroku-18-stable/php-$PHP_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Config  
RUN mkdir -p /app/.heroku/php/etc/php/conf.d  
RUN curl --silent --location https://raw.githubusercontent.com/heroku/heroku-
buildpack-php/5a770b914549cf2a897cbbaf379eb5adf410d464/conf/php/php.ini >
/app/.heroku/php/etc/php/php.ini  
RUN curl --silent --location https://lang-php.s3.amazonaws.com/dist-
heroku-18-stable/extensions/no-debug-non-
zts-20170718/redis-$REDIS_EXT_VERSION.tar.gz | tar xz -C /app/.heroku/php  
RUN curl --silent --location https://lang-php.s3.amazonaws.com/dist-
heroku-18-stable/extensions/no-debug-non-
zts-20170718/imagick-$IMAGICK_EXT_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Enable all optional exts  
RUN echo "\n\  
user_ini.cache_ttl = 30 \n\  
opcache.enable = 0 \n\  
extension=bcmath.so \n\  
extension=calendar.so \n\  
extension=exif.so \n\  
extension=ftp.so \n\  
extension=gd.so\n\  
extension=gettext.so \n\  
extension=intl.so \n\  
extension=mbstring.so \n\  
extension=pcntl.so \n\  
extension=redis.so \n\  
extension=imagick.so \n\  
extension=shmop.so \n\  
extension=soap.so \n\  
extension=sqlite3.so \n\  
extension=pdo_sqlite.so \n\  
extension=xmlrpc.so \n\  
extension=xsl.so\n\  
" >> /app/.heroku/php/etc/php/php.ini  
  
# Install Composer  
RUN curl --silent --location https://lang-php.s3.amazonaws.com/dist-
heroku-18-stable/composer-$COMPOSER_VERSION.tar.gz | tar xz -C
/app/.heroku/php  
  
# Install Node  
RUN curl -s
https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-
linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/.heroku/node  
  
# Install Yarn  
RUN curl -s https://s3.amazonaws.com/heroku-nodejs-
bins/yarn/release/yarn-v$YARN_VERSION.tar.gz | tar --strip-components=1 -xz -C
/app/.heroku/node  
  
# Install Chrome WebDriver  
RUN CHROMEDRIVER_VERSION=`curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE` \  
&& mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION \  
&& curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
\  
&& unzip -qq /tmp/chromedriver_linux64.zip -d
/opt/chromedriver-$CHROMEDRIVER_VERSION \  
&& rm /tmp/chromedriver_linux64.zip \  
&& chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver \  
&& ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
/usr/local/bin/chromedriver  
  
# Install Google Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/*  
  
# copy dep files first so Docker caches the install step if they don't change  
ONBUILD COPY composer.lock /app/user/  
ONBUILD COPY composer.json /app/user/  
# run install but without scripts as we don't have the app source yet  
ONBUILD RUN composer install --prefer-dist --no-scripts --no-suggest  
# require the buildpack for execution  
ONBUILD RUN composer show heroku/heroku-buildpack-php || { echo 'Your
composer.json must have "heroku/heroku-buildpack-php" as a "require-dev"
dependency.'; exit 1; }  
  
# run npm or yarn install  
ONBUILD COPY package*.json yarn.* /app/user/  
ONBUILD RUN [ -f yarn.lock ] && yarn install --no-progress || npm install  
  
# rest of app  
ONBUILD COPY . /app/user/  
# run hooks  
ONBUILD RUN cat composer.json | python -c 'import sys,json; sys.exit("post-
install-cmd" not in json.load(sys.stdin).get("scripts", {}));' && composer
run-script post-install-cmd || true  
ONBUILD RUN cat composer.json | python -c 'import sys,json; sys.exit("post-
autoload-dump" not in json.load(sys.stdin).get("scripts", {}));' && composer
run-script post-autoload-dump || true  

