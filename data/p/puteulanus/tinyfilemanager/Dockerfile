FROM alpine  
  
ENV PHP_VER 7.1.11  
ENV PHP_URL http://us1.php.net/get/php-$PHP_VER.tar.gz/from/this/mirror  
ENV PHP_DIR php-$PHP_VER  
ENV FM_URL
https://raw.githubusercontent.com/prasathmani/tinyfilemanager/master/tinyfilemanager.php  
  
RUN apk add --no-cache file  
RUN apk add --no-cache --virtual TMP gcc g++ make openssl \  
&& cd /tmp \  
&& wget -O php.tar.gz $PHP_URL \  
&& tar zxf php.tar.gz \  
&& rm -f php.tar.gz \  
&& cd $PHP_DIR \  
&& ./configure --disable-all --enable-session --enable-cli --enable-static \  
&& make -j$(nproc) \  
&& mv sapi/cli/php /usr/local/bin/ \  
&& rm -rf /tmp/$PHP_DIR \  
&& mkdir /web \  
&& wget -O /web/index.php $FM_URL \  
&& apk del TMP  
  
VOLUME /web/file/  
EXPOSE 8080  
CMD php -S 0.0.0.0:8080 -t /web  

