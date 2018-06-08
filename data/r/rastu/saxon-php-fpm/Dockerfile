FROM php:5.6.25-fpm  
  
COPY install-libsaxon-setup.sh /install-libsaxon-setup.sh  
  
ENV LIBSAXON_VERSION 1.0.2  
ENV LIBSAXON_ARCHITECTURE 64  
ENV LIBSAXON_DOWNLOAD_FILE_NAME libsaxon-HEC-
setup$LIBSAXON_ARCHITECTURE-v$LIBSAXON_VERSION  
ENV DEBIAN_FRONTEND noninteractive  
ENV SAXONC_HOME /usr/lib  
  
RUN apt-get update \  
&& apt-get install -y lib32z1 gcc-multilib gcj-jdk unzip openjdk-7-jre-
headless \  
  
#PREPARE SAXON INSTALLATION  
&& curl -o /libsaxon-setup.zip
http://www.saxonica.com/saxon-c/$LIBSAXON_DOWNLOAD_FILE_NAME.zip \  
&& unzip /libsaxon-setup.zip \  
&& chmod u+x /install-libsaxon-setup.sh \  
&& . /install-libsaxon-setup.sh \  
  
#PREPARE ENVIRONMENT  
&& cp /Saxonica/libsaxonhec.so /usr/lib/ \  
&& cp -r /Saxonica/rt /usr/lib/rt \  
#PHPIZE  
&& cd /Saxonica/Saxon.C.API \  
&& phpize \  
&& ./configure --enable-saxon \  
&& make -j$(nproc) \  
&& make install \  
  
#ENABLE SAXON PHP EXT  
&& docker-php-ext-enable saxon \  
  
#CLEANUP  
&& rm -rf /Saxonica /install-libsaxon-setup.sh /libsaxon-setup.zip
/$LIBSAXON_DOWNLOAD_FILE_NAME \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

