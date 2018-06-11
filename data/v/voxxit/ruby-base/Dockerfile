FROM ubuntu:latest  
  
ENV RUBY_MAJOR_VERSION "2.2"  
ENV RUBY_VERSION "2.2.2"  
ENV NODE_VERSION "v0.12.7"  
  
WORKDIR /usr/local/src  
  
# 1. Update apt repositories  
# 2. Upgrade any outdated system components  
# 3. Install build dependencies for Ruby  
# 4. Install Ruby  
# 5. Install node.js (JS runtime for Ruby)  
# 6. Clean up source code & apt repository caches  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
build-essential \  
git-core \  
curl \  
libcurl4-openssl-dev \  
libsqlite3-dev \  
libmysqlclient18 \  
libpq5 \  
libffi-dev \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
python-software-properties \  
zlib1g-dev \  
&& curl http://ftp.ruby-
lang.org/pub/ruby/$RUBY_MAJOR_VERSION/ruby-$RUBY_VERSION.tar.gz | tar -xz \  
&& cd ruby-$RUBY_VERSION \  
&& ./configure \  
&& make \  
&& make install \  
&& gem install bundler --no-ri --no-rdoc \  
&& curl https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION.tar.gz | tar
-xz \  
&& cd node-$NODE_VERSION \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /usr/local/src/* /var/apt/lists/*  

