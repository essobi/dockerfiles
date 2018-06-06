FROM jamesharv/drupal7:latest  
  
RUN apt-get -y update  
RUN curl -sSL -O https://get.docker.com/builds/Linux/x86_64/docker-1.8.1 &&
chmod +x docker-1.8.1 && sudo mv docker-1.8.1 /usr/local/bin/docker  
RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
RUN apt-get -y install nodejs npm build-essential  
RUN apt-get -y install ack-grep  
RUN apt-get -y install \  
wget \  
git-core \  
zlib1g-dev \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt1-dev \  
libcurl4-openssl-dev \  
python-software-properties \  
libffi-dev  
RUN wget -c http://ftp.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz && \  
tar -xzf ruby-2.2.2.tar.gz && \  
cd ruby-2.2.2 && \  
./configure && \  
make && \  
make install && \  
export PATH="/usr/local/ruby/bin:$PATH" && \  
echo "gem: --no-ri --no-rdoc" > ~/.gemrc && \  
gem update --system && \  
gem install bundler  
RUN apt-get -y install python-dev && pip install awsebcli  
RUN npm install -g bower  
RUN npm install -g gulp  
RUN apt-get -y install vim  
  
ENTRYPOINT bash  

