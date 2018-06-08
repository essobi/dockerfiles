FROM prograils/ruby-node:latest  
MAINTAINER Maciej Litwiniuk <maciej@litwiniuk.net>  
  
# Install extra dependencies  
RUN apt-get -y install libicu55  
  
# Download phantomjs build (see README)  
RUN \  
cd /tmp && \  
git clone https://github.com/mlitwiniuk/phantomjs-build.git && \  
cd phantomjs-build && \  
cp bin/phantomjs /usr/local/bin/ && \  
cd /tmp && \  
rm -rf /tmp/phantomjs-build  
  

