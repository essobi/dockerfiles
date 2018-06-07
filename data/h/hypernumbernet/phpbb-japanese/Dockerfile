FROM php:5-apache  
  
MAINTAINER Tomohito Inoue <hypernumbernet@users.noreply.github.com>  
  
RUN a2enmod rewrite  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y curl unzip bzip2 libpq-dev libpng-dev libjpeg-dev git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli pgsql  
  
WORKDIR /var/www/html  
  
ENV PHPBB_VERSION 3.1.12  
ENV PHPBB_URL
https://www.phpbb.com/files/release/phpBB-${PHPBB_VERSION}.tar.bz2  
ENV PHPBB_SHA 14476397931bc73642a2144430b7ed45db75bcd51369b0115ca34c755602fb65  
ENV PHPBB_FILE phpBB.tar.bz2  
  
RUN set -xe \  
&& curl -fSL ${PHPBB_URL} -o ${PHPBB_FILE} \  
&& echo "${PHPBB_SHA} ${PHPBB_FILE}" | sha256sum -c - \  
&& tar -xjf ${PHPBB_FILE} \--strip-components=1 \  
&& rm ${PHPBB_FILE}  
  
WORKDIR /tmp  
  
ENV PHPBB_LANG_URL 'https://github.com/ocean0yohsuke/phpBB3_language_ja.git'  
ENV PHPBB_LANG_DIR 'phpBB3_language_ja/root'  
RUN git clone ${PHPBB_LANG_URL} \  
&& cp -pr ${PHPBB_LANG_DIR}/* /var/www/html \  
&& rm -r ${PHPBB_LANG_DIR}  
  
WORKDIR /var/www/html  
  
RUN chown -R www-data:www-data .  

