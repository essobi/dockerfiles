#  
# nZEDb Dockerfile  
#  
# Use baseimage-docker  
FROM phusion/baseimage:0.10.1  
# Set maintainer  
MAINTAINER butlerpeter <https://github.com/butlerpeter/nzedb-docker>  
  
# Set correct environment variables.  
ENV TZ Europe/London  
ENV HOME /root  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV TERM xterm  
  
# Update /etc/default/locale  
RUN update-locale  
  
# Regenerate SSH host keys.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Configure SSH access to container  
RUN \  
sed -i 's/^#Port 22/Port 22/' /etc/ssh/sshd_config && \  
sed -i 's,^#HostKey /etc/ssh_host_rsa_key,HostKey /etc/ssh/ssh_host_rsa_key,'
/etc/ssh/sshd_config && \  
sed -i 's,^#HostKey /etc/ssh_host_dsa_key,HostKey /etc/ssh/ssh_host_dsa_key,'
/etc/ssh/sshd_config && \  
sed -i 's/^#LoginGraceTime 2m/LoginGraceTime 2m/' /etc/ssh/sshd_config && \  
sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \  
sed -i 's/^#StrictModes yes/StrictModes yes/' /etc/ssh/sshd_config && \  
sed -i 's/^#RSAAuthentication yes/RSAAuthentication yes/' /etc/ssh/sshd_config
&& \  
sed -i 's/^#PubkeyAuthentication yes/PubkeyAuthentication yes/'
/etc/ssh/sshd_config && \  
sed -i 's,^#AuthorizedKeysFile.*,AuthorizedKeysFile .ssh/authorized_keys,'
/etc/ssh/sshd_config  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Make sure system is up-to-date.  
RUN \  
# sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
# sed -i
's#http://archive.ubuntu.com/ubuntu#http://mirror.aarnet.edu.au/pub/ubuntu/archive#g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y dist-upgrade && \  
locale-gen en_US.UTF-8  
  
# Install base software.  
RUN apt-get install -y nano sudo curl git htop man htop nmon vnstat tcptrack
bwm-ng mytop software-properties-common python-software-properties unzip vim
wget tmux ntp ntpdate time  
  
# Install PHP.  
RUN \  
add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y \  
php7.0 \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-dev \  
php7.0-fpm \  
php7.0-gd \  
php7.0-json \  
php-pear \  
php7.0-mysql \  
php7.0-pdo \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-imagick  
  
# Configure PHP  
RUN \  
sed -ri 's/(max_execution_time =) ([0-9]+)/\1 120/' /etc/php/7.0/cli/php.ini
&& \  
sed -ri 's/(memory_limit =) ([0-9]+)/\1 -1/' /etc/php/7.0/cli/php.ini && \  
sed -ri 's/;(date.timezone =)/\1 Europe\/London/' /etc/php/7.0/cli/php.ini &&
\  
sed -ri 's/(max_execution_time =) ([0-9]+)/\1 120/' /etc/php/7.0/fpm/php.ini
&& \  
sed -ri 's/(memory_limit =) ([0-9]+)/\1 1024/' /etc/php/7.0/fpm/php.ini && \  
sed -ri 's/;(date.timezone =)/\1 Europe\/London/' /etc/php/7.0/fpm/php.ini &&
\  
mkdir /run/php && \  
chmod -R 777 /var/lib/php/sessions && \  
sed -i 's/^listen =.*/listen = 127.0.0.1:9000/'
/etc/php/7.0/fpm/pool.d/www.conf  
  
# Install ffmpeg, mediainfo, p7zip-full, unrar and lame.  
RUN \  
curl https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz |
tar xfvJ - -C /usr/local/bin && \  
apt-get install -y unrar-free lame mediainfo p7zip-full ffmpeg libav-tools  
# apt-get install -y unrar-free lame mediainfo p7zip-full libav-tools  
# Install unrar  
RUN \  
mkdir -p /tmp/new_unrar && cd /tmp/new_unrar && \  
wget http://www.rarlab.com/rar/rarlinux-x64-5.5.0.tar.gz && \  
tar -xzf rarlinux*.tar.gz && \  
mv /usr/bin/unrar /usr/bin/unrar4 && \  
mv rar/unrar /usr/bin/unrar && \  
chmod 755 /usr/bin/unrar && \  
cd / && rm -rf /tmp/new_unrar  
  
# Install yEnc  
RUN \  
mkdir -p /tmp/yenc && cd /tmp/yenc && \  
wget
https://ayera.dl.sourceforge.net/project/yydecode/yydecode/0.2.10/yydecode-0.2.10.tar.gz
&& \  
tar xzf yydecode-0.2.10.tar.gz && cd yydecode-0.2.10 && \  
apt-get install -y gcc make && \  
./configure && make && make install && \  
cd /tmp && \  
rm -rf yenc && \  
wget https://github.com/niel/php-
yenc/releases/download/v1.3.0/php7.0-yenc_1.3.0_amd64.deb && \  
apt-get -f install && \  
dpkg -i php7.0-yenc_1.3.0_amd64.deb  
  
# Install tmux version 2  
RUN \  
apt-get install -y libevent-dev build-essential git autotools-dev automake
pkg-config ncurses-dev && \  
apt remove -y tmux && \  
cd /tmp && \  
git clone https://github.com/tmux/tmux.git --branch 2.0 --single-branch && \  
cd tmux && ./autogen.sh && ./configure && make -j4 && make install && make
clean && \  
cd / && rm -rf /tmp/tmux  
  
# Install certificates  
RUN \  
wget -P /etc/ssl/certs/ http://curl.haxx.se/ca/cacert.pem && \  
chmod 744 /etc/ssl/certs/cacert.pem  
  
# Install MariaDB.  
#RUN \  
# apt-get install -y mariadb-server mariadb-client libmysqlclient-dev && \  
# sed -i 's/^max_allowed_packet.*/max_allowed_packet = 16M/' /etc/mysql/my.cnf
&& \  
# sed -i '/key_buffer.*/a group_concat_max_len = 8192' /etc/mysql/my.cnf && \  
# sed -i 's/^key_buffer.*/key_buffer = 256M/' /etc/mysql/my.cnf && \  
# sed -i '/key_buffer.*/a key_buffer_size = 256M' /etc/mysql/my.cnf && \  
# sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf  
# Install Python MySQL modules.  
#RUN \  
# apt-get install -y python-setuptools software-properties-common
python3-setuptools python3-pip python-pip && \  
# python -m easy_install pip && \  
# easy_install cymysql && \  
## easy_install pynntp && \  
## easy_install socketpool && \  
# pip list && \  
# python3 -m easy_install pip && \  
# easy_install3 cymysql && \  
## easy_install3 pynntp && \  
## easy_install3 socketpool && \  
# pip3 list  
# Install simple_php_yenc_decode.  
#RUN \  
# cd /tmp && \  
# git clone https://github.com/kevinlekiller/simple_php_yenc_decode.git && \  
# cd simple_php_yenc_decode/source/ && \  
# apt-get install -y swig libboost-regex-dev g++  
#RUN \  
# cd /tmp/simple_php_yenc_decode/source/ && \  
# swig -php -c++ yenc_decode.i && \  
# g++ `php-config7.1 --includes` -fpic -c yenc_decode_wrap.cpp && \  
# g++ -fpic -c yenc_decode.cpp -lboost_rege && \  
# g++ -shared *.o -o simple_php_yenc_decode.so -lboost_regex && \  
# cd ~ && \  
# rm -rf /tmp/simple_php_yenc_decode/  
# Install memcached.  
RUN apt-get install -y memcached  
  
# Install and configure nginx.  
RUN \  
apt-get install -y nginx && \  
echo '\ndaemon off;' >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx && \  
mkdir -p /var/log/nginx && \  
chmod 755 /var/log/nginx  
ADD nZEDb /etc/nginx/sites-available/nZEDb  
RUN \  
unlink /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/nZEDb /etc/nginx/sites-enabled/nZEDb  
  
# Setup the Composer installer.  
RUN \  
curl -o /tmp/composer-setup.php https://getcomposer.org/installer && \  
curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig && \  
php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !==
trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-
setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }" && \  
cd /tmp && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer  
  
# Clone nZEDb master and set directory permissions  
#RUN \  
# mkdir /var/www && \  
# cd /var/www && \  
# git clone https://github.com/nZEDb/nZEDb.git && \  
# chown www-data:www-data nZEDb/www -R && \  
# cd /var/www/nZEDb && \  
# composer install --no-dev --prefer-source && \  
# chmod -R 777 /var/www/nZEDb  
# Add services.  
RUN mkdir /etc/service/nginx  
ADD nginx.sh /etc/service/nginx/run  
RUN mkdir /etc/service/php7.0-fpm && mkdir /var/log/php-fpm  
ADD php-fpm.sh /etc/service/php7.0-fpm/run  
#RUN mkdir /etc/service/mariadb  
#ADD mariadb.sh /etc/service/mariadb/run  
# Add nZEDb.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD nZEDb.sh /etc/my_init.d/nZEDb.sh  
  
# Install SSH key.  
ADD id_rsa.pub /tmp/key.pub  
RUN cat /tmp/key.pub >> /root/.ssh/authorized_keys && rm -f /tmp/key.pub  
  
# Update SSL CA bundles  
#RUN \  
# update-ca-certificates && \  
# cd /etc/ssl/certs/ && \  
# wget https://curl.haxx.se/ca/cacert.pem && \  
# chmod -R 777 *  
# Define mountable directories  
VOLUME ["/etc/nginx/sites-enabled", "/var/log", "/var/www/nZEDb",
"/var/lib/mysql"]  
  
# Expose ports  
EXPOSE 8810  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

