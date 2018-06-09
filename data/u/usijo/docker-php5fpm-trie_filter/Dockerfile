FROM usijo/docker-php5fpm  
MAINTAINER Hongshun Yang<ojisucom@gmail.com>  
  
## support trie-filter  
ENV LIBICONV_VERSION 1.15  
ENV LIBICONV_DOWNLOAD_URL
http://ftp.gnu.org/pub/gnu/libiconv/libiconv-$LIBICONV_VERSION.tar.gz  
  
## libdatrie 0.2.10 not work  
ENV LIBDATRIE_VERSION 0.2.9  
ENV LIBDATRIE_DOWNLOAD_URL
ftp://sourceforge.mirrorservice.org/sites/distfiles.finkmirrors.net/libdatrie-$LIBDATRIE_VERSION.tar.xz  
  
  
RUN apk add -U --virtual build-deps autoconf build-base php5-dev git \  
&& cd /tmp/ \  
&& wget -qO- $LIBICONV_DOWNLOAD_URL | tar xvz \  
&& cd libiconv-$LIBICONV_VERSION \  
&& ./configure && make && make install \  
&& cd /tmp/ \  
&& wget $LIBDATRIE_DOWNLOAD_URL \  
&& tar xvf libdatrie-$LIBDATRIE_VERSION.tar.xz \  
&& cd libdatrie-$LIBDATRIE_VERSION \  
&& ./configure && make && make install \  
&& cd /tmp/ \  
&& git clone https://github.com/wulijun/php-ext-trie-filter.git \  
&& cd php-ext-trie-filter \  
&& phpize \  
&& ./configure && make && make install \  
&& cd ~ \  
&& rm -rf /tmp/* \  
&& apk del -U build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN echo "extension=trie_filter.so" > /etc/php5/conf.d/trie_filter.ini  
  
## trie-filter  

