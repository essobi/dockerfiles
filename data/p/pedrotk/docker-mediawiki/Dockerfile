FROM php:5.6.15-apache  
MAINTAINER Yuichi Saotome <y@sotm.jp>  
  
ENV MEDIAWIKI_VERSION 1.26  
ENV MEDIAWIKI_FULL_VERSION 1.26.0  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
g++ \  
libicu52 \  
libicu-dev \  
git vim curl wget libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libmcrypt-dev libxml2-dev libpq-dev libpq5 postgresql-client \  
&& pecl install intl apcu \  
&& echo extension=intl.so >> /usr/local/etc/php/conf.d/ext-intl.ini \  
&& echo "extension=apcu.so\napc.enable_cli=1" >>
/usr/local/etc/php/conf.d/ext-apcu.ini \  
&& apt-get purge -y --auto-remove g++ libicu-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
mysqli opcache mbstring zip gd xml pdo pdo_pgsql soap  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends imagemagick \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
# https://www.mediawiki.org/keys/keys.txt  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
441276E9CCD15F44F6D97D18C119E1A64D70938E \  
41B2ABE817ADD3E52BDA946F72BC1C5D23107F8A \  
162432D9E81C1C618B301EECEE1F663462D84F01 \  
1D98867E82982C8FE0ABC25F9B69B3109D3BB7B0 \  
3CEF8262806D3F0B6BA1DBDD7956EE477F901A30 \  
280DB7845A1DCAC92BB5A00A946B02565DC00AA7  
  
RUN
MEDIAWIKI_DOWNLOAD_URL="https://releases.wikimedia.org/mediawiki/$MEDIAWIKI_VERSION/mediawiki-$MEDIAWIKI_FULL_VERSION.tar.gz";
\  
set -x; \  
mkdir -p /usr/src/mediawiki \  
&& curl -fSL "$MEDIAWIKI_DOWNLOAD_URL" -o mediawiki.tar.gz \  
&& curl -fSL "${MEDIAWIKI_DOWNLOAD_URL}.sig" -o mediawiki.tar.gz.sig \  
&& gpg --verify mediawiki.tar.gz.sig \  
&& tar -xf mediawiki.tar.gz -C /usr/src/mediawiki --strip-components=1  
  
COPY apache/mediawiki.conf /etc/apache2/  
RUN echo Include /etc/apache2/mediawiki.conf >> /etc/apache2/apache2.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

