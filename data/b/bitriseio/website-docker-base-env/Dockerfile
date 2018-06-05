FROM ubuntu:14.04  
RUN apt-get update -qq  
  
# Environments  
# - Language  
RUN apt-get install -y debconf sudo apt-utils locales  
RUN locale-gen --purge en_US.UTF-8  
ENV LANG "en_US.UTF-8"  
ENV LANGUAGE "en_US.UTF-8"  
ENV LC_ALL "en_US.UTF-8"  
RUN dpkg-reconfigure --frontend=noninteractive locales  
# RUN update-locale LANG="en_US.UTF-8"  
# Essentials  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential wget
curl  
  
# ------------------------------------------------------  
# --- Pre-installed but not through apt-get  
# install Ruby from source  
# from source: mainly because of GEM native extensions,  
# this is the most reliable way to use Ruby no Ubuntu if GEM native extensions
are required  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential wget
zlib1g-dev libssl-dev libreadline6-dev libyaml-dev  
RUN wget -q http://cache.ruby-lang.org/pub/ruby/ruby-2.3.1.tar.gz  
RUN tar -xvzf ruby-2.3.1.tar.gz  
RUN cd ruby-2.3.1 && ./configure --prefix=/usr/local && make && make install  
# cleanup  
RUN rm -rf ruby-2.3.1  
RUN rm ruby-2.3.1.tar.gz  
  
# NodeJS  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN apt-get update -qq && apt-get install -y nodejs libfontconfig  
  
# ------------------------------------------------------  
# --- Tools installed through Ruby gems, NPM, ...  
# PhantomJS  
RUN npm install -g phantomjs@1.9  
RUN gem install bundler --version "=1.10.0" \--no-document

