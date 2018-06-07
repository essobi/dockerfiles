# dockerhub - A repository for various dockerfiles  
# For more information; http://github.com/cmfatih/dockerhub  
#  
# phantomjs  
#  
# Usage  
# sudo docker run fentas/phantomjs /usr/bin/phantomjs -v  
# sudo docker run fentas/phantomjs /usr/bin/casperjs --version  
# sudo docker run -v `pwd`:/mnt/test fentas/phantomjs /usr/bin/phantomjs
/mnt/test/test.js  
# VERSION 1.0.1  
  
FROM ubuntu:14.04  
  
MAINTAINER fentas <jan.guth.so>  
  
# Env  
ENV PHANTOMJS_VERSION master  
ENV CASPERJS_VERSION master  
  
# Commands  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 \  
build-essential g++ flex bison gperf ruby perl \  
libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \  
libpng-dev libjpeg-dev python && \  
mkdir -p /srv/var && \  
git clone https://github.com/ariya/phantomjs.git /tmp/phantomjs && \  
cd /tmp/phantomjs && git checkout $PHANTOMJS_VERSION && \  
./build.sh --silent --confirm && \  
mv ./bin/phantomjs /usr/bin && \  
cd /tmp && rm -R ./phantomjs && \  
git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
cd /srv/var/casperjs && \  
git checkout $CASPERJS_VERSION && \  
ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  
# Default command  
ENTRYPOINT "phantomjs"  
CMD ["--help"]  

