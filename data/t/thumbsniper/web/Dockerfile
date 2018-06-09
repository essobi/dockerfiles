FROM opensuse:42.3  
MAINTAINER Thomas Schulte <thomas@cupracer.de>  
  
EXPOSE 80  
ENV MONGO_HOST=mongo MONGO_PORT=27017 MONGO_USER=thumbsniper MONGO_PASS=secret
MONGO_DB=thumbsniper  
  
RUN zypper --non-interactive ref \  
&& zypper --non-interactive up \  
&& zypper --non-interactive in curl  
  
RUN rpm --import
http://download.opensuse.org/repositories/server:/php:/extensions/openSUSE_Leap_42.3/repodata/repomd.xml.key
\  
&& zypper ar --refresh
http://download.opensuse.org/repositories/server:/php:/extensions/openSUSE_Leap_42.3/server:php:extensions.repo
\  
&& zypper ar --refresh --no-gpgcheck
https://repo.mongodb.org/zypper/suse/12/mongodb-org/3.4/x86_64/ mongodb \  
&& zypper ref  
  
RUN zypper --non-interactive in \  
apache2-mod_php5 \  
gcc \  
git \  
make \  
mongodb-org-shell \  
netcat-openbsd \  
npm \  
openssl-devel \  
php5-curl \  
php5-devel \  
php5-gd \  
php5-geoip \  
php5-intl \  
php5-json \  
php5-mbstring \  
php5-openssl \  
php5-pear \  
php5-phar \  
php5-zip \  
zlib-devel  
  
#RUN curl -o /tmp/pecl-mongodb.tgz https://pecl.php.net/get/mongodb \  
# && mkdir /tmp/pecl-mongodb \  
# && tar xf /tmp/pecl-mongodb.tgz --strip 1 -C /tmp/pecl-mongodb  
#  
#WORKDIR /tmp/pecl-mongodb  
#  
#RUN phpize \  
# && CFLAGS="-fno-strict-aliasing" ./configure --with-libdir=/usr/lib64
--enable-mongo \  
# && make \  
# && make install \  
# && echo "extension=mongodb.so" > /etc/php5/conf.d/mongodb.ini  
#  
#WORKDIR /  
#  
#RUN rm -rf /tmp/pecl-mongodb*  
RUN curl -o /tmp/pecl-mongo.tgz https://pecl.php.net/get/mongo \  
&& mkdir /tmp/pecl-mongo \  
&& tar xf /tmp/pecl-mongo.tgz --strip 1 -C /tmp/pecl-mongo \  
&& cd /tmp/pecl-mongo \  
&& phpize \  
&& CFLAGS="-fno-strict-aliasing" ./configure --with-libdir=/usr/lib64
--enable-mongo \  
&& make \  
&& make install \  
&& cd / \  
&& echo "extension=mongo.so" > /etc/php5/conf.d/mongo.ini \  
&& rm -rf /tmp/pecl-mongo*  
  
RUN curl -s https://getcomposer.org/installer | php -- --install-dir
/usr/local/bin --filename composer  
  
RUN npm install -g bower  
  
COPY etc/apache2 /etc/apache2  
  
RUN a2enmod php5 \  
&& a2enmod logio \  
&& a2enmod expires \  
&& a2enmod headers \  
&& a2enmod remoteip \  
&& a2enmod rewrite \  
&& a2enflag FOREGROUND  
  
#RUN git clone -b master https://github.com/thumbsniper/backend.git
/opt/thumbsniper  
RUN git clone -b v0.9.15 https://github.com/thumbsniper/backend.git
/opt/thumbsniper  
  
RUN composer --working-dir=/opt/thumbsniper update  
  
RUN echo 'always_populate_raw_post_data=-1' >> /etc/php5/apache2/php.ini \  
&& echo 'geoip.custom_directory=/usr/local/share/GeoIP' >>
/etc/php5/apache2/php.ini \  
&& echo 'post_max_size=128M' >> /etc/php5/apache2/php.ini \  
&& echo 'upload_max_filesize=128M' >> /etc/php5/apache2/php.ini \  
&& echo 'include_path=.:/usr/share/php5:/usr/share/php5/PEAR:/opt/thumbsniper'
>> /etc/php5/apache2/php.ini \  
&& echo 'open_basedir=/opt/thumbsniper:/usr/share/php5:/tmp' >>
/etc/php5/apache2/php.ini \  
&& echo 'upload_tmp_dir=/tmp' >> /etc/php5/apache2/php.ini \  
&& echo 'session.save_path=/tmp' >> /etc/php5/apache2/php.ini \  
&& echo 'sys_temp_dir=/tmp' >> /etc/php5/apache2/php.ini \  
&& echo 'error_reporting=E_ALL' >> /etc/php5/apache2/php.ini \  
&& echo 'cgi.fix_pathinfo=0' >> /etc/php5/apache2/php.ini \  
&& echo 'display_errors=Off' >> /etc/php5/apache2/php.ini \  
&& echo 'expose_php=Off' >> /etc/php5/apache2/php.ini \  
&& echo 'log_errors=On' >> /etc/php5/apache2/php.ini \  
&& echo 'date.timezone=Europe/Berlin' >> /etc/php5/apache2/php.ini  
  
WORKDIR /opt/thumbsniper/web_panel  
RUN bower --allow-root --config.interactive=false update  
WORKDIR /  
  
RUN groupmod -g 999 www \  
&& usermod -u 999 -g 999 wwwrun \  
&& chown -R wwwrun /var/cache/apache2 /var/lib/apache2 /var/lib/php5 \  
&& chown wwwrun:www /opt/thumbsniper/web_panel/templates_c  
  
COPY config/backend-config.inc.php /opt/thumbsniper/config/backend-
config.inc.php  
COPY config/panel-config.inc.php /opt/thumbsniper/config/panel-config.inc.php  
  
COPY init.sh /  
  
CMD ["/init.sh"]  

