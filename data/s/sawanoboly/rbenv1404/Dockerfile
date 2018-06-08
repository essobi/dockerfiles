# install rbenv from Official Ubuntu base image  
FROM ubuntu:14.04  
MAINTAINER SAWANOBORI Yukihiko <sawanoboriyu@higanworks.com>  
  
WORKDIR /root  
RUN apt-get -qq update  
RUN apt-get -qqy install git build-essential g++ gcc make libc6-dev patch
openssl ca-certificates libreadline6 libreadline6-dev curl zlib1g zlib1g-dev
libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev
libncurses5-dev automake libtool bison pkg-config libffi-dev subversion
libxml2-dev libxslt-dev  
RUN git clone https://github.com/sstephenson/rbenv.git .rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
.rbenv/plugins/ruby-build  
ENV HOME /root  
ENV PATH ~/.rbenv/shims:~/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' > ~/.bash_profile  

