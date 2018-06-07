FROM node:4.1.2  
MAINTAINER R Sloan "rnsloan1@gmail.com"  
ENV REFRESHED_AT 2015-10-22  
# Watchman  
RUN apt-get -yqq update; \  
apt-get -yqq install python-dev; \  
cd /tmp; \  
git clone https://github.com/facebook/watchman.git; \  
cd watchman; \  
git checkout v3.9.0; \  
./autogen.sh; \  
./configure; \  
make; \  
make install  
  
# phantomjs2  
RUN cd /tmp; \  
wget
https://github.com/danielra/phantomjs-2.0.0-linux-x86_64/raw/master/phantomjs-2.0.0-linux-x86_64.tar.bz2;
\  
tar xf phantomjs-2.0.0-linux-x86_64.tar.bz2; \  
cp phantomjs-2.0.0-linux-x86_64/bin/phantomjs /usr/local/bin/  
  
# ember-cli  
RUN npm i -g ember-cli  
  
WORKDIR /usr/src  
  
# just hints. Still have to bind these ports at runtime  
EXPOSE 4200 35729  

