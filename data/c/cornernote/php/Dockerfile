FROM dmstr/php-yii2:7.2-fpm-4.2  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install system packages  
RUN apt-get update && \  
apt-get -y install \  
cron \  
vim \  
ghostscript \  
percona-toolkit \  
\--no-install-recommends  
  
# Install supervisor  
RUN apt-get -y install \  
supervisor \  
python-pip && \  
pip install supervisor-stdout  
  
# Install lockrun  
ADD https://raw.githubusercontent.com/pushcx/lockrun/master/lockrun.c
lockrun.c  
RUN apt-get -y install \  
gcc && \  
gcc lockrun.c -o lockrun && \  
cp lockrun /usr/local/bin/ && \  
rm -f lockrun.c  
  
# Install gearman  
RUN apt-get -y install \  
libgearman-dev && \  
cd /tmp && \  
git clone https://github.com/wcgallego/pecl-gearman.git && \  
cd pecl-gearman && \  
phpize && \  
./configure && \  
make && \  
make install && \  
docker-php-ext-enable gearman && \  
rm -rf /tmp/pecl-gearman  
  
# Install geoip  
ADD
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
GeoIP.dat.gz  
RUN gunzip GeoIP.dat.gz && \  
mkdir /usr/share/GeoIP/ && \  
mv GeoIP.dat /usr/share/GeoIP/ && \  
chmod a+r /usr/share/GeoIP/GeoIP.dat && \  
rm -f GeoIP.dat.gz  
  
# Install mysqli  
RUN docker-php-ext-install mysqli && \  
docker-php-ext-enable mysqli  
  
# Install mailparse  
RUN pecl install mailparse && \  
docker-php-ext-enable mailparse  
  
# Install pcntl  
RUN docker-php-ext-install pcntl && \  
docker-php-ext-enable pcntl  
  
# Install ssh2  
RUN apt-get -y install \  
libssh2-1-dev && \  
git clone https://github.com/php/pecl-networking-ssh2.git
/usr/src/php/ext/ssh2 && \  
docker-php-ext-install ssh2  
  
# Install imap  
RUN apt-get -y install \  
libc-client-dev \  
libkrb5-dev && \  
docker-php-ext-configure imap \  
\--with-kerberos \  
\--with-imap-ssl && \  
docker-php-ext-install imap  
  
# Install tidy  
RUN apt install -y libtidy-dev && \  
docker-php-ext-install tidy && \  
docker-php-ext-enable tidy  
  
# Install memcached  
RUN apt-get -y install \  
libpq-dev \  
libmemcached-dev && \  
curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-
memcached/archive/php7.tar.gz" && \  
mkdir -p /usr/src/php/ext/memcached && \  
tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 && \  
docker-php-ext-configure memcached && \  
docker-php-ext-install memcached && \  
rm /tmp/memcached.tar.gz  
  
# Install wkhtmltopdf  
ADD https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN apt-get -y install \  
wkhtmltopdf \  
build-essential \  
openssl \  
libssl1.0-dev \  
xorg \  
xvfb && \  
tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
mv wkhtmltox/bin/wkhtmlto* /usr/bin/ && \  
rm -rf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz wkhtmltox/  
  
# Install mscorefonts  
ADD http://ftp.us.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-
mscorefonts-installer_3.6_all.deb ttf-mscorefonts-installer_3.6_all.deb  
RUN apt-get -y install \  
wget \  
cabextract && \  
dpkg -i ttf-mscorefonts-installer_3.6_all.deb && \  
rm -f ttf-mscorefonts-installer_3.6_all.deb  
  
# Cleanup  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy configuration files  
COPY files/ /  
  
# forward logs to docker log collector  
RUN ln -sf /usr/sbin/cron /usr/sbin/crond  
  
# Run supervisor  
CMD ["/usr/bin/supervisord"]  

