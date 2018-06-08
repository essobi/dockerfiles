FROM node:9.1-stretch  
LABEL maintainer="hi@liammartens.com"  
  
# set envs  
ENV DEBIAN_FRONTEND=noninteractive  
ENV FFMPEG=snapshot  
ENV LIBAV=12.2  
# install pre deps  
RUN apt-get update && apt-get -y upgrade && apt-get -y install debconf apt-
transport-https lsb-release ca-certificates  
  
# include debian backports  
RUN echo 'deb http://deb.debian.org/debian stretch-backports main' >
/etc/apt/sources.list.d/backports.list  
# include dotdeb  
RUN echo 'deb https://packages.sury.org/php stretch main' >
/etc/apt/sources.list.d/sury-php.list  
RUN curl -L https://packages.sury.org/php/apt.gpg | apt-key add -  
  
# update for new repos  
RUN apt-get update  
  
# install some dependencies  
RUN apt-get -y install tzdata curl perl bash git nano \  
libgtk2.0-0 libgconf-2-4 libasound2 \  
libasound2-plugins \  
libxtst6 libxss1 libnss3 xvfb \  
software-properties-common locales \  
sox lame libavcodec57 libavdevice57 libavfilter6 libavresample3 libavutil55  
  
# install general development packages  
RUN apt-get -y install autoconf make gcc libpcre3-dev g++ build-essential yasm
nasm  
  
# build avconv and install ffmpeg  
RUN apt-get -y install automake libfreetype6 libfreetype6-dev liblcms2-2
liblcms2-dev zlib1g zlib1g-dev \  
libjpeg-dev libpng16-16 libpng-dev libtiff5 libtiff5-dev \  
libwebp-dev libwebp6 libjpeg62-turbo-dev libjpeg62-turbo \  
libass-dev libsdl2-dev libtheora-dev libtool libva-dev \  
libvdpau-dev libvorbis-dev libxcb-util0-dev texinfo \  
wget libx264-dev libx265-dev libmp3lame-dev librtmp-dev \  
libopus-dev libvpx-dev pulseaudio pulseaudio-utils pavucontrol libavutil55 \  
libxv1 libsdl2-2.0-0 libxcb-shape0  
  
RUN git clone git://git.libav.org/libav.git && cd libav && ./configure && make
&& make install  
  
RUN apt-get install -y ffmpeg  
  
# install PHP7  
ENV PHPV=7.1  
RUN apt-get -y install \  
php$PHPV-common \  
php$PHPV-mcrypt \  
php$PHPV-soap \  
php$PHPV-gmp \  
php$PHPV-odbc \  
php$PHPV-mysql \  
php$PHPV-pgsql \  
php$PHPV-sqlite3 \  
php$PHPV-sqlite3 \  
php$PHPV-json \  
php$PHPV-xml \  
php$PHPV-zip \  
php$PHPV-bcmath \  
php$PHPV-opcache \  
php$PHPV-intl \  
php$PHPV-mbstring \  
php$PHPV-gd \  
php$PHPV-xmlrpc \  
php$PHPV-bz2 \  
php$PHPV-curl \  
php$PHPV-phar \  
php$PHPV-fpm \  
php$PHPV-imagick \  
php$PHPV-dev \  
php-yaml  
  
# install php-redis extension  
RUN git clone https://github.com/phpredis/phpredis  
RUN cd phpredis && phpize && ./configure && make && make install  
RUN rm -rf phpredis  
  
# install phalcon  
# RUN git clone --single-branch git://github.com/phalcon/cphalcon  
# RUN cd cphalcon/build && ./install  
# RUN rm -rf cphalcon  
RUN curl -s
"https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh" |
bash  
RUN apt-get install -y php$PHPV-phalcon  
  
# remove build packages  
# keep gcc, g++, build-essential for cargo compiling on docker  
RUN apt-get -y remove php$PHPV-dev libpcre3-dev  
  
# install composer globally  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php && php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
# create additional user  
ENV USER=www  
ENV HOME=/home/www  
  
# remove node user  
RUN userdel node  
RUN groupadd --gid 1000 www  
RUN useradd --uid 1000 --gid www -md $HOME -p "" -s /bin/bash $USER && \  
usermod -aG www-data $USER && \  
usermod -aG audio,pulse,pulse-access $USER  
WORKDIR /home/www  
# install rust  
USER www  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y  
RUN chown -R $USER:$USER $HOME/.cargo  
USER root  
  
# more install  
RUN apt-get -y install libpulse0 alsa-utils  
RUN apt-get -y autoremove  
  
# create directories  
RUN mkdir -p /etc/php/$PHPV /usr/lib/php/$PHPV /var/log/php/$PHPV /var/www &&
\  
chown -R $USER:www-data /etc/php/$PHPV /var/log/php/$PHPV /usr/lib/php/$PHPV
/var/www  
  
# chown timezone files  
RUN touch /etc/timezone /etc/localtime && \  
chown $USER:www-data /etc/localtime /etc/timezone  
  
# Set LOCALE to UTF8  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# set volumes  
VOLUME ["/etc/php/$PHPV", "/var/log/php/$PHPV", "/var/www", "/var/run/dbus"]  
  
# copy run file  
COPY scripts/run.sh $HOME/run.sh  
RUN chmod +x $HOME/run.sh  
  
# copy own file  
COPY scripts/own.sh $HOME/own.sh  
RUN chmod +x $HOME/own.sh  
  
# copy pulse files  
COPY pulse/default.pa /etc/pulse/default.pa  
COPY pulse/client.conf /etc/pulse/client.conf  
COPY pulse/daemon.conf /etc/pulse/daemon.conf  
  
# dbus, x11 and own  
ONBUILD RUN mkdir /tmp/.X11-unix && chown -R root:root /tmp/.X11-unix && chmod
-R 1777 /tmp/.X11-unix  
ONBUILD RUN mkdir $HOME/.config && $HOME/own.sh  
  
ENTRYPOINT $HOME/run.sh

