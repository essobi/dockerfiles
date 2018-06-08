FROM debian:7.6  
MAINTAINER maintain@geneegroup.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install cURL  
RUN apt-get update && apt-get install -y curl apt-utils  
  
# Install PHP 5.5  
RUN echo "deb http://packages.dotdeb.org wheezy-php55 all" >
/etc/apt/sources.list.d/dotdeb-php5.list && \  
(curl -sL http://www.dotdeb.org/dotdeb.gpg | apt-key add -) && \  
apt-get update && apt-get install -y locales gettext php5-fpm php5-cli
php5-intl php5-gd php5-mcrypt php5-mysqlnd php5-redis php5-sqlite php5-curl
php5-ldap libyaml-0-2 && \  
sed -i 's/^listen\s*=.*$/listen = 0.0.0.0:9000/' /etc/php5/fpm/pool.d/www.conf
&& \  
sed -i 's/^error_log\s*=.*$/error_log = syslog/' /etc/php5/fpm/php-fpm.conf &&
\  
sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = syslog/'
/etc/php5/fpm/php.ini && \  
sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = syslog/'
/etc/php5/cli/php.ini  
  
ADD yaml.so /usr/lib/php5/20121212/yaml.so  
RUN echo "extension=yaml.so" > /etc/php5/mods-available/yaml.ini && \  
php5enmod yaml  
  
# Install Friso  
ADD libfriso.so /usr/lib/libfriso.so  
ADD friso.so /usr/lib/php5/20121212/friso.so  
RUN printf
"extension=friso.so\n[friso]\nfriso.ini_file=/etc/friso/friso.ini\n" >
/etc/php5/mods-available/friso.ini && \  
php5enmod friso  
ADD friso /etc/friso  
  
# Install ZeroMQ  
RUN curl -sLo /usr/local/lib/libzmq.so.4.0.0
http://d.genee.cn/packages/zeromq-4/libzmq.so.4.0.0 && \  
curl -sLo /usr/lib/php5/20121212/zmq.so http://d.genee.cn/packages/zmq.so && \  
printf "extension=zmq.so\n" > /etc/php5/mods-available/zmq.ini && \  
ldconfig && php5enmod zmq  
  
# Install Development Tools  
RUN apt-get install -y git  
  
# Setup Locale  
RUN \  
sed -i 's/# en_US.UTF-8/en_US.UTF-8/' /etc/locale.gen && \  
sed -i 's/# zh_CN.UTF-8/zh_CN.UTF-8/' /etc/locale.gen && \  
locale-gen && \  
/usr/sbin/update-locale LANG="en_US.UTF-8" LANGUAGE="en_US:en"  
  
# Install msmtp-mta  
RUN apt-get install -y msmtp-mta  
ADD msmtprc /etc/msmtprc  
  
# Install Oracle  
RUN apt-get install -y alien libaio1 && \  
curl -sLo /tmp/oracle.rpm \  
http://d.genee.cn/packages/oracle-
instantclient11.2-basiclite-11.2.0.4.0-1.x86_64.rpm && \  
alien -i /tmp/oracle.rpm  
  
RUN curl -sLo /usr/lib/php5/20121212/oci8.so
http://d.genee.cn/packages/oci8.so && \  
echo "extension=oci8.so" > /etc/php5/mods-available/oci8.ini && \  
php5enmod oci8  
  
# Install xlsx2csv  
RUN apt-get install -y python-setuptools && \  
easy_install xlsx2csv  
  
EXPOSE 9000  
# Add interactive shell  
ADD interactive.sh /interactive.sh  
  
ADD start /start  
CMD ["/start"]  

