FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get install -yq \  
bison \  
build-essential \  
curl \  
flex \  
g++ \  
git \  
gperf \  
sqlite3 \  
libsqlite3-dev \  
fontconfig \  
libfontconfig1 \  
libfontconfig1-dev \  
libfreetype6 \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libpng-dev \  
libssl-dev \  
libqt5webkit5-dev \  
ruby \  
perl \  
unzip \  
wget  
  
RUN git clone git://github.com/ariya/phantomjs.git  
RUN cd phantomjs \  
&& git checkout 2.0 \  
&& ./build.sh --confirm  
  
RUN cp /phantomjs/bin/phantomjs /usr/local/bin/phantomjs  
  
VOLUME ["/srv"]  
WORKDIR /srv  
  
ADD rasterize.js /rasterize.js  
  
ENTRYPOINT ["/phantomjs/bin/phantomjs", "--debug=true", "--ignore-ssl-
errors=yes", "--ssl-protocol=tlsv1", "/rasterize.js"]  

