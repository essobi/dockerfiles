FROM ubuntu:14.04  
MAINTAINER ngot "https://github.com/ngot"  
RUN apt-get update  
RUN apt-get install -y curl g++ make cmake git xz-utils  
  
ENV FIBJS_VERSION 0.3.0  
ENV NODE_VERSION 6.10.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz"  
RUN tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1  
RUN rm -f "node-v$NODE_VERSION-linux-x64.tar.xz"  
RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Install fibjs  
RUN curl -SL
"https://github.com/fibjs/fibjs/releases/download/v$FIBJS_VERSION/installer-
linux-x64.sh" -o installer.sh  
RUN sudo sh installer.sh  

