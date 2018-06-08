FROM asux/rails:2.3  
MAINTAINER Alex Ulianytskyi <a.ulyanitsky@gmail.com>  
  
# Packages  
# ENV MAIN_PACKAGES  
# PhantomJS from https://github.com/fgrehm/docker-
phantomjs2/blob/master/Dockerfile.buildphantomjs  
# Dependencies we just need for building phantomjs  
# ENV BUILD_DEPENDENCIES\  
# wget tar gzip build-essential g++ flex bison gperf\  
# ruby perl libsqlite3-dev libssl-dev libpng-dev  
# Dependencies we need for running phantomjs  
ENV PHANTOM_JS_DEPENDENCIES\  
libicu-dev libfontconfig1-dev libjpeg-dev libfreetype6  
  
ENV PHANTOM_JS_TAG 2.1.1  
# Installing phantomjs  
# Installing dependencies  
RUN apt-get update  
RUN apt-get install -fyq ${PHANTOM_JS_DEPENDENCIES}  
  
# Downloading bin, unzipping & removing zip  
WORKDIR /tmp  
RUN wget -q
http://cnpmjs.org/mirrors/phantomjs/phantomjs-${PHANTOM_JS_TAG}-linux-x86_64.tar.bz2
-O phantomjs.tar.bz2 \  
&& tar xjf phantomjs.tar.bz2 \  
&& rm -rf phantomjs.tar.bz2 \  
&& mv phantomjs-* phantomjs \  
&& mv /tmp/phantomjs/bin/phantomjs /usr/local/bin/phantomjs  
  
RUN echo "phantomjs binary is located at `which phantomjs`" \  
&& echo "just run 'phantomjs' (version `phantomjs -v`)"  
  
# Removing build dependencies, clean temporary files  
# RUN apt-get purge -yq ${BUILD_DEPENDENCIES}  
# Make sure required packages installed  
RUN apt-get install -yq ${PHANTOM_JS_DEPENDENCIES}  
RUN apt-get autoremove -yq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rails --version  
RUN puma --version  
RUN phantomjs -v  
  
WORKDIR /usr/src/app  

