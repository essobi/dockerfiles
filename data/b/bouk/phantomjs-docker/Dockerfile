FROM golang:1.4.1  
  
RUN \  
echo "deb http://http.debian.net/debian jessie contrib" >>
/etc/apt/sources.list && \  
apt-get update && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
apt-get install -y -q g++ flex bison gperf ruby perl \  
libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \  
libpng-dev libjpeg-dev ttf-mscorefonts-installer  
  
RUN \  
cd / && \  
git clone git://github.com/ariya/phantomjs.git && \  
cd phantomjs && \  
./build.sh \--confirm && \  
mv /phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
rm -rf /phantomjs  

