FROM maven:3.5.3  
  
RUN \  
apt-get update \  
&& \  
apt-get install -y \  
sudo \  
ruby \  
wget \  
ruby-integration \  
rubygems-integration \  
build-essential \  
ruby-dev \  
python-pip \  
groovy \  
imagemagick \  
software-properties-common \  
python3-software-properties \  
iptraf \  
lsof \  
openjdk-8-jdk \  
openjfx \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& \  
apt-get install -y \  
nodejs \  
xvfb  
  
RUN \  
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key
add - \  
&& \  
wget -O /tmp/google-chrome-stable_current_amd64.deb
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \  
&& \  
apt-get install -f /tmp/google-chrome-stable_current_amd64.deb -y \  
&& \  
rm -rf /tmp/google-chrome-stable_current_amd64.deb  
  
RUN \  
git clone https://github.com/sass/sassc.git --branch 3.2.1 --depth 1
/usr/local/lib/sassc \  
&& \  
git clone https://github.com/sass/libsass.git --branch 3.2.1 \--depth 1
/usr/local/lib/libsass \  
&& \  
echo 'SASS_LIBSASS_PATH="/usr/local/lib/libsass"' >> /etc/environment \  
&& \  
export SASS_LIBSASS_PATH="/usr/local/lib/libsass" \  
&& \  
make -C /usr/local/lib/sassc/ \  
&& \  
ln -s /usr/local/lib/sassc/bin/sassc /usr/local/bin/sassc  
  
RUN \  
npm -g config set user root \  
&& \  
npm install -g gulp \  
&& \  
npm -g install node-sass  
  
RUN \  
apt-get install -y \  
ruby-dev \  
zlib1g-dev \  
liblzma-dev \  
&& \  
gem install \  
hpricot \  
nokogiri \  
premailer \  
&& \  
gem install compass  
  
RUN \  
pip install \  
jinja2 \  
markdown  
  
RUN \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
\  
&& \  
tar jxf phantomjs-1.9.8-linux-x86_64.tar.bz2 -C /usr/local/bin \  
&& \  
ln -s /usr/local/bin/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs \  
&& \  
rm -rf phantomjs-1.9.8-linux-x86_64.tar.bz2  
  
RUN \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \  
&& \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& \  
apt-get update \  
&& \  
apt-get install -y yarn  
  
RUN \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  

