FROM yenpai/jetbrains-base:latest  
MAINTAINER Robin Chen <yenpai.mis@gmail.com>  
  
# Add PHP repository to apt source  
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" \  
> /etc/apt/sources.list.d/php5-5.6.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C  
  
# Install tools, php-fpm and composer  
RUN apt-get update -qqy && \  
apt-get install -qqy --no-install-recommends \  
wget sudo git subversion \  
php5-fpm php5-cli php5-sqlite php5-mysql php5-mcrypt \  
php5-curl php5-json php5-gd php5-geoip php5-xdebug \  
php5-xmlrpc php5-xcache && \  
apt-get clean && \  
apt-get autoremove -qqy && \  
rm -rf /var/lib/apt/lists/* && \  
php -r "readfile('https://getcomposer.org/installer');" | \  
php -- --install-dir=/usr/local/bin --filename=composer  
  
# Install PhpStorm  
RUN wget --quiet \  
\--output-document=/tmp/phpstorm.tar.gz \  
\--no-check-certificate --no-cookies \  
http://download.jetbrains.com/webide/PhpStorm-10.0.3.tar.gz && \  
mkdir -p /opt/phpstorm && \  
tar zxvf /tmp/phpstorm.tar.gz --strip-components=1 -C /opt/phpstorm && \  
rm -f /tmp/*  
  
# Setup Path  
ENV HOME="/home/developer" \  
WORKSPACE="/work"  
# Create workspace/home, add group/account, sudo  
RUN export uid=1000 gid=1000 && \  
mkdir -p ${WORKSPACE} && mkdir -p ${HOME} && \  
echo "developer:x:${uid}:${gid}:Developer,,,:${HOME}:/bin/bash" >> /etc/passwd
&& \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R ${HOME}  
  
# USER, WORKDIR, ENTRYPOINT  
USER developer:developer  
WORKDIR $WORKSPACE  
ENTRYPOINT ["/opt/phpstorm/bin/phpstorm.sh"]  
  

