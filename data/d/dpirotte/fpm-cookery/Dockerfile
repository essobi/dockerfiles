FROM buildpack-deps:xenial  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
ruby \  
ruby-dev \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install fpm fpm-cookery --no-rdoc --no-ri  

