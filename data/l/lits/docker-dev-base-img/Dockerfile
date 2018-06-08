FROM ruby:2.4.0  
MAINTAINER Kalyn Valentyn <valentyn.kalyn@litslink.com>  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# set UTF-8 locale  
RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen
en_US.UTF-8 en_us && dpkg-reconfigure locales && dpkg-reconfigure locales &&
locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# install some system libs  
RUN apt-get update -qq -y  
RUN apt-get install -qq -y \  
wget \  
sudo \  
git \  
curl \  
build-essential \  
imagemagick \  
libpq-dev \  
autoconf \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
zlib1g-dev \  
libbz2-dev  
  
# install npm  
RUN apt-get install -y npm  
#install and update nodejs  
RUN npm cache clean -f && npm install -g n && n 5.8.0  
  
RUN gem install rake  
  
RUN echo "deb http://security.ubuntu.com/ubuntu lucid-security main" >>
/etc/apt/sources.list  
RUN echo "deb http://cz.archive.ubuntu.com/ubuntu lucid main" >>
/etc/apt/sources.list  
  
RUN mkdir /var/app  
WORKDIR /var/app  

