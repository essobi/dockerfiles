FROM ubuntu:15.10  
MAINTAINER Hao Sun <xsunsmile@gmail.com>  
  
# Enable the universe package repository.  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
  
# Install build dependencies. Note that python is required to build Node.  
RUN apt-get -y update  
RUN apt-get install -y --no-install-recommends \  
autoconf \  
bison \  
build-essential \  
ca-certificates \  
curl \  
git-core \  
git \  
libcurl4-openssl-dev \  
libffi-dev \  
libgdbm3 \  
libgdbm-dev \  
libreadline-dev \  
libncurses5-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
python \  
redis-server \  
vim \  
iputils-ping \  
python-software-properties \  
sqlite3 \  
zlib1g-dev  
  
# install rbenv ruby-build  
# install nodenv node-build  
RUN git clone git://github.com/sstephenson/rbenv.git /root/.rbenv && \  
git clone git://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build && \  
git clone git://github.com/sstephenson/rbenv-gem-rehash.git
/root/.rbenv/plugins/rbenv-gem-rehash && \  
git clone git://github.com/OiNutter/nodenv.git /root/.nodenv && \  
git clone git://github.com/OiNutter/node-build.git /root/.nodenv/plugins/node-
build  
ENV PATH
/root/.rbenv/shims:/root/.rbenv/bin:/root/.nodenv/shims:/root/.nodenv/bin:$PATH  
  
# application  
ENV APP /app  
RUN mkdir $APP  
WORKDIR $APP  
  
ADD src ${APP}/src  
ADD public ${APP}/public  
  
ADD .node-version $APP/  
ADD package.json $APP/  
ADD .babelrc $APP/  
ADD webpack.config.babel.js $APP/  
  
ADD .ruby-version $APP/  
ADD Gemfile $APP/  
ADD Gemfile.lock $APP/  
ADD config.ru $APP/  
ADD debug-docker.sh $APP/  
  
RUN rbenv install && \  
gem install bundler && \  
nodenv install && \  
nodenv rehash  
  
RUN bundle  
RUN npm install  
RUN npm run compile  
CMD /bin/sh debug-docker.sh  

