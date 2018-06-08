FROM debian:jessie  
  
MAINTAINER Smart Pension <dev@smartpension.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_BASE_PACKAGES build-essential autoconf locales ca-certificates
locales apt-utils \  
libyaml-dev libxml2-dev libssl-dev libreadline-dev zlib1g zlib1g-dev \  
libevent-dev libsqlite3-dev libxslt1-dev libxml2-dev libfontconfig1-dev
libnss3-dev libgconf2-dev \  
wget vim git netcat sudo curl zip \  
libmysqlclient-dev mysql-client wkhtmltopdf imagemagick file \  
gnupg apt-transport-https ca-certificates software-properties-common \  
groff python-dev python-pip \  
qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base gstreamer1.0-tools
gstreamer1.0-x xvfb  
  
# Add backports repo  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free' >> /etc/apt/sources.list  
  
RUN apt-get update && apt-get upgrade --assume-yes && apt-get dist-upgrade
--assume-yes && \  
(apt-get install --assume-yes $DEBIAN_BASE_PACKAGES || apt-get update --fix-
missing) && \  
(apt-get install --assume-yes $DEBIAN_BASE_PACKAGES || echo "no need to
install") &&\  
apt-get autoremove && apt-get autoclean && apt-get clean  
  
# Set timezone + locale  
RUN echo "en_GB.UTF-8 UTF-8\nen_US.UTF-8 UTF-8" > /etc/locale.gen && locale-
gen && dpkg-reconfigure -f noninteractive locales && \  
echo "LANG=en_GB.UTF-8" > /etc/default/locale && \  
echo "Europe/London" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
ENV LANG en_GB.UTF-8  
# Add google apt repo and chrome  
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& add-apt-repository "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" \  
&& apt-get -y -qq update \  
&& apt-get install --assume-yes google-chrome-stable  
  
# Add chromedriver  
ENV CHROMEDRIVER_VERSION 2.29  
ADD
http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
/usr/local/bin/  
RUN cd /usr/local/bin/ \  
&& unzip chromedriver_linux64.zip \  
&& rm chromedriver_linux64.zip \  
&& cd -  
  
ENV NONROOTUSER containeruser  
ENV NONROOTHOME /home/$NONROOTUSER  
  
# Add a non-root user and permit them to do all with sudo  
RUN adduser --disabled-password --gecos --create-home --home $NONROOTHOME
\--shell /bin/bash $NONROOTUSER  
RUN echo "root ALL=(ALL:ALL) ALL \n $NONROOTUSER ALL=(ALL) NOPASSWD: ALL" >>
/tmp/sudoers.new  
RUN sudo EDITOR="cp /tmp/sudoers.new" visudo  
  
# Install docker  
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \  
&& apt-key fingerprint 0EBFCD88 \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable" \  
&& apt-get -y -qq update \  
&& apt-get -y -qq install docker-ce  
  
## Install awscli from pip anf diff-cover  
RUN pip install awscli  
RUN pip install diff_cover  
  
# ruby-install (ruby installer)  
ENV RUBYINSTALL_VERSION 0.6.1  
RUN wget -O ruby-install-$RUBYINSTALL_VERSION.tar.gz
https://github.com/postmodern/ruby-
install/archive/v$RUBYINSTALL_VERSION.tar.gz &&\  
tar -xzvf ruby-install-$RUBYINSTALL_VERSION.tar.gz &&\  
rm ruby-install-$RUBYINSTALL_VERSION.tar.gz &&\  
cd ruby-install-$RUBYINSTALL_VERSION/ &&\  
make install &&\  
cd /  
  
# nvm (nodejs installer)  
ENV NVM_VERSION 0.33.1  
ENV NVM_DIR /usr/local/nvm  
RUN wget -O nvm-$NVM_VERSION.tar.gz
https://github.com/creationix/nvm/archive/v$NVM_VERSION.tar.gz &&\  
tar -xzvf nvm-$NVM_VERSION.tar.gz &&\  
rm nvm-$NVM_VERSION.tar.gz &&\  
cp -a ./nvm-$NVM_VERSION /opt/nvm &&\  
mkdir -m 777 /usr/local/nvm &&\  
mkdir -m 777 /usr/local/node  
  
# Change to the non-root user  
USER $NONROOTUSER  
  
# Build nodejs  
ENV NODE_VERSION 6.10.0  
RUN bash -c 'source /opt/nvm/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default '  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
RUN npm install yarn --global  
  
# Build ruby, update gem and setup bundler  
ENV RUBYVERSION 2.3.4  
RUN ruby-install ruby $RUBYVERSION \  
&& rm -rf $NONROOTHOME/src/ruby-$RUBYVERSION  
ENV RUBYBINPATH $NONROOTHOME/.rubies/ruby-$RUBYVERSION/bin  
ENV PATH $RUBYBINPATH:$PATH  
RUN echo 'gem: --no-rdoc --no-ri' > $NONROOTHOME/.gemrc \  
&& gem update --system \  
&& gem install bundler  

