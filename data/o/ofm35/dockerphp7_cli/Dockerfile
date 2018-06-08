FROM php:7.0.4-cli  
  
RUN sed -i 's/main/main contrib/g' /etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install git cmake -y \  
&& apt-get install libwebp-dev libjpeg-dev libpng-dev libjxr-tools libjxr-dev
libtiff5-dev -y \  
&& apt-get install msttcorefonts libfontconfig1-dev -y  
  
RUN mkdir -p /data/build  
  
# Compile openjp2  
ENV OPENJPEG_VERSION=2.1  
WORKDIR /data/build  
ADD
https://github.com/uclouvain/openjpeg/archive/version.$OPENJPEG_VERSION.tar.gz
openjp2.tar.gz  
RUN tar -xzf openjp2.tar.gz && \  
cd openjpeg* && \  
cmake . && \  
make && \  
make install && \  
make clean  
  
#Compile ImageMagick  
ENV IMAGEMAGICK_VERSION=6.9.3-7  
WORKDIR /data/build  
ADD
http://www.imagemagick.org/download/ImageMagick-$IMAGEMAGICK_VERSION.tar.gz
ImageMagick.tar.gz  
RUN tar -xzf ImageMagick.tar.gz && \  
cd ImageMagick-$IMAGEMAGICK_VERSION && \  
export CFLAGS="-mtune=haswell" && \  
./configure \  
\--with-webp \  
\--with-libtiff \  
\--with-jpeg=yes \  
\--with-openjp2=yes \  
\--with-quantum-depth=8 \  
\--with-png=yes \  
\--with-fontconfig=yes \  
\--with-freetype=yes \  
LIBS=-lfontconfig \  
\--with-windows-font-dir=/usr/share/fonts/truetype/msttcorefonts && \  
make && \  
make install && \  
ldconfig /usr/local/lib  
  
#Compile pecl ImageMagick  
ENV PECL_IMAGEMAGICK_VERSION=3.4.1  
WORKDIR /data/build  
ADD https://pecl.php.net/get/imagick-$PECL_IMAGEMAGICK_VERSION.tgz pecl-
imagick.tgz  
RUN tar -xzf pecl-imagick.tgz && \  
cd imagick-* && \  
phpize && \  
./configure && \  
make && \  
make install  
  
RUN docker-php-ext-install mysqli  
  
RUN mkdir /data/www  
  
RUN echo "extension=imagick.so" > /usr/local/etc/php/php-cli.ini  
  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

