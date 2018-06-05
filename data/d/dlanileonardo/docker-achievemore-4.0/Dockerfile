#  
# Preparing Ruby/Rbenv Dockerfile  
#  
# https://github.com/dockerfile/ruby  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
MAINTAINER Odlanier Mendes <dlanileonardo@gmail.com>  
  
ENV HOME /azk  
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH  
ENV SHELL /bin/bash  
  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
RUN apt-get -y install \  
git-core \  
curl \  
zlib1g-dev \  
build-essential \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt1-dev \  
libcurl4-openssl-dev \  
python-software-properties \  
libmysqlclient-dev \  
libpq-dev \  
nodejs  
  
RUN git clone \--quiet --depth 1 https://github.com/sstephenson/rbenv.git \  
$HOME/.rbenv  
RUN git clone \--quiet --depth 1 https://github.com/sstephenson/ruby-build.git
\  
$HOME/.rbenv/plugins/ruby-build  
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.profile  
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc

