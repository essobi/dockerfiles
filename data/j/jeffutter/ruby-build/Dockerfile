FROM ubuntu:14.04  
MAINTAINER Jeffery Utter "jeff@jeffutter.com"  
  
RUN adduser --disabled-login --gecos 'Deploy' deploy ;\  
mkdir -p /home/deploy/sockets /home/deploy/bundle /home/deploy/app  
  
RUN locale-gen en_US.UTF-8 ;\  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale ;\  
dpkg-reconfigure locales  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV HOME /home/deploy  
ENV BUNDLE_PATH /home/deploy/bundle  
WORKDIR /home/deploy/app  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update ;\  
apt-get -y install curl software-properties-common ;\  
apt-add-repository ppa:brightbox/ruby-ng ;\  
rm -rf /var/lib/apt/lists/*  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update ;\  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
advancecomp \  
build-essential \  
curl \  
g++ \  
gifsicle \  
git \  
imagemagick \  
jhead \  
jpegoptim \  
libffi-dev \  
libjpeg-turbo-progs \  
libmysql++-dev \  
libmysqlclient-dev \  
libncurses5-dev \  
libpq-dev \  
libreadline-dev \  
libssl-dev \  
libyaml-dev \  
libxml2-dev \  
libxslt-dev \  
make \  
nginx \  
openssl \  
optipng \  
pdftk \  
phantomjs \  
pngcrush \  
ruby2.2 \  
ruby2.2-dev \  
wget \  
zlib1g-dev \  
# Webkit deps for capybara-webkit  
xvfb \  
dbus-1-dbg \  
qt5-default \  
libqtwebkit-dev \  
libqt5webkit5-dev \  
# Drone  
socat \  
# Passenger  
libcurl4-openssl-dev \  
libpcre3-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& dbus-uuidgen > /etc/machine-id  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
9554F04D7259F04124DE6B476D5A82AC7E37093B
DD8F2338BAE7501E3DD5AC78C273792F7D83545D  
ENV IOJS_VERSION 1.3.0  
  
RUN curl -SLO "https://iojs.org/dist/v$IOJS_VERSION/iojs-v$IOJS_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://iojs.org/dist/v$IOJS_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " iojs-v$IOJS_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "iojs-v$IOJS_VERSION-linux-x64.tar.gz" -C /usr/local --strip-
components=1 \  
&& rm "iojs-v$IOJS_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc  
  
RUN echo 'gem: --no-rdoc --no-ri' >> /home/deploy/.gemrc ;\  
chown deploy:deploy /home/deploy/.gemrc ;\  
gem install --no-rdoc --no-ri bundler  

