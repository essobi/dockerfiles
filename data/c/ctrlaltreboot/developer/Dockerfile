# Base source, I prefer LTS  
FROM ubuntu:14.04  
  
MAINTAINER ostrev  
  
# Freshen  
RUN apt-get -y update  
  
RUN \  
apt-get install -yy \  
wget curl \  
git-core build-essential libcurl3 libcurl3-gnutls libcurl4-openssl-dev \  
libsqlite3-dev libpq-dev libmysqlclient-dev libyaml-dev openssl
libreadline6-dev \  
update-motd man-db ssh nano vim screen libxml2-dev libxslt1-dev upstart ntp
unzip \  
net-tools tmux openssh-server iputils-ping  

