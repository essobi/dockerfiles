FROM ubuntu:16.04  
MAINTAINER ABL  
  
RUN apt-get update  
# Install Phantom.js  
RUN mkdir /tmp/phantomjs  
RUN cd /tmp/phantomjs  
RUN apt-get install curl build-essential -y  
RUN curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.5.0-beta-linux-
ubuntu-xenial-x86_64.tar.gz --output /tmp/phantomjs/phantomjs.tar.gz  
RUN tar zxf /tmp/phantomjs/phantomjs.tar.gz  
RUN mv phantomjs-2.5.0-beta-ubuntu-xenial/bin/phantomjs /usr/local/bin  
RUN chmod +x /usr/local/bin/phantomjs  
RUN apt-get install libfontconfig1-dev libjpeg-dev libxslt1-dev libhyphen-dev
-y  
  
# Install Node.js  
RUN curl -SLO "https://nodejs.org/dist/v7.10.0/node-v7.10.0-linux-x64.tar.xz"
\  
&& tar -xJf "node-v7.10.0-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Run as non-root user  
# RUN useradd --system --uid 72379 -m --shell /usr/sbin/nologin phantomjs  
# USER phantomjs  
EXPOSE 8910  
CMD ["/usr/local/bin/phantomjs"]  

