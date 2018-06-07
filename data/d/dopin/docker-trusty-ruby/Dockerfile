FROM ubuntu:trusty  
MAINTAINER dopin "dopinninja@gmail.com"  
  
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
RUN echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get -y \--force-yes install \  
build-essential \  
curl \  
git-core \  
nginx \  
libcurl4-openssl-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
zlib1g-dev && \  
curl -O http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.3.tar.gz && \  
tar -zxvf ruby-2.1.3.tar.gz && \  
cd ruby-2.1.3 && \  
./configure --disable-install-doc && \  
make && \  
make install && \  
cd .. && \  
rm -r ruby-2.1.3 ruby-2.1.3.tar.gz && \  
echo 'gem: --no-document' > /usr/local/etc/gemrc  
  
# Install Bundler for each version of ruby  
RUN \  
echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \  
gem install bundler  
  

