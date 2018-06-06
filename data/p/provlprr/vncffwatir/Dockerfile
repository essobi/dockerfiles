FROM ubuntu:14.04  
  
## Install LXDE and VNC server  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal
tightvncserver && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p ~/.vnc && \  
echo 'Hello!23' | vncpasswd -f > ~/.vnc/passwd && \  
chmod 600 ~/.vnc/passwd  
EXPOSE 5901  
  
## Install custom linux apps  
RUN \  
apt-get update && \  
apt-get install -y \  
supervisor \  
xvfb \  
wget \  
curl \  
git \  
libmysqlclient-dev \  
libpq-dev \  
mailutils \  
fetchmail  
  
## Install Ruby v217  
RUN \  
apt-get update && \  
apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties libffi-dev && \  
cd /tmp && \  
wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.7.tar.gz && \  
tar -xvzf ruby-2.1.7.tar.gz && \  
cd ruby-2.1.7 && \  
./configure --prefix=/usr/local && \  
make && \  
sudo make install && \  
gem install bundler && \  
rm -rf /tmp/ruby-2.1.7  
  
## Install Gems  
RUN \  
apt-get update && apt-get install -y libpq-dev && \  
gem install --no-rdoc --no-ri watir headless rspec zip rest-client mysql2 pg
&& \  
gem uninstall -I watir-webdriver && \  
gem install --no-rdoc --no-ri watir-webdriver --version '0.8.0' && \  
gem uninstall -I selenium-webdriver && \  
gem install --no-rdoc --no-ri selenium-webdriver --version '2.46.2'  
  
## Install firefox ESR  
RUN \  
cd /tmp && \  
wget -O ff.tar.bz2
https://ftp.mozilla.org/pub/firefox/releases/31.8.0esr/linux-x86_64/en-
US/firefox-31.8.0esr.tar.bz2 && \  
tar -xvjf ff.tar.bz2 -C /opt && \  
ln -s /opt/firefox/firefox /usr/bin/firefox && \  
rm -rf /tmp/ff.tar.bz2  
  
## Provide a custom default user profile with user_pref to disable automatic
update  
RUN mkdir -p /root/.mozilla/firefox/  
COPY /custom/ff_profiles/* /root/.mozilla/firefox/  
  
WORKDIR /media/shared  
  
#CMD vncserver :1 -name vnc -geometry 1280x800 && tail -F ~/.vnc/*.log  
CMD vncserver :1 -name vnc -geometry 1408x864 && tail -F ~/.vnc/*.log  

