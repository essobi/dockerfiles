FROM ubuntu:trusty  
MAINTAINER QEdu IT TEAM  
  
#
==============================================================================  
# Ubuntu Linux 14.04  
#
==============================================================================  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN apt-get update \  
&& apt-get upgrade -yq \  
&& apt-get -yq install \  
build-essential \  
python \  
wget \  
bindfs \  
vim \  
git-core \  
g++ \  
autoconf \  
file \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD https://storage.googleapis.com/chrome-builds/headless/chrome-headless.deb
/src/chrome-headless.deb  
  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
gconf-service \  
libgconf-2-4 \  
libnspr4 \  
libnss3 \  
libxss1 \  
libxtst6 \  
libxrender1 \  
libfreetype6 \  
libfontconfig1 \  
libxrandr2 \  
libc6 \  
zlib1g \  
xdg-utils \  
\--no-install-recommends && \  
dpkg -i '/src/chrome-headless.deb' && \  
rm -r /var/lib/apt/lists/*  
  
  
RUN ln -s /opt/stickmanventures/chrome-headless/headless_shell
/usr/bin/google-chrome  
RUN export CHROME_BIN=/usr/bin/google-chrome  
  
#
==============================================================================  
# Install Postgres, MySQL, MongoDB and more dependencies  
#
==============================================================================  
# Add PGDG repository key  
RUN wget -qO - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc \  
| apt-key add -  
  
RUN apt-get update -qq \  
&& apt-get install -y -qq \  
autoconf \  
imagemagick \  
libbz2-dev \  
libevent-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libncurses-dev \  
libcurl4-openssl-dev \  
libffi-dev \  
libgdbm-dev \  
libpq-dev \  
libreadline-dev libreadline6-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
software-properties-common \  
zlib1g-dev \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
" \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/*  
  
RUN useradd --home /home/node -m -U -s /bin/bash node  
  
RUN echo 'Defaults !requiretty' >> /etc/sudoers; \  
echo 'node ALL= NOPASSWD: /usr/sbin/dpkg-reconfigure -f noninteractive tzdata,
/usr/bin/tee /etc/timezone' >> /etc/sudoers;  
  
RUN mkdir -p /var/www  
RUN chown -R node\:node /var/www && chown -R node\:node /usr/local && chown -R
node\:node /home/node  
  
USER node  
  
RUN cd /home/node &&\  
echo 'export PATH=$HOME/local/bin:$PATH' >> ~/.bashrc  
  
ENV NODE_VERSION 8.9.4  
ENV PM2_VERSION 2.4.2  
ENV YARN_VERSION 1.6.0  
ENV HOME /home/node  
  
RUN cd $HOME && mkdir -p $HOME/tmp  
RUN cd $HOME/tmp &&\  
wget
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
&&\  
tar -xzf node-v${NODE_VERSION}-linux-x64.tar.gz -C /usr/local \--strip-
components=1 &&\  
rm node-v${NODE_VERSION}-linux-x64.tar.gz &&\  
npm i -g npm &&\  
npm i -g yarn@$YARN_VERSION &&\  
npm i -g pm2@$PM2_VERSION  

