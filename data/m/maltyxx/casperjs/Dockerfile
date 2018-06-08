FROM node:6.11  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
ENV CASPERJS_VERSION 1.1.4  
ENV PHANTOMJS_VERSION 2.1.16  
RUN npm -g install phantomjs-prebuilt@"$PHANTOMJS_VERSION"
casperjs@"$CASPERJS_VERSION" \  
&& npm cache clean  

