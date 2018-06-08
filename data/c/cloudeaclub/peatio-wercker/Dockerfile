FROM ruby:2.2.1  
ENV PHANTOMJS_VERSION 2.1.1  
RUN apt-get update \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -qO /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
https://s3-ap-northeast-1.amazonaws.com/dev.re-
work.io/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2  
RUN tar jxf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp  
RUN mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
RUN rm -rf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
/tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64  

