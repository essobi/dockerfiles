FROM debian:jessie  
MAINTAINER Jan Mitoraj <jan@ifsm.eu>  
ENV w_directory /home/runner  
  
# valid from Docker 1.12  
#SHELL ["/bin/bash","-c"]  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y sudo curl git-core curl nodejs zlib1g-dev build-
essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev libxml2-dev
libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev mysql-
client postgresql-client libmysqlclient-dev libpq-dev libmagickwand-dev
imagemagick  
RUN adduser --system runner  
RUN echo "runner ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/runner  
USER runner  
WORKDIR $w_directory  
RUN git clone https://github.com/sstephenson/rbenv.git .rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
.rbenv/plugins/ruby-build  
RUN sudo ${w_directory}/.rbenv/plugins/ruby-build/install.sh  
ENV PATH ${w_directory}/.rbenv/bin:$PATH  
ENV CONFIGURE_OPTS --disable-install-doc  
RUN echo 'gem: --no-rdoc --no-ri --no-document' >> .gemrc  
USER root  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
USER runner  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
RUN rbenv install -v 2.0.0-p648  
RUN rbenv install -v 2.1.5  
RUN rbenv install -v 2.2.0  
RUN rbenv install -v 2.2.4  
RUN rbenv install -v 2.3.1  
RUN rbenv install -v 2.4.0  
RUN rbenv install -v 2.5.0  
RUN rbenv install -v 2.5.1  
ENV PATH ${w_directory}/.rbenv/shims:$PATH  
ENV RBENV_VERSION 2.0.0-p648  
RUN gem install bundler  
ENV RBENV_VERSION 2.1.5  
RUN gem install bundler  
ENV RBENV_VERSION 2.2.0  
RUN gem install bundler  
ENV RBENV_VERSION 2.2.4  
RUN gem install bundler  
ENV RBENV_VERSION 2.3.1  
RUN gem install bundler  
ENV RBENV_VERSION 2.4.0  
RUN gem install bundler  
ENV RBENV_VERSION 2.5.0  
RUN gem install bundler  
ENV RBENV_VERSION 2.5.1  
RUN gem install bundler  
RUN ruby --version  
RUN export APT_CACHE_DIR=`pwd`/apt-cache && mkdir -pv $APT_CACHE_DIR  

