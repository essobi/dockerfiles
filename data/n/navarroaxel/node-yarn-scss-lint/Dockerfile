FROM node:6  
MAINTAINER navarroaxel <navarroaxel@gmail.com>  
  
LABEL Description="Node LTS with yarn and ruby installed for scss_lint"  
  
# Repo for Yarn  
RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install -y \  
curl \  
libxml2-dev \  
libxslt-dev \  
libcurl4-openssl-dev \  
libreadline6-dev \  
libssl-dev \  
patch \  
build-essential \  
zlib1g-dev \  
openssh-server \  
libyaml-dev \  
libicu-dev \  
rsync \  
libmysqlclient-dev \  
yarn \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Ruby installation  
RUN mkdir /tmp/ruby  
RUN cd /tmp/ruby && curl --silent ftp://ftp.ruby-
lang.org/pub/ruby/2.4/ruby-2.4.0.tar.gz | tar xz  
RUN cd /tmp/ruby/ruby-2.4.0 && ./configure --disable-install-rdoc && make
install  
  
RUN gem install scss_lint  

