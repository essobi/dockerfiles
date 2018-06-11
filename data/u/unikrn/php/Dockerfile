FROM php:5.5-fpm  
  
ENV TERM=xterm  
  
RUN echo deb http://httpredir.debian.org/debian stable main contrib
>/etc/apt/sources.list \  
&& echo deb http://security.debian.org/ stable/updates main contrib
>>/etc/apt/sources.list \  
&& curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libgeoip-dev \  
python \  
locales \  
expect-dev \  
geoip-bin geoip-database-contrib \  
nodejs \  
libgmp-dev \  
git\  
redis-server redis-tools \  
&& curl -fsSL https://dev.mysql.com/get/mysql-apt-config_0.7.3-1_all.deb -o
/tmp/mysql.deb \  
&& DEBIAN_FRONTEND=noninteractive MYSQL_SERVER_VERSION=mysql-5.6 dpkg -i
/tmp/mysql.deb \  
&& rm /tmp/mysql.deb\  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-
community-server \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd pdo pdo_mysql mysql mysqli bcmath
mbstring zip gmp \  
&& DEBIAN_FRONTEND=noninteractive MYSQL_SERVER_VERSION=mysql-5.6 apt-get
upgrade -y\  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -fsSL
'https://xcache.lighttpd.net/pub/Releases/3.2.0/xcache-3.2.0.tar.gz' -o
xcache.tar.gz \  
&& mkdir -p xcache \  
&& tar -xf xcache.tar.gz -C xcache --strip-components=1 \  
&& rm xcache.tar.gz \  
&& ( \  
cd xcache \  
&& cp -vr htdocs /var/www/ \  
&& phpize \  
&& ./configure --enable-xcache \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& rm -r xcache \  
&& docker-php-ext-enable xcache  
  
RUN pecl install xdebug && docker-php-ext-enable xdebug \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pecl install geoip && docker-php-ext-enable geoip \  
&& echo "<?php var_dump(geoip_record_by_name('141.30.225.1')); " | php | grep
Dresden -cq || (echo "Geo not working" && exit 1) \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY *.sh /  
RUN chmod u+rwx /*.sh  
  
RUN npm set registry https://npm.bsolut.com \  
&& npm config set always-auth true \  
&& /npm-exp.sh "npm login " docker insecure docker@unikrn.com \  
&& npm install node-tcp-relay pm2 less grunt gulp -g  
  
RUN echo -e "de_DE.UTF-8 UTF-8\nde_DE ISO-8859-1\nde_DE@euro
ISO-8859-15\nen_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen && /usr/sbin/update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
VOLUME /var/lib/redis  
  
EXPOSE 9000 9001 9002 6379  
ADD zzz-unikrn-fpm.conf /usr/local/etc/php-fpm.d/  
ADD unikrn-php.ini /usr/local/etc/php/conf.d/  
ADD unikrn-xdebug.ini /usr/local/etc/php/conf.d/  
ADD mysql-tmpfs.cnf /etc/mysql/conf.d/mysql-tmpfs.cnf  
RUN chmod go-w /etc/mysql/conf.d/mysql-tmpfs.cnf && chown mysql
/etc/mysql/conf.d/mysql-tmpfs.cnf  
  
ENTRYPOINT [ "/run.sh" ]  
  

