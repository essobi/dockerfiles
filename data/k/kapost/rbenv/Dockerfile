#FROM debian:latest  
FROM ubuntu:12.04  
MAINTAINER Kapost Engineering <noreply@kapost.com>  
  
ENV HOME /root  
# Add repositoroes and install dependencies  
RUN mkdir -p $HOME && \  
apt-get update  
RUN apt-get install -f -y git curl libcurl4-gnutls-dev wget build-essential
subversion autoconf libpq-dev libsqlite3-dev libmysqlclient-dev zlib1g-dev
libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev bison qt4-qmake
libqtwebkit-dev libffi-dev net-tools && \  
apt-get clean libcomerr2 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install rbenv and ruby-build  
RUN git clone https://github.com/sstephenson/rbenv.git $HOME/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
$HOME/.rbenv/plugins/ruby-build  
RUN $HOME/.rbenv/plugins/ruby-build/install.sh  
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc  

