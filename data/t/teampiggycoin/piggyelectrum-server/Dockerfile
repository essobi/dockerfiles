#BUILDS teampiggycoin/piggyelectrum-server  
FROM qlustor/alpine-runit  
MAINTAINER Team PiggyCoin <team@piggy-coin.com>  
  
# Install Python 2.x  
RUN apk-install --update python python-dev py-pip \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& apk-install py-setuptools \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk-install leveldb-dev \  
&& apk-install build-base git \  
&& pip install --no-cache-dir --upgrade pip jsonrpclib irc plyvel leveldb
x11_hash \  
&& git clone https://github.com/TeamPiggyCoin/PiggyElectrum-Server.git
/electrum \  
&& cd /electrum \  
&& python setup.py install \  
&& apk del build-base git \  
&& adduser -D -g "" electrum  
ADD . /  
  
EXPOSE 5001 5002 8000  
VOLUME /home/electrum  
ENTRYPOINT ["/sbin/runit-docker"]  

