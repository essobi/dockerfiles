FROM ruby:2.4-stretch  
MAINTAINER Campus Code <dev@campuscode.com.br>  
  
ENV NODE_VERSION 7  
RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION.x | bash -  
  
RUN apt-get update -qq  
RUN apt-get install -y --no-install-recommends nodejs \  
locales \  
qt5-default \  
libqt5webkit5-dev \  
gstreamer1.0-plugins-base \  
gstreamer1.0-tools \  
gstreamer1.0-x \  
xvfb  
  
ENV PHANTOMJS_VERSION 2.1.1  
RUN curl -L -O
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2  
RUN tar -jxvf phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs  
RUN mv phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/local/bin/  
RUN rm phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && rm -rf
phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin  
RUN chmod 755 /usr/local/bin/phantomjs  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN locale-gen  
ENV LC_ALL en_US.utf8  
  
RUN gem install bundler-audit  

