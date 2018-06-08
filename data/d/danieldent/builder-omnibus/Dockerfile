FROM ubuntu:15.04  
MAINTAINER Daniel Dent (https://www.danieldent.com/)  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV LANG=en_US.UTF-8  
ADD http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc
/tmp/erlang_solutions.asc  
ADD https://deb.nodesource.com/gpgkey/nodesource.gpg.key
/tmp/nodesource.gpg.key  
ADD https://apt.dockerproject.org/gpg /tmp/docker.gpg.key  
ADD https://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest/SALTSTACK-GPG-
KEY.pub /tmp/saltstack.gpg.key  
  
WORKDIR /tmp  
RUN apt-get update -q && \  
apt-get install -y locales apt-transport-https && \  
locale-gen "en_US.UTF-8" && \  
echo "86232086a4dec44a5a505544d30822987a23a892db418f9e8e17dfff21eb0c23
erlang_solutions.asc" | sha256sum -c && \  
echo "773b328f7b1d6db58a8c6a7fc89e2ed58ac5e06c3ab148411cf8272be7b1c472
nodesource.gpg.key" | sha256sum -c && \  
echo "c836dc13577c6f7c133ad1db1a2ee5f41ad742d11e4ac860d8e658b2b39e6ac1
docker.gpg.key" | sha256sum -c && \  
echo "2bdcf4c30cdfd672aacb9eeff4d78b5e0cf9d405b82b1645ad5a876ec8e5037a
saltstack.gpg.key" | sha256sum -c && \  
apt-key add erlang_solutions.asc && \  
apt-key add nodesource.gpg.key && \  
apt-key add docker.gpg.key && \  
apt-key add saltstack.gpg.key && \  
echo "deb http://apt.dockerproject.org/repo ubuntu-vivid main" >
/etc/apt/sources.list.d/docker.list && \  
echo 'deb http://deb.nodesource.com/node_4.x vivid main' >
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb http://packages.erlang-solutions.com/ubuntu vivid contrib" >
/etc/apt/sources.list.d/erlang-solutions.list && \  
echo "deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/2015.8 trusty main"
> /etc/apt/sources.list.d/saltstack.list && \  
apt-get update -q && \  
apt-get dist-upgrade -y && \  
apt-get install -y build-essential wget curl git erlang-base=1:18.2 erlang-
dev=1:18.2 erlang-eunit=1:18.2 \  
erlang-xmerl=1:18.2 elixir=1.2.0-1 nodejs=4.4.0-1nodesource1~vivid1 docker-
engine=1.9.1-0~vivid python-pip \  
inotify-tools postgresql-client jed nano mtr-tiny lsof rsync rdate dnsutils
dstat ifstat bwm-ng mosh telnet \  
sysstat php5-cli php5-curl php5-mysql php5-pgsql php5-gd mysql-client
php5-mysql php-getid3 php5-fpm php5-dev \  
php5-json salt-master salt-minion salt-ssh salt-syndic salt-cloud net-tools
iputils-ping && \  
wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
echo "ee414ce42f071b78ed90d2cc3e388e6a77f8fbefa0e2d092b93a4014552ae1fc
ioncube_loaders_lin_x86-64.tar.gz"|sha256sum -c && \  
tar -xvvzf ioncube_loaders_lin_x86-64.tar.gz && \  
mv ioncube/ioncube_loader_lin_5.6.so /usr/lib/php5/20131226 && \  
rm -Rf ioncube_loaders_lin_x86-64.tar.gz ioncube && \  
echo "zend_extension = ioncube_loader_lin_5.6.so" > /etc/php5/mods-
available/ioncube.ini && \  
ln -s /etc/php5/mods-available/ioncube.ini /etc/php5/fpm/conf.d/01-ioncube.ini
&& \  
ln -s /etc/php5/mods-available/ioncube.ini /etc/php5/cli/conf.d/01-ioncube.ini
&& \  
pear install PHP_CodeSniffer && \  
pip install docker-compose && \  
mix local.hex --force && \  
mix local.rebar --force && \  
curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin && \  
mkdir /app && \  
apt-get clean -y  
WORKDIR /app  

