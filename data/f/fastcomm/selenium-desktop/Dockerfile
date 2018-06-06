############################################################  
# Dockerfile to run Selenium tests on desktop browsers  
############################################################  
  
FROM ubuntu:16.04  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
libsqlite3-dev \  
ruby-dev \  
zlibc \  
zlib1g-dev \  
qt5-default \  
libqt5webkit5-dev \  
nodejs-legacy \  
chromium-chromedriver \  
libgconf-2-4 \  
xvfb \  
wget \  
git \  
less \  
uuid-runtime  
  
# Install zabbix sender  
RUN wget -q http://repo.zabbix.com/zabbix/3.2/ubuntu/pool/main/z/zabbix-
release/zabbix-release_3.2-1+xenial_all.deb && \  
dpkg -i zabbix-release_3.2-1+xenial_all.deb && \  
apt-get update && \  
apt-get install -y zabbix-sender  
  
# Install Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google-chrome.list' && \  
apt-get update && apt-get install -y \  
google-chrome-stable \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Bundler  
RUN gem install bundle && \  
echo "gem: --no-document" >> ~/.gemrc  
  
# Prepare the CI working directory  
WORKDIR /tmp/build  

