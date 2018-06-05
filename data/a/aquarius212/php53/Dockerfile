FROM aquarius212/ffmpeg  
MAINTAINER Michael Bishop <m@aquariusinteractive.com>  
  
RUN apt-get install -y -qq libenchant-dev libsqlite0-dev libenchant-dev libgd-
dev libxpm4 icu-devtools libicu-dev libicu52 libedit-dev libedit2 libtidy-dev
mysql-client apache2-dev apache2 apache2-utils libapache2-mod-encoding
libapache2-mod-spamhaus libapache2-mod-xsendfile memcached && apt-mark hold
php5  
  
  
# PHP 5.3 Cannot find several multiarch headers/libraries  
RUN ln -s /usr/lib/x86_64-linux-gnu/libXpm.so /usr/lib64/libXpm.so && ln -s
/usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h && ldconfig  
RUN mkdir /usr/include/freetype2/freetype && ln -s
/usr/include/freetype2/freetype.h /usr/include/freetype2/freetype/freetype.h  
  
ENV PHP_VERSION 5.3  
WORKDIR /tmp  
RUN wget -q http://php.net/get/php-5.3.28.tar.bz2/from/this/mirror -O
php-5.3.28.tar.bz2 && tar -xf php-5.3.28.tar.bz2  
  
WORKDIR php-5.3.28  
  
RUN CFLAGS="-O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-
security -fsigned-char -fno-strict-aliasing -march=native -mtune=native"
./configure \--build=x86_64-linux-gnu \--host=x86_64-linux-gnu \--program-
prefix= \--prefix=/usr \--exec-prefix=/usr \--bindir=/usr/bin
\--sbindir=/usr/sbin \--sysconfdir=/etc \--datadir=/usr/share
\--includedir=/usr/include \--libdir=/usr/lib64 \--libexecdir=/usr/libexec
\--localstatedir=/var \--sharedstatedir=/var/lib \--mandir=/usr/share/man
\--infodir=/usr/share/info \--cache-file=../config.cache \--with-libdir=lib64
\--with-config-file-path=/etc/php5/apache2 \--with-config-file-scan-
dir=/etc/php5/apache2/conf.d \--disable-debug \--with-pic \--disable-rpath
\--with-exec-dir=/usr/bin \--with-png-dir=/usr \--enable-gd-native-ttf
\--with-t1lib=/usr \--without-gdbm \--with-jpeg-dir=/usr \--with-openssl
\--with-pcre-regex \--with-zlib \--with-layout=GNU \--with-kerberos \--with-
libxml-dir=/usr \--with-mhash \--libdir=/usr/lib64/php \--enable-pcntl
\--enable-mbstring=shared \--enable-mbregex \--enable-calendar=shared
\--enable-bcmath=shared \--with-bz2=static \--enable-ctype=shared \--enable-
exif=shared \--enable-ftp=shared \--with-gettext=shared \--with-iconv=shared
\--enable-sockets=shared \--enable-tokenizer=shared \--with-xmlrpc=shared
\--enable-mysqlnd=shared \--with-mysql=shared,mysqlnd \--with-
mysqli=shared,mysqlnd \--with-mysql-sock=/var/lib/mysql/mysql.sock \--enable-
dom=shared \--enable-simplexml=shared \--enable-xml \--enable-soap=shared
\--with-xsl=shared,/usr \--enable-xmlreader=shared \--enable-xmlwriter=shared
\--with-curl=static \--enable-pdo=shared \--with-pdo-mysql=shared,mysqlnd
\--without-readline \--with-libedit \--enable-phar=static \--with-
mcrypt=shared,/usr \--with-tidy=shared,/usr \--enable-sysvmsg=static
\--enable-sysvshm=static \--enable-sysvsem=static \--enable-shmop=static
\--enable-posix=shared \--enable-fileinfo=shared \--enable-intl=shared
\--with-icu-dir=/usr \--with-enchant=shared,/usr \--with-pear \--with-xpm-
dir=/usr \--with-gd \--with-gmp=shared \--with-libdir=lib64 \--enable-
session=static \--enable-pdo=static \--with-apxs2 \--with-regex=php \--with-
freetype-dir=/usr  
  
RUN mkdir -p /etc/php5/apache2/conf.d && make -j4  
  
RUN cat php.ini-production | tr "\t" " " | sed -e'/short_open_tag =/
s/Off/On/g;/session.gc_probability =/ s/1/0/g;/disable_functions =/ s/$/
pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,/g;'
> php.ini-production  
  
RUN make install && make clean && cp php.ini-development
/etc/php5/apache2/php.ini && ls `php-config \--extension-dir`/*.so -1 | xargs
-L1 -n1 basename | xargs -n1 -I {} printf "extension=%s\n" {} >>
/etc/php5/apache2/conf.d/extensions.ini  
  
RUN pecl config-set php_ini /etc/php5/apache2/conf.d/extensions.ini && pear
config-set php_ini /etc/php5/apache2/conf.d/extensions.ini && pear upgrade
\--force && pear install PHP_Archive-0.11.4 && pecl install -a memcache &&
pecl install -a uploadprogress  
  
  
#ioncube  
WORKDIR /tmp  
RUN wget -q
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.bz2
-O ioncube.tar.bz2 && tar -xf ioncube.tar.bz2  
  
RUN cp ioncube/ioncube_loader_lin_${PHP_VERSION}.so `php-config \--extension-
dir` && rm -rf ioncube  
RUN echo zend_extension=`php-config \--extension-
dir`/ioncube_loader_lin_${PHP_VERSION}.so >
/etc/php5/apache2/conf.d/00-ioncube.ini  
# Set some php ini variables  
ENV PHP_SERVER_INI /files/etc/php5/apache2/php.ini/PHP/  
RUN augtool set ${PHP_SERVER_INI}/upload_max_filesize 500M && augtool set
${PHP_SERVER_INI}/post_max_size 500M && augtool set
${PHP_SERVER_INI}/max_execution_time 7200 && augtool set
${PHP_SERVER_INI}/max_input_time 7200 && augtool set
${PHP_SERVER_INI}/memory_limit 640M && augtool set
${PHP_SERVER_INI}/expose_php off && augtool set
${PHP_SERVER_INI}/short_open_tag on && augtool set
${PHP_SERVER_INI}/include_path /usr/share/pear && augtool set
/files//etc/php5/apache2/php.ini/Date/date.timezone America/New_York  
  
RUN a2dismod mpm_event && a2enmod mpm_prefork && a2enmod rewrite  
  
ADD php.conf /etc/apache2/conf-enabled/  
ADD apache.conf /etc/apache2/sites-available/000-default.conf  
  
ADD crontab /tmp/  
  
RUN crontab crontab  
  
CMD cron && /usr/bin/memcached -d -u memcache && apache2ctl -D FOREGROUND  

