FROM debian:jessie  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER muze-nl  
  
RUN sed -e 's@main$@main contrib non-free@' -i /etc/apt/sources.list  
  
# Commands  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y locales libfreetype6 libfontconfig libicu52 openssl ttf-
mscorefonts-installer xfonts-base libjpeg62 fonts-liberation && \  
apt-get --no-install-recommends install -y php5-cli curl npm nodejs-legacy
nodejs bzip2 git && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
RUN \  
npm -g install phantomjs-prebuilt  

