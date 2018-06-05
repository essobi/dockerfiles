FROM ruby:2.3.4  
  
ARG BUILD_DEPS="autoconf \  
bison \  
build-essential \  
cmake \  
curl \  
git \  
libffi-dev \  
libfontconfig1 \  
libfontconfig1-dev \  
libfreetype6 \  
libfreetype6-dev \  
libgdbm-dev \  
libgdbm3 \  
libgit2-dev \  
libncurses5-dev \  
libpq-dev \  
libreadline6-dev \  
libssl-dev \  
libxft-dev \  
libyaml-dev \  
nodejs \  
postgresql-client \  
python \  
python-dev \  
python-pip \  
software-properties-common \  
unzip \  
zlib1g-dev"  
  
# Don't use for now  
ARG NIGHTMARE_DEPS="xvfb \  
x11-xkb-utils \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-scalable \  
xfonts-cyrillic \  
x11-apps \  
clang \  
libdbus-1-dev \  
libgtk2.0-dev \  
libnotify-dev \  
libgnome-keyring-dev \  
libgconf2-dev \  
libasound2-dev \  
libcap-dev \  
libcups2-dev \  
libxtst-dev \  
libxss1 \  
libnss3-dev \  
gcc-multilib \  
g++-multilib \  
libgtk2.0-0"  
  
ARG NODE_VERSION=7  
ARG DOCKER_VERSION=17.04.0-ce  
ARG PHANTOMJS_VERSION=phantomjs-2.1.1-linux-x86_64  
  
RUN (curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash -) &&
\  
apt install -y --no-install-recommends --fix-missing ${BUILD_DEPS} && \  
curl -L -o /tmp/docker-${DOCKER_VERSION}.tgz
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \  
tar -xz -C /tmp -f /tmp/docker-${DOCKER_VERSION}.tgz && \  
mv /tmp/docker/* /usr/bin && \  
wget
https://github.com/Medium/phantomjs/releases/download/v2.1.1/${PHANTOMJS_VERSION}.tar.bz2
&& \  
tar xjf ${PHANTOMJS_VERSION}.tar.bz2 && \  
mv ${PHANTOMJS_VERSION} /usr/local/share && \  
ln -sf /usr/local/share/${PHANTOMJS_VERSION}/bin/phantomjs /usr/local/bin && \  
pip install -q awscli 'docker-compose==1.12.0' && \  
npm install -g yarn && \  
curl -Ls https://convox.com/install/linux.zip > /tmp/convox.zip && \  
unzip /tmp/convox.zip -d /usr/local/bin && \  
curl -L -o /usr/local/bin/wait-for-it
https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
&& \  
chmod +x /usr/local/bin/wait-for-it && \  
gem install rubygems-update --version 2.6.3 && gem update --system 2.6.10 && \  
gem install bundler && \  
bundle config --global ignore_messages true && \  
echo '[[ "${CIRCLE_BRANCH}" == "master" ]] && exec "$@" || true' >
/usr/local/bin/if_master && \  
chmod +x /usr/local/bin/if_master  
  
  
  
  

