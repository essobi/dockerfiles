# dkdde/jenkins-worker:node-8_ruby-2.5  
FROM ubuntu:bionic-20180426  
  
LABEL maintainer.first="Nicolai Reuschling 'nicolai.reuschling@dkd.de'"  
# Setup environment  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Add user jenkins  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins  
  
# Setup locale  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends locales &&\  
locale-gen en_US.UTF-8 de_DE.UTF-8 && localedef -i en_US -f UTF-8 en_US.UTF-8  
  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o
Dpkg::Options::="--force-confnew" \--no-install-recommends \  
openssh-client \  
curl \  
locales \  
git-core \  
libxslt-dev \  
libxml2-dev \  
libmysqlclient-dev \  
build-essential \  
sqlite3 \  
libsqlite3-dev \  
libcurl4-openssl-dev \  
imagemagick \  
libmagickwand-dev \  
net-tools  
  
# Create local cache directories  
RUN mkdir -p {/home/jenkins/.ssh,/home/jenkins/composer-
cache,/home/jenkins/.npm,/home/jenkins/bundler-cache} &&\  
chown -R jenkins:jenkins {/home/jenkins/.ssh,/home/jenkins/composer-
cache,/home/jenkins/.npm,/home/jenkins/bundler-cache} &&\  
chmod -R 0700 {/home/jenkins/.ssh,/home/jenkins/composer-
cache,/home/jenkins/.npm,/home/jenkins/bundler-cache}  
  
  
# Install JDK (v8)  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o
Dpkg::Options::="--force-confnew" \--no-install-recommends \  
openjdk-8-jre-headless  
  
  
# Install Ruby (v2.5)  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o
Dpkg::Options::="--force-confnew" \--no-install-recommends \  
apt-transport-https \  
ca-certificates \  
software-properties-common &&\  
add-apt-repository ppa:brightbox/ruby-ng &&\  
apt-get update -q  
  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o
Dpkg::Options::="--force-confnew" \--no-install-recommends \  
ruby2.5 \  
ruby2.5-dev  
  
  
# Install NodeJS (v8.10.0)  
RUN curl -SLO "https://nodejs.org/dist/v8.10.0/node-v8.10.0-linux-x64.tar.xz"
&&\  
tar -xJf "node-v8.10.0-linux-x64.tar.xz" -C /usr/local --strip-components=1
&&\  
ln -s /usr/local/bin/node /usr/local/bin/nodejs &&\  
rm /node-v8.10.0-linux-x64.tar.xz  
  
# Install npm (v5.7.1)  
RUN npm install -g npm@5.7.1  
# Cleanup  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q autoremove &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q clean -y &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /var/cache/apt/*.bin  

