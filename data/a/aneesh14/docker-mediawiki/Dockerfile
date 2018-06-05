FROM php:5.6-apache  
MAINTAINER Synctree App Force <appforce+docker@synctree.com>  
  
ENV MEDIAWIKI_VERSION 1.24  
ENV MEDIAWIKI_FULL_VERSION 1.24.2  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
g++ \  
libicu52 \  
libicu-dev \  
unzip \  
&& pecl install intl \  
&& echo extension=intl.so >> /usr/local/etc/php/conf.d/ext-intl.ini \  
&& apt-get purge -y --auto-remove g++ libicu-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mysqli opcache  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends imagemagick \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
RUN
MEDIAWIKI_DOWNLOAD_URL="http://ncu.dl.sourceforge.net/project/bluespice/BlueSpice-
free-2.23.3-installer.zip"; \  
set -x; \  
mkdir -p /usr/src/mediawiki \  
&& curl -fSL "$MEDIAWIKI_DOWNLOAD_URL" -o bluespice.zip \  
&& unzip bluespice.zip \  
&& mv bluespice-free/* /usr/src/mediawiki  
  
RUN rm bluespice.zip && rm -rf bluespiece-free  
  
RUN apt-get update \  
&& apt-get install -y vim wget git php5-gd php5-tidy \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libtidy-dev && \  
docker-php-ext-install tidy && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd  
  
RUN apt-get install -y locate libldb-dev libldap-2.4-2 libldap2-dev  
RUN apt-get install -y php5-pgsql libpq-dev && docker-php-ext-install pgsql  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so  
RUN docker-php-ext-install ldap  
  
RUN wget https://extdist.wmflabs.org/dist/extensions/LdapAuthentication-
REL1_27-b0dba33.tar.gz  
RUN tar -xzf LdapAuthentication-REL1_27-b0dba33.tar.gz -C
/usr/src/mediawiki/extensions  
RUN rm LdapAuthentication-REL1_27-b0dba33.tar.gz  
  
RUN echo "session.save_path = '/tmp'" >
/usr/local/etc/php/conf.d/session_save_path.ini && \  
echo "max_execution_time = 120" >
/usr/local/etc/php/conf.d/max_execution_time.ini && \  
echo "post_max_size = 32M" > /usr/local/etc/php/conf.d/post_max_size.ini && \  
echo "upload_max_filesize = 32M" >
/usr/local/etc/php/conf.d/upload_max_filesize.ini && \  
echo "display_errors = false" > /usr/local/etc/php/conf.d/display_errors.ini
&& \  
echo "upload_tmp_dir = '/tmp'" > /usr/local/etc/php/conf.d/upload_tmp_dir.ini  
  
RUN chmod g+w /tmp  
  
COPY apache/mediawiki.conf /etc/apache2/  
RUN echo Include /etc/apache2/mediawiki.conf >> /etc/apache2/apache2.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

