FROM ruby:2.1  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 4.4.4  
ENV PHANTOMJS_VERSION 1.9.8  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for nokogiri  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# for capybara-webkit  
RUN apt-get install -y qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base
gstreamer1.0-tools gstreamer1.0-x xvfb  
  
ADD phantomjs /usr/bin/phantomjs  
RUN chmod +x /usr/bin/phantomjs  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.3/install.sh | bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& npm install -g npm-cache  
  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  

