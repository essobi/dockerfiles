FROM qnib/d-consul  
  
  
RUN apt-get update \  
&& apt-get -y install build-essential g++ flex bison gperf ruby perl
libsqlite3-dev libfontconfig1-dev  
RUN apt-get -y install libicu-dev libfreetype6 libssl-dev libpng-dev libjpeg-
dev python libx11-dev libxext-dev git-core  
RUN echo \  
&& cd /tmp \  
&& git clone git://github.com/ariya/phantomjs.git \  
&& cd phantomjs \  
&& git checkout 2.1.1 \  
&& git submodule init \  
&& git submodule update \  
&& cd /tmp/phantomjs \  
&& python build.py --confirm \  
&& cd /root/ \  
&& cp /tmp/phantomjs/bin/phantomjs /usr/local/bin/ \  
&& apt-get -y purge build-essential g++ flex bison gperf libsqlite3-dev
libfontconfig1-dev libicu-dev libssl-dev libpng-dev libjpeg-dev libx11-dev
libxext-dev git-core \  
&& rm -rf /tmp/*  
RUN apt-get install -y imagemagick  
ENV SCREENSHOT_NAME=screen  
ADD opt/qnib/phantomjs/bin/screenshot.sh \  
opt/qnib/phantomjs/bin/take_screenshot.js \  
/opt/qnib/phantomjs/bin/  
ADD etc/supervisord.d/screenshot.ini /etc/supervisord.d/  

