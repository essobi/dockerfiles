FROM debian:jessie  
MAINTAINER Alessandro Bologna <alessandro.bologna@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq \  
&& apt-get -yqq install build-essential g++ flex bison gperf ruby perl
libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 \  
libssl-dev libpng-dev libjpeg-dev python libx11-dev libxext-dev git  
  
RUN cd /tmp && git clone git://github.com/ariya/phantomjs.git \  
&& cd phantomjs \  
&& git checkout 2.0 \  
&& cd /tmp/phantomjs && ./build.sh --jobs 1 --confirm --silent \  
&& cp /tmp/phantomjs/bin/phantomjs /usr/local/bin/phantomjs \  
&& rm -rf /tmp/phantomjs \  
&& apt-get purge -yqq build-essential g++ flex bison gperf ruby perl
libsqlite3-dev libssl-dev libpng-dev \  
&& apt-get autoremove -yqq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD phantom-render.js /app/  
EXPOSE 80  
ENTRYPOINT ["/usr/local/bin/phantomjs","/app/phantom-render.js","80"]  
  

