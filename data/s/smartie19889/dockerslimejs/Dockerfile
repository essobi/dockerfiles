FROM buildpack-deps:jessie-curl  
  
MAINTAINER Steven Alexander "steven.william.alexander@googlemail.com"  
  
ENV PHANTOMJS_VERSION 1.9.0  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git-core build-essential g++ flex bison gperf ruby perl \  
libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \  
libgstreamermm-0.10-dev \  
libpng-dev libjpeg-dev python libx11-dev libxext-dev && \  
  
  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install PhantomJS  
RUN git clone https://bitbucket.org/smartie19889/dockerslimejs.git && \  
mv /dockerslimejs/phantomjs /bin && \  
chmod +x /bin/phantomjs && \  
rm -rf phantomjs

