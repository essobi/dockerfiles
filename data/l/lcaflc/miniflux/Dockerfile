FROM php:5-apache  
MAINTAINER Laurent Corbes <caf@glot.net>  
# add needed git and extra dev packages  
RUN apt-get update && apt-get install -y git  
  
# add needed php modules  
RUN apt-get install -y libsqlite3-dev libcurl4-gnutls-dev && docker-php-ext-
install -j$(nproc) mbstring iconv pdo_sqlite curl  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Configure php  
COPY php-local.conf /usr/local/etc/php/conf.d/  
  
# installing app  
ENV APPDIR /var/www/html  
RUN rm -rf $APPDIR \  
&& cd /var/www \  
&& git clone \--depth 1 https://github.com/miniflux/miniflux.git \  
&& mv /var/www/miniflux $APPDIR \  
&& chown -R www-data:www-data $APPDIR/data  
  
WORKDIR $APPDIR  
  
# installing themes  
RUN cd $APPDIR/themes \  
&& git clone https://github.com/miniflux/theme-bootstrap-light.git bootstrap-
light \  
&& git clone https://github.com/miniflux/theme-bootswatch-cyborg.git
bootswatch-cyborg \  
# && git clone https://github.com/miniflux/theme-cards.git cards \  
&& git clone https://github.com/lcaflc/miniflux-theme-cards.git cards \  
&& git clone https://github.com/miniflux/theme-nostyle.git nostyle \  
&& git clone https://github.com/miniflux/theme-still.git still \  
&& git clone https://github.com/miniflux/theme-green.git green \  
&& git clone https://github.com/miniflux/theme-midnight.git midnight \  
&& git clone https://github.com/miniflux/theme-copper.git copper \  
&& git clone https://github.com/meradoou/hello.git \  
&& git clone -b flat https://github.com/meradoou/hello.git hello-flat \  
&& git clone -b reader https://github.com/meradoou/hello.git hello-reader \  
&& git clone https://github.com/Cygnusfear/Miniflux-Theme-Sun.git sun \  
&& git clone https://github.com/lacereation/minflux-theme.git /tmp/emm && mv
/tmp/emm/themes/* . && rm -rf /tmp/emm \  
&& git clone https://github.com/meradoou/yonta.git \  
&& git clone https://github.com/Debetux/miniflux-theme-compact.git compact \  
&& git clone https://github.com/JoshuaCrewe/reader-theme.git reader \  
&& git clone https://github.com/johnmartin/read.git  
  
VOLUME $APPDIR/data  

