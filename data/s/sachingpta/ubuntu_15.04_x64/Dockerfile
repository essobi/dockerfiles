# buildpack-deps provides full batteries-included images. With them, a
majority of arbitrary  
# gem install / npm install / pip install should be successfull without
additional header/development  
# packages.  
#  
# SRC: https://hub.docker.com/_/buildpack-deps/  
# Set the base image to Ubuntu v15.10 (x64) OS.  
FROM ubuntu:15.10  
# Author or maintainer of this image file  
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  
  
# All packages must work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
# Add add-apt-repository command  
RUN apt-get -qq update > /dev/null && apt-get install -qq -y --no-install-
recommends \  
python-software-properties \  
apt-file \  
software-properties-common > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
# Add All Package Source  
RUN add-apt-repository -y main > /dev/null && \  
add-apt-repository -y universe > /dev/null && \  
add-apt-repository -y restricted > /dev/null && \  
add-apt-repository -y multiverse > /dev/null  
  
# Update all installed packages  
RUN apt-get update -qq -y > /dev/null && \  
apt-get upgrade -qq -y > /dev/null && \  
apt-get dist-upgrade -qq -y > /dev/null && \  
apt-get -qq -y autoremove > /dev/null && \  
apt-get clean > /dev/null  
  
# Replication Of "buildpack-deps:xenial-curl" Package  
# https://github.com/docker-library/buildpack-
deps/blob/2da658b9a1b91fa61d63ffad2ea52685cac6c702/xenial/curl/Dockerfile  
RUN apt-get -qq -y update > /dev/null && apt-get install -qq -y --no-install-
recommends \  
apt-utils \  
ca-certificates \  
curl \  
wget \  
sudo > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
# Replication Of "buildpack-deps:xenial-scm" Package  
# procps is very common in build systems, and is a reasonably small package  
RUN apt-get -qq -y update > /dev/null && apt-get install -qq -y --no-install-
recommends \  
bzr \  
git \  
mercurial \  
openssh-client \  
subversion \  
procps > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
# Replication Of "buildpack-deps:xenial" Package  
# https://github.com/docker-library/buildpack-
deps/blob/11492c68d993221fd5cd4d8a980354634fc165dd/xenial/Dockerfile  
# Also added many other essential packages  
RUN apt-get -qq -y update > /dev/null && apt-get install -qq -y --no-install-
recommends \  
autoconf \  
automake \  
bzip2 \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgdbm-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libkrb5-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libxslt1-dev \  
libyaml-dev \  
make \  
patch \  
xz-utils \  
zlib1g-dev \  
build-essential \  
libqt4-webkit \  
libqt4-dev \  
xvfb \  
checkinstall \  
yum \  
gedit > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
#-------------------------------------------------------------------  
# Print Current Directory  
#-------------------------------------------------------------------  
RUN echo "Current Directory Is:" && \  
pwd  
  
#-------------------------------------------------------------------  
# Install Various Packages for ZIP / UnZip  
#-------------------------------------------------------------------  
# Install Various Packages for ZIP / UnZip  
RUN apt-get -qq -y update > /dev/null && apt-get install -qq -y --no-install-
recommends \  
p7zip \  
p7zip-full \  
p7zip-rar \  
unace \  
unrar \  
zip \  
unzip \  
xz-utils \  
sharutils \  
rar \  
uudeview \  
mpack \  
arj \  
cabextract \  
file-roller > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
#-------------------------------------------------------------------  
# Install JDK v1.8.0_111  
#-------------------------------------------------------------------  
RUN mkdir /opt/jdk > /dev/null && \  
cd /opt > /dev/null && \  
wget --quiet --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz > /dev/null && \  
tar -zxf jdk-8u111-linux-x64.tar.gz -C /opt/jdk > /dev/null && \  
update-alternatives --install /usr/bin/java java
/opt/jdk/jdk1.8.0_111/bin/java 100 > /dev/null && \  
update-alternatives --install /usr/bin/javac javac
/opt/jdk/jdk1.8.0_111/bin/javac 100 > /dev/null && \  
rm -rf jdk-8u111-linux-x64.tar.gz > /dev/null && \  
cd / > /dev/null  
  
# Verify installed version  
RUN java -version  
  
#-------------------------------------------------------------------  
# Install & check python 2.7.10  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV PYTHON_VERSION 2.7.10  
ENV PYTHON_DIR /Python-$PYTHON_VERSION  
RUN export PYTHON_VERSION=2.7.10  
RUN export PYTHON_DIR=/Python-$PYTHON_VERSION  
  
# Download zip file, extact, install python  
RUN wget --quiet
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz >
/dev/null && \  
tar xzf Python-$PYTHON_VERSION.tgz > /dev/null && \  
rm -rf Python-$PYTHON_VERSION.tgz > /dev/null && \  
cd Python-$PYTHON_VERSION > /dev/null && \  
sudo ./configure > /dev/null && \  
sudo make --quiet altinstall > /dev/null  
  
# Install other python dependencies  
RUN apt-get update > /dev/null && apt-get install -y --no-install-recommends \  
python-dev \  
python-pip \  
python-virtualenv > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
# Verify installed version  
RUN python --version  
  
#-------------------------------------------------------------------  
# Install & check python 3.4.3  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV PYTHON3_VERSION 3.4.3  
ENV PYTHON3_DIR /Python-$PYTHON3_VERSION  
RUN export PYTHON3_VERSION=3.4.3  
RUN export PYTHON3_DIR=/Python-$PYTHON3_VERSION  
  
# Download zip file, extact, install python  
RUN wget --quiet
https://www.python.org/ftp/python/$PYTHON3_VERSION/Python-$PYTHON3_VERSION.tgz
> /dev/null && \  
tar xzf Python-$PYTHON3_VERSION.tgz > /dev/null && \  
rm -rf Python-$PYTHON3_VERSION.tgz > /dev/null && \  
cd Python-$PYTHON3_VERSION > /dev/null && \  
sudo ./configure > /dev/null && \  
sudo make --quiet altinstall > /dev/null  
  
# Install other python dependencies  
RUN apt-get update > /dev/null && apt-get install -y --no-install-recommends \  
python3-dev \  
python3-pip \  
python3-virtualenv > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null  
  
# Verify installed version  
RUN python3 --version  
  
#-------------------------------------------------------------------  
# Install & check node.js 7.4.0 & npm 4.0.5 (integrated with node.js)  
# http://www.hostingadvice.com/how-to/install-nodejs-ubuntu-14-04/  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV NODE_VERSION 7.4.0  
RUN export NODE_VERSION=7.4.0  
  
ENV NODEBASE /usr/local  
RUN export NODEBASE=/usr/local  
  
# Install Node.js  
RUN cd / > /dev/null  
RUN apt-get install -qq -y --no-install-recommends xz-utils > /dev/null  
RUN wget --quiet https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz > /dev/null  
RUN tar -C $NODEBASE \--strip-components 1 -xJf node-v$NODE_VERSION-
linux-x64.tar.xz > /dev/null  
  
RUN ls -l $NODEBASE/bin/node  
RUN ls -l $NODEBASE/bin/npm  
  
# Verify Installed Version  
RUN node -v  
RUN npm -v  
  
#-------------------------------------------------------------------  
# Install & Bower 1.8.0, Grunt v1.0.1 and Grunt-CLI v1.2.0  
#-------------------------------------------------------------------  
RUN npm install -g bower@1.8.0 > /dev/null  
RUN npm install -g grunt-cli@1.2.0 > /dev/null  
RUN npm install -g grunt@1.0.1 > /dev/null  
  
# Verify installed version  
RUN bower -v  
RUN grunt --version  
  
#-------------------------------------------------------------------  
# install Ruby and Bundler  
#-------------------------------------------------------------------  
# Skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
ENV RUBY_MAJOR 2.3  
ENV RUBY_VERSION 2.3.1  
ENV RUBY_DOWNLOAD_SHA256
b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
ENV RUBYGEMS_VERSION 2.6.7  
# Some of ruby's build scripts are written in ruby  
# We purge this later to make sure our final image uses what we just built  
RUN set -ex \  
&& buildDeps=' \  
bison \  
libgdbm-dev \  
ruby \  
' \  
&& apt-get update > /dev/null \  
&& apt-get install -y --no-install-recommends $buildDeps > /dev/null \  
&& rm -rf /var/lib/apt/lists/* > /dev/null \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" > /dev/null \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - > /dev/null \  
&& mkdir -p /usr/src/ruby > /dev/null \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 > /dev/null \  
&& rm ruby.tar.gz > /dev/null \  
&& cd /usr/src/ruby > /dev/null \  
&& { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new &&
mv file.c.new file.c > /dev/null \  
&& autoconf > /dev/null \  
&& ./configure --disable-install-doc > /dev/null \  
&& make --quiet -j"$(nproc)" > /dev/null \  
&& make --quiet install > /dev/null \  
&& apt-get purge -y --auto-remove $buildDeps > /dev/null \  
&& gem update --system $RUBYGEMS_VERSION > /dev/null \  
&& rm -r /usr/src/ruby > /dev/null  
  
ENV BUNDLER_VERSION 1.13.6  
RUN gem install bundler --version "$BUNDLER_VERSION" > /dev/null  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" > /dev/null \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN" > /dev/null  
  
#Cleanup  
CMD [ "irb" ]  
  
# Verify installed version  
RUN ruby --version  
RUN gem --version  
RUN bundle --version  
RUN bundler --version  
  
#-------------------------------------------------------------------  
# install Jekyll  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV JEKYLL_VERSION 3.3.1  
RUN export JEKYLL_VERSION=3.3.1  
  
# Install Jekyll  
RUN gem install jekyll -v $JEKYLL_VERSION > /dev/null  
  
# Verify installed version  
RUN jekyll --version  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

