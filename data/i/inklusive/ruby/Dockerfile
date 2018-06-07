FROM ubuntu:14.04  
# git for git-ls and ruby gems, so I can run 'bundle install' inside a
container  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libffi-dev \  
wget \  
git  
  
# delete all the apt list files since they're big and get stale quickly  
# this forces "apt-get update" in dependent images, which is also good  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
RUN wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz  
RUN tar -xvzf ruby-*  
RUN cd ruby-* && ./configure --prefix=/opt/ruby && make install  
RUN rm -r /tmp/ruby-*  
  
RUN useradd -m app --home /app --shell /bin/bash  
  
ENV PATH /opt/ruby/bin:$PATH  
ENV HOME /app  
ENV GEM_HOME /cache/gems/2.3.1  
# `gem install --user-install` will download binaries to ~/.gem/ruby/2.3.1/bin  
# This path will have precedence over the cached path binaries  
# User install path for 2.3.1 will be ~/.gem/ruby/2.3.1/bin  
ENV PATH $PATH:$HOME/.gem/ruby/2.3.0/bin:/cache/gems/2.3.1/bin  
  
# This will setup the cache dir in case it doesn't get mounted by the user  
RUN mkdir -p /cache/gems/2.3.1  
RUN chown app:app /cache/gems/2.3.1  
  
USER app  
WORKDIR /app  
  
RUN gem install --user-install bundler  

