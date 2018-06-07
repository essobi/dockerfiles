FROM ruby:2.3.1  
  
RUN apt-get update -yqq && apt-get install -y build-essential g++  
  
# Install postgres nokogiri and sprokets dependencies  
RUN apt-get install -y libpq-dev \  
libxml2-dev libxslt1-dev \  
nodejs  
  
# Install phantomjs dependencies  
RUN apt-get install -y libfreetype6 libfontconfig bzip2 wget  
  
# Install phantomjs 1.9.8  
RUN mkdir -p /srv/var  
RUN wget -q -O /tmp/phantomjs-1.9.8-linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN tar -xjf /tmp/phantomjs-1.9.8-linux-x86_64.tar.bz2 -C /tmp  
RUN rm -f /tmp/phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN mv /tmp/phantomjs-1.9.8-linux-x86_64/ /srv/var/phantomjs  
RUN ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs  
RUN apt-get autoremove -y && apt-get clean all  
  
# # Dependencies we just need for building phantomjs  
# ENV buildDependencies\  
# wget unzip python build-essential g++ flex bison gperf\  
# perl libsqlite3-dev libssl-dev libpng-dev  
#  
# # Dependencies we need for running phantomjs  
# ENV phantomJSDependencies\  
# libicu-dev libfontconfig1-dev libjpeg-dev libfreetype6  
#  
# # Installing phantomjs  
# RUN \  
# # Installing dependencies  
# apt-get install -fyqq ${buildDependencies} ${phantomJSDependencies}\  
# # Downloading src, unzipping & removing zip  
# && mkdir phantomjs \  
# && cd phantomjs \  
# && wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.0.0-source.zip \  
# && unzip phantomjs-2.0.0-source.zip \  
# && rm -rf /phantomjs/phantomjs-2.0.0-source.zip \  
# # Building phantom  
# && cd phantomjs-2.0.0/ \  
# && ./build.sh --confirm --silent \  
# # Removing everything but the binary  
# && ls -A | grep -v bin | xargs rm -rf \  
# # Symlink phantom so that we are able to run `phantomjs`  
# && ln -s /phantomjs/phantomjs-2.0.0/bin/phantomjs /usr/local/share/phantomjs
\  
# && ln -s /phantomjs/phantomjs-2.0.0/bin/phantomjs /usr/local/bin/phantomjs \  
# && ln -s /phantomjs/phantomjs-2.0.0/bin/phantomjs /usr/bin/phantomjs \  
# # Removing build dependencies, clean temporary files  
# && apt-get purge -yqq ${buildDependencies} \  
# && apt-get autoremove -yqq \  
# && apt-get clean \  
# && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
# # Checking if phantom works  
# && phantomjs -v  

