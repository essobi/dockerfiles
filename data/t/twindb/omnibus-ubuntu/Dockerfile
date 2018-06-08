FROM ubuntu:trusty  
MAINTAINER Ovais Tariq @ovaistariq  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
curl \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libxslt1-dev \  
libxml2-dev \  
libcurl4-gnutls-dev \  
zlib1g-dev \  
libexpat1-dev \  
libicu-dev \  
gnupg2 \  
cmake \  
flex \  
bison \  
automake \  
autoconf \  
libtool \  
libaio-dev \  
mysql-client \  
libncurses-dev \  
libgcrypt11-dev \  
libev-dev \  
vim-common  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
  
RUN bash -lc "rvm requirements; \  
rvm install 2.2.2 ; \  
gem install bundler --no-ri --no-rdoc;\  
"  
  
RUN rm -rf /usr/local/rvm/src/ruby-2.2.2  
  
RUN git clone https://github.com/twindb/backup.git /tmp/backup  
RUN bash -lc "cd /tmp/backup/omnibus; bundle update; bundle install
--binstubs"  
  
CMD /bin/bash -l  

