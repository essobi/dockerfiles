FROM ubuntu:16.04  
  
ENV CONFIGURE_OPTS --disable-install-doc  
ENV PATH /root/.rbenv/versions/2.2.9/bin:/root/.rbenv/bin:$PATH  
ENV RUBYOPT W0  
  
# Install packages for building ruby  
RUN apt-get update && \  
apt-get install -y sudo build-essential vim numactl procps curl libcurl3
libcurl3-gnutls libcurl4-openssl-dev git zlib1g-dev libffi-dev libssl-dev
libreadline-dev libyaml-dev libxml2-dev libxslt-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
git clone https://github.com/sstephenson/rbenv.git /root/.rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build && \  
./root/.rbenv/plugins/ruby-build/install.sh && \  
rbenv install 2.2.9 && echo 'gem: --no-rdoc --no-ri' >> /.gemrc && \  
rbenv global 2.2.9 && gem install bundler && rbenv rehash  

