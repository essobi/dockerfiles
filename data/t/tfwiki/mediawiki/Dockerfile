FROM mediawiki:1.27.4  
# Luxuries  
RUN apt-get update && apt-get install -y \  
vim \  
less \  
zip \  
unzip \  
libmemcached-dev \  
libz-dev \  
\--no-install-recommends && \  
rm -r /var/lib/apt/lists/*  
  
# We want Apache's rewrite module  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
# MediaWiki needs these extra extensions  
RUN docker-php-ext-install sockets  
RUN pear install MAIL Net_SMTP  
RUN pecl install memcached && \  
docker-php-ext-enable memcached  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/bin/ --filename=composer  
  
# We want the wiki in a w/ subfolder  
RUN mv /var/www/html /var/www/i-will-be-w && \  
mkdir -p /var/www/html && \  
mv /var/www/i-will-be-w /var/www/html/w  
  
# Install composer dependencies  
COPY composer.json /var/www/html/w/composer.json  
COPY composer.lock /var/www/html/w/composer.lock  
RUN composer install --working-dir=/var/www/html/w/ --no-ansi --no-dev --no-
interaction --no-progress --no-scripts --optimize-autoloader  
  
# Assets  
COPY src/fonts /var/www/html/fonts  
COPY src/favicon.ico /var/www/html/  
  
# Shell utils  
COPY src/shell /var/www/html/shell  
  
# Scripts  
COPY src/scripts /var/www/html/scripts  
  
# Valve skin  
# TODO: Check how much of this is actually used, and clean up  
COPY src/skins/valve /var/www/html/w/skins/valve  
  
# MediaWiki extensions  
COPY src/extensions/AbuseFilter /var/www/html/w/extensions/AbuseFilter  
COPY src/extensions/CategoryTree /var/www/html/w/extensions/CategoryTree  
COPY src/extensions/CodeEditor /var/www/html/w/extensions/CodeEditor  
COPY src/extensions/Echo /var/www/html/w/extensions/Echo  
COPY src/extensions/EmbedVideo /var/www/html/w/extensions/EmbedVideo  
COPY src/extensions/MultimediaViewer
/var/www/html/w/extensions/MultimediaViewer  
COPY src/extensions/NewUserMessage /var/www/html/w/extensions/NewUserMessage  
COPY src/extensions/RedditThumbnail /var/www/html/w/extensions/RedditThumbnail  
COPY src/extensions/Scribunto /var/www/html/w/extensions/Scribunto  
COPY src/extensions/Sentry /var/www/html/w/extensions/Sentry  
COPY src/extensions/UserMerge /var/www/html/w/extensions/UserMerge  
  
# Config templates  
COPY configs/php.ini /usr/local/etc/php/php.ini  
COPY configs/apache.conf /etc/apache2/sites-available/000-default.conf  
COPY configs/LocalSettings.php /var/www/html/w/LocalSettings.php  
  
# Generate config at runtime  
COPY scripts/configure-mediawiki.sh /usr/local/bin/configure-mediawiki  
COPY scripts/configure-blackfire.sh /usr/local/bin/configure-blackfire  
RUN chmod +x /usr/local/bin/configure-*  
  
VOLUME /var/www/html/w/images  
  
# Required environmental variables  
ENV CAPTCHA_SECRET=  
ENV DB_DATABASE='wiki'  
ENV DB_HOST='db'  
ENV DB_TYPE='mysql'  
ENV DB_USER='root'  
ENV SECRET_KEY=  
ENV SERVER_URL='https://tfwiki.localhost'  
ENV SITENAME='Local Team Fortress Wiki'  
# Optional environmental variables  
ENV BLACKFIRE_SOCKET=  
ENV DB_PASSWORD=  
ENV EMAIL_EMERGENCY_CONTACT=  
ENV EMAIL_PASSWORD_SENDER=  
ENV MEMCACHED_HOST=  
ENV SENTRY_DSN=  
ENV SMTP_AUTH=  
ENV SMTP_HOST=  
ENV SMTP_IDHOST=  
ENV SMTP_PASSWORD=  
ENV SMTP_PORT=  
ENV SMTP_USERNAME=  
ENV STEAM_API_KEY=  
ENV VARNISH_HOST=  
  
CMD /usr/local/bin/configure-blackfire && /usr/local/bin/configure-mediawiki
&& apache2-foreground

