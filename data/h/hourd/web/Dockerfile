FROM debian  
MAINTAINER Daniel Atkinson <hourd.tasa@gmail.com>  
  
RUN apt-get update \  
&& \  
apt-get install -y --fix-missing \  
aptitude \  
bash \  
vim \  
curl \  
wget \  
php5-json \  
php5-mysql \  
php5-mcrypt \  
php5-sqlite \  
php5-curl \  
php5-gd \  
php5-ldap \  
php5-ssh2 \  
libssh2-php \  
ssh \  
git \  
nodejs \  
apache2 \  
libapache2-mod-php5 \  
supervisor \  
&& \  
wget https://getcomposer.org/composer.phar \  
&& \  
mv composer.phar /bin/composer \  
&& \  
chmod +x /bin/composer \  
&& \  
rm -rf /var/lib/apt/lists/* \  
&& \  
ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load \  
&& \  
mkdir -p /etc/nginx/sites-enabled /var/run/php-fpm /var/log/supervisor
/var/lock/apache2 /var/run/apache2  
  
RUN apt-get update \  
&& \  
apt-get install -y \  
make \  
gcc \  
build-essential \  
openssl \  
libssl-dev \  
pkg-config \  
&& \  
cd /tmp \  
&& \  
wget http://nodejs.org/dist/node-latest.tar.gz \  
&& \  
tar xvzf node-latest.tar.gz \  
&& \  
rm -f node-latest.tar.gz \  
&& \  
cd node-v* \  
&& \  
./configure \  
&& \  
CXX="g++ -Wno-unused-local-typedefs" make \  
&& \  
CXX="g++ -Wno-unused-local-typedefs" make install \  
&& \  
cd /tmp \  
&& \  
rm -rf /tmp/node-v* \  
&& \  
npm install -g npm npm-cache \  
&& \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
ADD .docker/apache/sites-enabled/000-default.conf /etc/apache2/sites-
enabled/000-default.conf  
  
VOLUME ["/var/www", "/etc/nginx/sites-enabled"]  
  
ADD supervisor.ini /etc/supervisor.d/supervisor.ini  
ADD .docker/php/php.ini /etc/php/php.ini  
  
EXPOSE 80  
  
WORKDIR /var/www  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisor.ini"]  

