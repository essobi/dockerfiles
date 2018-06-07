FROM ricordanza/develop  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
apt-get install -y build-essential zlib1g-dev libssl-dev libreadline-dev
libyaml-dev libxml2-dev libxslt-dev && \  
git clone https://github.com/sstephenson/rbenv.git ~/.rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-
build && \  
echo 'export PATH="~/.rbenv/bin:$PATH"' >> ~/.bashrc && \  
echo 'eval "$(rbenv init -)"' >> ~/.bashrc && \  
echo 'eval "$(rbenv init -)"' >> /etc/profile && \  
~/.rbenv/bin/rbenv install 2.4.1 && \  
~/.rbenv/bin/rbenv global 2.4.1 && \  
~/.rbenv/bin/rbenv rehash && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

