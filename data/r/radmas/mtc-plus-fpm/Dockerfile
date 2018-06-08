FROM ubuntu:xenial  
  
MAINTAINER Fernando Moro <fernando.moro@radmas.com>  
  
LABEL org.mejoratuciudad.vendor="Radmas Technologies"  
LABEL org.mejoratuciudad.image-name="mtc-plus-fpm"  
LABEL version="1.0"  
LABEL description="FPM Application Server and project dependencies."  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# BUILD TOOLS  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y \  
byobu \  
curl \  
git \  
htop \  
man \  
unzip \  
vim \  
wget \  
iputils-ping \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# SUDO  
  
RUN \  
apt-get update && \  
apt-get -y install \  
sudo && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# RADMAS USER  
  
RUN \  
sed -i '/secure_path/d' /etc/sudoers && \  
sed -i '/%sudo/d' /etc/sudoers  
  
RUN \  
sudo useradd radmas --shell /bin/bash --create-home && \  
sudo usermod -a -G sudo radmas && \  
echo '%sudo ALL = (ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
echo 'radmas:d0ck3r' | chpasswd  
  
#################################################  
# PHP  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
language-pack-en-base && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
  
RUN \  
add-apt-repository -y ppa:ondrej/php  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
php5.6 \  
php5.6-dev \  
php5.6-cli \  
php5.6-json \  
php5.6-xml \  
php5.6-curl \  
php5.6-intl \  
php5.6-gd \  
php5.6-mbstring \  
php5.6-zip \  
php5.6-fpm \  
php5.6-xdebug \  
php5.6-mongo \  
php5.6-soap \  
php5.6-redis \  
php5.6-gmp && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
update-alternatives --set php /usr/bin/php5.6  
#################################################  
# EXTRA DEPS  
#################################################  
# AWS cli  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
awscli && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# JAVA 8  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
rm -rf /var/lib/apt/lists/*  
  
# define JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#################################################  
# PYTHON  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
python \  
python-dev \  
python-pip \  
python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
pip install yamllint  
  
#################################################  
# NODE.JS  
  
ENV NODE_VERSION v0.12.17  
  
RUN \  
cd /tmp && \  
wget
http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.gz
&& \  
tar -C /usr/local --strip-components 1 -xzf
node-${NODE_VERSION}-linux-x64.tar.gz && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm@4.5.0  
# define node.js variables  
#ENV PATH node_modules/.bin:$PATH  
#ENV NODE_PATH /usr/local/lib/node_modules  
# Configure NPM for radmas user  
USER radmas  
  
RUN mkdir /home/radmas/npm-global  
  
ENV PATH /home/radmas/npm-global/bin:$PATH  
ENV NODE_PATH /home/radmas/npm-global/lib/node_modules/  
  
RUN npm config set prefix '/home/radmas/npm-global'  
# install node.js dependencies  
RUN \  
npm install -g \  
npm@4.5.0 \  
bower \  
grunt-cli \  
coffee-script \  
less@1.7.5  
# NPM FIX (Prevent docker EXDEV error )  
RUN \  
cd $(npm root -g)/npm && \  
npm install fs-extra && \  
sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
  
#################################################  
# Continue install proccess as root  
USER root  
  
#################################################  
# RUBY  
  
ENV RUBY_VERSION 2.2  
# install ruby from PPA  
RUN \  
add-apt-repository -y ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get install -y \  
ruby${RUBY_VERSION} \  
ruby${RUBY_VERSION}-dev \  
ruby-switch && \  
rm -rf /var/lib/apt/lists/*  
  
# switch default ruby version  
RUN \  
ruby-switch \--set ruby${RUBY_VERSION}  
  
# install ruby gems  
RUN \  
gem install \  
premailer \  
nokogiri  
  
#################################################  
# SUPERVISOR  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/log/supervisor  
  
#################################################  
# DEV DEPS  
#################################################  
# PHPUNIT  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
phpunit && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# BLACKFIRE.IO  
  
RUN \  
wget -O - https://packagecloud.io/gpg.key | apt-key add -  
  
RUN \  
echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
blackfire-agent \  
blackfire-php && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# SQLITE3  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# RUBY (development gems)  
  
RUN gem install bundle mailcatcher --no-rdoc --no-ri  
RUN gem install net-ssh -v 2.9.2 \--no-rdoc --no-ri  
RUN gem install capistrano -v 3.4.0 \--no-rdoc --no-ri  
  
#################################################  
# COMPOSER  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
#################################################  
# PHPMETRICS  
  
RUN wget
https://github.com/Halleck45/PhpMetrics/raw/master/build/phpmetrics.phar && \  
chmod +x phpmetrics.phar && \  
mv phpmetrics.phar /usr/local/bin/phpmetrics  
  
#################################################  
# PHP-CODE-FIXER  
  
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer && \  
chmod a+x php-cs-fixer && \  
mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
#################################################  
# SSH  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
openssh-server && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
#################################################  
# RSYSLOG  
# Install PPA dependencies  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
software-properties-common  
  
# rsyslog PPA  
RUN \  
add-apt-repository ppa:adiscon/v8-stable  
  
# Install rsyslog  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
rsyslog && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# WKHTMLTOPDF  
  
ENV WKHTMLTOPDF_FILENAME wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
ENV WKHTMLTOPDF_LINK
https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz  
  
RUN \  
cd /opt && \  
wget ${WKHTMLTOPDF_LINK} && \  
tar -xJf ${WKHTMLTOPDF_FILENAME} && \  
rm -f ${WKHTMLTOPDF_FILENAME}  
  
RUN ln -s /opt/wkhtmltox/bin/wkhtmltopdf /usr/bin/.  
  
# install WKHTMLTOPDF dependencies  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y --allow-downgrades \  
fontconfig \  
libfontconfig1 \  
libfreetype6 \  
libpng12-0 \  
zlib1g \  
libjpeg-turbo8 \  
libx11-6 \  
libxext6 \  
libxrender1 \  
libstdc++6 \  
libc6 \  
libssl1.0.0=1.0.2g-1ubuntu4 \  
libssl-dev=1.0.2g-1ubuntu4 && \  
apt-mark hold libssl1.0.0 && \  
apt-mark hold libssl-dev && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# CURL HTTP2  
  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install nghttp2 libnghttp2-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
wget https://curl.haxx.se/download/curl-7.54.0.tar.bz2 && \  
tar -xvjf curl-7.54.0.tar.bz2 && \  
cd curl-7.54.0 && \  
./configure --with-nghttp2 --prefix=/usr/local && \  
make && \  
make install && \  
ldconfig  
  
#################################################  
## PHP-LDAP  
# LDAP requirements  
RUN \  
apt-get update && \  
apt-get install -y ldap-utils libldap2-dev  
  
# install ldap for php  
RUN \  
apt-get update -y && \  
apt-get install -y php5.6-ldap && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
ENV DEBIAN_FRONTEND newt  
  
#################################################  
# S6 OVERLAY  
  
USER root  
  
# install s6-overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
ENTRYPOINT ["/init"]  

