FROM ubuntu:precise  
MAINTAINER Anton Belov anton4@bk.ru  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
# Use source.list with all repositories and Yandex mirrors.  
ADD sources.list /etc/apt/sources.list  
RUN sed -i 's|://.*\\..*\\.com|://ru.archive.ubuntu.com|'
/etc/apt/sources.list  
RUN echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache  
RUN echo 'Acquire::http {No-Cache=True;};' | tee /etc/apt/apt.conf.d/no-http-
cache  
  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
zsh php5-mysql php-apc pwgen python-setuptools python-software-properties
software-properties-common git \  
curl php5-curl php5-gd php5-intl php-pear php5-imagick mc mysql-client \  
php5-imap php5-mcrypt php5-memcache php5-ming php5-ps php5-pspell php5-cli
php5-dev \  
php5-recode php5-sqlite php5-tidy php5-xmlrpc php5-xsl php5-xdebug wget
inetutils-tools inetutils-ping &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
#install utils  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
pv tmux openssh-server nano htop meld expect remmina ssmtp &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
lxde-core lxterminal tightvncserver &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
  
#install sublime text 3  
RUN add-apt-repository ppa:webupd8team/sublime-text-3 && \  
apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y &&
apt-get clean && \  
apt-get -y install \  
sublime-text-installer &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
  
EXPOSE 22  
RUN mkdir -p /root/.ssh  
  
ENV LOGIN admin  
ENV PASS 123q123q  
  
#install nodejs  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
nodejs build-essential &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
  
#ioncube  
WORKDIR /tmp  
RUN wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
tar xvfz ioncube_loaders_lin_x86-64.tar.gz  
RUN echo ioncube/ioncube_loader_lin_${PHP_VERSION}.so `php-config --extension-
dir`  
RUN PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;") && \  
cp ioncube/ioncube_loader_lin_${PHP_VERSION}.so `php-config --extension-dir`
&& rm -rf ioncube && \  
echo zend_extension=`php-config --extension-
dir`/ioncube_loader_lin_${PHP_VERSION}.so >> /etc/php5/php.ini  
  
#install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
wget -q --no-check-certificate
https://raw.github.com/colinmollenhour/modman/master/modman-installer && \  
bash < modman-installer  
  
# mcrypt enable  
RUN ln -s /etc/php5/mods-available/mcrypt.ini
/etc/php5/cli/conf.d/20-mcrypt.ini  
  
# Enabling session files  
RUN mkdir -p /tmp/sessions/  
RUN chown www-data.www-data /tmp/sessions -Rf  
#install n-98 util  
RUN wget http://files.magerun.net/n98-magerun-latest.phar -O n98-magerun.phar  
RUN chmod +x n98-magerun.phar  
RUN cp n98-magerun.phar /usr/local/bin/  
RUN ssh-keyscan -t rsa bitbucket.org > ~/.ssh/known_hosts  
RUN composer config -g github-oauth.github.com
6e18b614391d88b271c1e3f069e55d7fd9bf6e3d  
  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends\  
apt-transport-https \  
build-essential \  
curl \  
ca-certificates \  
git \  
lsb-release \  
python-all \  
rlwrap \  
&& rm -rf /var/lib/apt/lists/*;  
  
RUN npm install -g pangyp\  
&& ln -s $(which pangyp) $(dirname $(which pangyp))/node-gyp\  
&& npm cache clear\  
&& node-gyp configure || echo ""  
  
ENV NODE_ENV production  
  
RUN apt-get update -qq && apt-get install -y build-essential  
RUN apt-get install -y ruby git  
RUN gem install sass  
  
RUN mkdir /src  
WORKDIR /src  
RUN git clone https://github.com/c9/core.git c9sdk  
WORKDIR /src/c9sdk  
RUN scripts/install-sdk.sh  
  
RUN mkdir -p /var/www  
# Configure locales and timezone  
RUN locale-gen en_US.UTF-8  
RUN locale-gen en_GB.UTF-8  
RUN locale-gen fr_CH.UTF-8  
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime  
RUN echo "Europe/Moscow" > /etc/timezone  
RUN mkdir /var/run/sshd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN easy_install pip  
  
EXPOSE 8080  
# Supervisor config  
RUN mkdir /var/log/supervisor  
RUN pip install supervisor  
  
#install java for phpstorm  
RUN add-apt-repository ppa:webupd8team/java && \  
apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y &&
apt-get clean && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | \  
debconf-set-selections &&\  
echo debconf shared/accepted-oracle-license-v1-1 seen true | \  
debconf-set-selections &&\  
apt-get -y install \  
oracle-java8-installer &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
#install nice terminal  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
terminator gedit remmina &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
#install x2go  
RUN add-apt-repository ppa:x2go/stable  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
x2goserver x2goserver-xsession &&\  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory  
#install firefox stable and chromium  
ADD https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb
/src/google-talkplugin_current_amd64.deb  
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
/src/google-chrome-stable_current_amd64.deb  
RUN mkdir -p /usr/share/icons/hicolor && \  
apt-get update && apt-get install -y \  
firefox \  
ca-certificates \  
fonts-liberation \  
wget \  
xdg-utils \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
COPY local.conf /etc/fonts/local.conf  
  
# Install Compass+Ruby  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean && \  
apt-get -y install \  
git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-
dev libsqlite3-dev \  
sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-
properties \  
libgdbm-dev libncurses5-dev automake libtool bison libffi-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -c "source /usr/local/rvm/scripts/rvm" && echo "source
/usr/local/rvm/scripts/rvm" >> ~/.bashrc && \  
/bin/bash -c "source /usr/local/rvm/scripts/rvm && rvm install 2.1.2 && rvm
use 2.1.2 --default"  
#http://blog.acrona.com/index.php?post/2014/05/15/Installer-Fondation-et-
Compass/sass-sur-Ubuntu-14.04  
RUN /bin/bash -c "source /usr/local/rvm/scripts/rvm && gem install compass"  
  
COPY config/supervisor/supervisord.conf /etc/supervisord.conf  
# Magento Initialization and Startup Script  
ADD /scripts /scripts  
ADD /config /config  
RUN chmod 755 /scripts/*.sh  
  
# Startup script  
COPY scripts/start.sh /opt/start.sh  
RUN chmod 755 /opt/start.sh  
  
CMD ["/opt/start.sh"]  

