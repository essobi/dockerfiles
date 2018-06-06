FROM ruby:2.3.4  
  
ENV PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y rsync locales build-essential chrpath libssl-dev libxft-dev
libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev qt5-default
libqt5webkit5-dev gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x
nodejs yarn && \  
curl -L -O https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
&& \  
tar xvjf $PHANTOM_JS.tar.bz2 && \  
mv $PHANTOM_JS /usr/local/share && \  
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin && \  
mkdir -p /root/.phantomjs/2.1.1/x86_64-linux/bin && \  
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs
/root/.phantomjs/2.1.1/x86_64-linux/bin/phantomjs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -i "s/^#\ \\+\\(en_US.UTF-8\\)/\1/" /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  

