FROM php:7-fpm  
  
MAINTAINER AttractGroup  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
libmemcached-dev \  
libz-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
git  
  
# Install the PHP mcrypt extention  
RUN docker-php-ext-install mcrypt  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get purge --auto-remove -y zlib1g-dev \  
&& apt-get -y install libssl-dev libc-client2007e-dev libkrb5-dev libpq-dev \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install imap \  
&& docker-php-ext-install opcache  
  
#####################################  
# OpCahce  
#####################################  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
#####################################  
# ZipArchive:  
#####################################  
  
RUN pecl install zip && \  
docker-php-ext-enable zip  
  
#####################################  
# Composer:  
#####################################  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#####################################  
# Set Timezone  
#####################################  
  
ARG TZ=UTC  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN composer global require "hirak/prestissimo:^0.3"  
  
# Versions  
ENV OSMOSIS_VERSION 0.44.1  
ENV MAPSFORGE_VERSION 0.6.0  
ENV PHYGHTMAP_VERSION 1.74  
  
#  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install JDK 7 (latest edition)  
RUN apt-get update && apt-get install -y openjdk-7-jdk  
  
# Install Osmosis  
RUN cd /  
RUN wget http://bretth.dev.openstreetmap.org/osmosis-
build/osmosis-${OSMOSIS_VERSION}.tgz  
RUN mkdir /osmosis  
RUN tar xvfz osmosis-${OSMOSIS_VERSION}.tgz --directory=/osmosis  
RUN rm osmosis-${OSMOSIS_VERSION}.tgz  
RUN chmod a+x /osmosis/bin/osmosis  
ENV PATH /osmosis/bin:$PATH  
RUN echo 'export PATH=$PATH:/osmosis/bin' > /etc/profile.d/osmosis.sh  
RUN chmod 775 /etc/profile.d/osmosis.sh  
  
# Install Osmosis Mapsforge Map Writer  
RUN wget http://repo.jenkins-ci.org/public/org/mapsforge/mapsforge-map-
writer/${MAPSFORGE_VERSION}/mapsforge-map-writer-${MAPSFORGE_VERSION}-jar-
with-dependencies.jar  
RUN mv mapsforge-map-writer-${MAPSFORGE_VERSION}-jar-with-dependencies.jar
/osmosis/lib/default/  
  
# Install Python  
RUN apt-get update && apt-get -y install python2.7 python-pip  
RUN pip install sh && \  
pip install logging && \  
pip install setuptools  
  
# Install phyghtmap  
RUN apt-get update && apt-get -y install python-matplotlib python-
beautifulsoup python-numpy python-gdal  
RUN wget
http://katze.tfiu.de/projects/phyghtmap/phyghtmap_${PHYGHTMAP_VERSION}.orig.tar.gz  
RUN tar -xzf phyghtmap_${PHYGHTMAP_VERSION}.orig.tar.gz  
RUN cd phyghtmap-${PHYGHTMAP_VERSION} && python setup.py install  
RUN rm phyghtmap_${PHYGHTMAP_VERSION}.orig.tar.gz  
RUN rm -rf phyghtmap-${PHYGHTMAP_VERSION}  
  
  
# install nodejs && npm  
RUN apt-get install -y nodejs-legacy  
RUN apt-get install -y npm

