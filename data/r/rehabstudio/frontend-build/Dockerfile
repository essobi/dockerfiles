FROM debian:wheezy  
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>  
  
# install apt dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-transport-https \  
build-essential \  
curl \  
git \  
inotify-tools \  
libfontconfig1 \  
libfreetype6 \  
libpng-dev \  
ruby \  
sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install Node stable and latest npm  
RUN curl -sL https://deb.nodesource.com/setup | bash - && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
npm install -g npm@latest-2  
  
# install global task runners and phantomjs  
RUN npm install -g grunt-cli gulp phantomjs webpack  
  
# install gulp sass requirements  
RUN gem install sass  
  
ADD assets/package.json /src/  
RUN cd /src && npm install  
  
VOLUME ['/src/node_modules']  
WORKDIR /src  

