FROM phpdockerio/php71-fpm:latest  
  
# Install selected extensions and other stuff  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php7.1-pgsql php-redis php7.1-gd
php-imagick php7.1-mbstring php7.1-xmlrpc php-xdebug php-zmq php7.1-intl
php7.1-bcmath php-zip php7.1-bz2  
  
# install facedetect  
RUN apt-get -y --no-install-recommends install build-essential \  
cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-
dev \  
python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev
libjasper-dev libdc1394-22-dev git php-dev \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
RUN git clone https://github.com/opencv/opencv.git /tmp/opencv \  
&& cd /tmp/opencv \  
&& mkdir release \  
&& cd release \  
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. \  
&& make \  
&& make install  
  
RUN git clone https://github.com/infusion/PHP-Facedetect.git /tmp/PHP-
Facedetect \  
&& cd /tmp/PHP-Facedetect \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install  
  
COPY ./php-ini-overrides.ini /etc/php/7.1/fpm/conf.d/99-overrides.ini  
COPY ./php-ini-overrides.ini /etc/php/7.1/cli/conf.d/99-overrides.ini  
  
COPY ./facedetect.ini /etc/php/7.1/fpm/conf.d/20-facedetect.ini  
COPY ./facedetect.ini /etc/php/7.1/cli/conf.d/20-facedetect.ini  
  
RUN apt-get -y -f purge build-essential cmake git libgtk2.0-dev pkg-config
libavcodec-dev \  
libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev
libjpeg-dev \  
libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev git php-dev \  
&& apt-get -y autoremove && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/* /usr/share/doc/*  

