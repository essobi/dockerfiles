# Artifacts build container with fpm  
#  
# old ruby stuff  
# wget http://cache.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p481.tar.gz && \  
# tar -xvzf ruby-2.0.0-p481.tar.gz && \  
# cd ruby-2.0.0-p481/ && \  
#  
# VERSION 0.0.1  
FROM debian:jessie  
  
# Install curl & unzip  
RUN apt-get update && \  
apt-get install wget curl unzip --yes  
  
# Install Ruby 2.0  
# http://stackoverflow.com/questions/16222738/how-do-i-install-
ruby-2-0-0-correctly-on-ubuntu-12-04  
#
https://gist.githubusercontent.com/rubo77/ba9b64b160fe46e44aa1/raw/582178f14f7fd09bf1201ce8daaa71c2a26f5b03/Ubuntu-12.04-ruby2.0-install.sh  
#RUN wget -O - https://git.io/vvkI4 | bash  
RUN apt-get -y update && \  
apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev
libyaml-dev && \  
cd /tmp && \  
wget https://cache.ruby-lang.org/pub/ruby/2.5/ruby-2.5.1.tar.gz && \  
tar -xvzf ruby-2.5.1.tar.gz && \  
cd ruby-2.5.1/ && \  
./configure --prefix=/usr/local && \  
make && \  
make install  
  
# Lock the version of fpm  
# https://github.com/jordansissel/fpm/tree/v1.5.0  
# RUN gem install fpm -v 1.5.0  
RUN gem install fpm  
  
# build: contains the source/binary files that needs to be packaged up  
# packaging: contains config & meta files to create the debian package  
# output: will place the debian package here  
VOLUME ["/build", "/packaging", "/output"]  
  
# Add the entrypoint.sh  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN cd /usr/local/bin/ && \  
chmod ugo+x docker-entrypoint.sh  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["package"]

