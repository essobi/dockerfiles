# Panubo PHP-Apache  
#  
# Debian 8  
# PHP 5.6  
# Apache 2.4  
# Mongo support  
#  
FROM debian:8  
MAINTAINER Tim Robinson <tim@panubo.com>  
  
ENV S6_RELEASE=1.20.0 S6_VERSION=2.5.1.0
S6_SHA1=b798972cbf46e28f1c5d238f6703aba6edded57e  
ENV VOLTGRID_PIE=1.0.6
VOLTGRID_PIE_SHA1=11572a8ea15fb31cddeaa7e1438db61420556587  
  
# Change the www-data use to uid and gid 48 to match other containers  
RUN \  
usermod -u 48 www-data && \  
groupmod -g 48 www-data  
  
# Install main packages  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y wget curl ca-
certificates git openssh-client msmtp-mta python-jinja2 apache2 apache2-mpm-
event libapache2-mod-xsendfile imagemagick ghostscript php5-fpm php5-cli
php5-curl php5-apcu php5-gd php5-imap php5-intl php5-ldap php5-mcrypt
php5-mysql php5-pgsql php5-sqlite php5-redis php5-igbinary php5-imagick
php5-pspell php5-recode php5-xmlrpc php5-memcached php-http-request2 && \  
echo 'deb http://repo.suhosin.org/ debian-jessie main' >>
/etc/apt/sources.list && \  
wget -O- https://sektioneins.de/files/repository.asc | apt-key add - && \  
apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y php5-suhosin-
extension && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/www/html/*  
  
# Install php mongo extension  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y php5-dev re2c
make pkg-config && \  
pecl install mongo && \  
echo "; priority=99\nextension = mongo.so" > /etc/php5/mods-
available/mongo.ini && \  
apt-get --purge autoremove -y php5-dev re2c make pkg-config && apt-get clean
&& rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*  
  
# Add Volt Grid .py / .conf  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -s -L https://github.com/voltgrid/voltgrid-
pie/archive/v${VOLTGRID_PIE}.tar.gz -o voltgrid-pie.tar.gz && \  
sha1sum voltgrid-pie.tar.gz && \  
echo "${VOLTGRID_PIE_SHA1} voltgrid-pie.tar.gz" | sha1sum -c - && \  
tar -C /usr/local/bin --strip-components 1 -zxf voltgrid-pie.tar.gz voltgrid-
pie-${VOLTGRID_PIE}/voltgrid.py && \  
rm -rf ${DIR} && \  
echo '{"user":{"uid":0,"gid":0}}' > /usr/local/etc/voltgrid.conf  
  
# Install s6  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
curl -s -L https://github.com/just-
containers/skaware/releases/download/v${S6_RELEASE}/s6-${S6_VERSION}-linux-
amd64-bin.tar.gz -o s6.tar.gz && \  
echo "${S6_SHA1} s6.tar.gz" | sha1sum -c - && \  
tar -xzf s6.tar.gz -C /usr/local/ && \  
rm -rf ${DIR}  
  
# Configure  
RUN \  
mkdir /root/.ssh && \  
echo "Host *\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config && \  
sed -i -e '/^session.save_/ s/^/;/' /etc/php5/*/php.ini && \  
touch /var/log/msmtp.log && \  
chown www-data:www-data /var/log/msmtp.log && \  
sed -i -r 's/^Listen.*/Listen 8000/g' /etc/apache2/ports.conf && \  
sed -i 's/^error_log.*/error_log = \/dev\/stderr/' /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -E 's/^;?systemd_interval.*/systemd_interval = 0/' /etc/php5/fpm/php-
fpm.conf && \  
mv /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf_orig  
  
COPY apache2.conf /etc/apache2/conf-available/php5-fpm.conf  
COPY php.d /etc/php5/mods-available  
COPY msmtprc /etc/msmtprc  
COPY php-fpm.conf /etc/php5/fpm/pool.d/www.conf  
COPY voltgrid.conf /usr/local/etc/voltgrid.conf  
COPY s6 /etc/s6/  
COPY php-extras /usr/share/php/  
  
RUN \  
php5enmod suhosin session mongo && \  
a2dissite 000-default && \  
a2disconf security && \  
a2enconf php5-fpm && \  
a2enmod proxy_fcgi remoteip rewrite headers  
  
ENV TMPDIR=/var/tmp TERM=dumb  
EXPOSE 8000  
ENTRYPOINT ["/usr/local/bin/voltgrid.py"]  
CMD ["/usr/local/bin/s6-svscan", "/etc/s6"]  

