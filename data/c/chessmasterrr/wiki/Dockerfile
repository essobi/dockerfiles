FROM chessmasterrr/php:latest  
  
# install needed packages:  
# php-apcu as cache for the wiki  
# php-intl for internationalization  
# ca-certificates for the SSL root certificate for communication with the mail
server  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends \  
ca-certificates \  
php-apcu \  
php-intl \  
&& rm -rf /var/lib/apt/lists/*  
  
### set values ###  
# see https://www.mediawiki.org/wiki/MediaWiki for version number  
ENV MEDIAWIKI_VERSION 1.30.0  
# see https://www.mediawiki.org/wiki/Download  
ENV MEDIAWIKI_URL
https://releases.wikimedia.org/mediawiki/1.30/mediawiki-${MEDIAWIKI_VERSION}.tar.gz  
  
### install application ###  
# import gpg keys to verify the downloads  
WORKDIR /var/www/html  
COPY keys.txt keys.txt  
RUN set -xe \  
&& wget --no-check-certificate --no-verbose ${MEDIAWIKI_URL} -O
mediawiki.tar.gz \  
&& wget --no-check-certificate --no-verbose ${MEDIAWIKI_URL}.sig -O
mediawiki.tar.gz.sig \  
&& gpg --import keys.txt \  
&& gpg --verify mediawiki.tar.gz.sig mediawiki.tar.gz \  
&& tar -xz --strip-components=1 -f mediawiki.tar.gz \  
&& rm mediawiki.tar.gz \  
&& rm mediawiki.tar.gz.sig \  
&& rm keys.txt \  
&& chown -R root:root . \  
&& chown -R www-data images  

