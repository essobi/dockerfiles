FROM ubuntu:xenial  
  
RUN apt-get update  
  
RUN apt-get --assume-yes install python-pygments  
  
ENV HUGO_VERSION 0.19  
ENV HUGO_BINARY hugo_${HUGO_VERSION}-64bit.deb  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN dpkg -i /tmp/hugo.deb && rm /tmp/hugo.deb  
  
RUN apt-get --assume-yes install ruby-sass  
  
RUN apt-get --assume-yes install nodejs-legacy npm  
RUN npm install -g elm  

