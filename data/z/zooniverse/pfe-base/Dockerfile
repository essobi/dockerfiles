FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /src  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y curl libfreetype6 libfontconfig1 git g++ flex bison \  
gperf ruby perl libsqlite3-dev libfontconfig1-dev libicu-dev \  
libssl-dev libpng-dev libjpeg-dev build-essential python unzip && \  
curl https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs && \  
apt-get clean && \  
git clone git://github.com/ariya/phantomjs.git && \  
cd phantomjs && \  
git checkout 2.0 && \  
cd /src/phantomjs && ./build.sh \--confirm && \  
mv bin/phantomjs /usr/bin/ && cd .. && rm -rf phantomjs  

