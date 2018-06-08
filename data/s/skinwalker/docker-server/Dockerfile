FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends apt-utils \  
software-properties-common \  
python-software-properties \  
language-pack-en-base && \  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
  
## Install php nginx mysql supervisor  
RUN apt-get update && \  
apt-get -y -q --no-install-recommends install -y php-fpm php-cli php-gd php-
mcrypt php-mysql php-curl \  
php-intl \  
php-imagick \  
php-json \  
php-pear \  
php-dev \  
php7.1-sqlite \  
nginx \  
curl \  
mysql-server \  
mysql-client \  
unzip \  
sudo \  
nano \  
openssh-server \  
ssh \  
bash-completion \  
openssl \  
ca-certificates \  
wget \  
git \  
phpmyadmin php-mbstring php-gettext \  
supervisor && \  
  
# install composer  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
  
# add user "docker" to use it as default user for working with files  
yes "" | adduser --uid=1000 \--disabled-password docker && \  
echo "docker ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
  
# install composer assets plugin  
sudo -H -u docker bash -c "/usr/local/bin/composer global require
fxp/composer-asset-plugin:~1.1.3" && \  
  
# create and set access to the folder  
mkdir -p /web/docker && \  
echo "<?php echo 'web server is running';" > /web/docker/index.php && \  
chown -R docker:docker /web && \  
  
# add custom php configuration  
phpenmod custom && \  
  
# enable mcrypt module  
phpenmod mcrypt && \  
  
  
echo "mysql-server mysql-server/root_password password" | debconf-set-
selections && \  
echo "mysql-server mysql-server/root_password_again password" | debconf-set-
selections && \  
apt install -y mysql-server && \  
rm -rf /var/lib/apt/lists/*  
  
## Configuration  
RUN sed -i 's/^listen\s*=.*$/listen = 127.0.0.1:9000/'
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = \/var\/log\/php\/cgi.log/'
/etc/php/7.1/fpm/php.ini && \  
sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = \/var\/log\/php\/cli.log/'
/etc/php/7.1/cli/php.ini && \  
sed -i 's/^key_buffer\s*=/key_buffer_size =/' /etc/mysql/my.cnf  
  
COPY configs/root /  
  
# Setting openssh  
RUN mkdir /var/run/sshd  
  
# Clearing and setting authorized ssh keys  
RUN mkdir /home/docker/.ssh  
RUN echo '' > /home/docker/.ssh/authorized_keys  
RUN echo 'First SSH public key' >> /home/docker/.ssh/authorized_keys  
RUN echo 'Second SSH public key' >> /home/docker/.ssh/authorized_keys  
  
# copy custom ssh config  
COPY configs/ssh /etc/ssh/sshd_config  
  
# change root password  
RUN echo "root:root" | chpasswd  
  
RUN /bin/bash /opt/mysql-server  
  
# mongo db  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
  
RUN apt-get update && \  
apt-get install -y --allow-unauthenticated mongodb-org  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
VOLUME ["/web/projects", "/web/www", "/web/markup", "/var/lib/mysql"]  
  
WORKDIR /web  
  
EXPOSE 80 443 2202 3306 9000 27017  
ENTRYPOINT ["/entrypoint.sh"]  

