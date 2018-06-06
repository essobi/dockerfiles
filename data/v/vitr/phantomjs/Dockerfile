# PhantomJS  
# http://phantomjs.org/  
#  
# Usage  
# 'hello world' and version check (default script)  
# docker run --rm vitr/phantomjs  
# mount your own script  
# docker run --rm -v `pwd`/myscript.js:/home/phantomjs/script.js
vitr/phantomjs  
FROM debian:jessie  
MAINTAINER vitr http://vit.online  
  
ENV PHANTOMJS_VERSION=phantomjs-2.1.1-linux-x86_64  
ENV PHANTOMJS_DIR=/home/phantomjs  
  
RUN apt-get update -y  
RUN apt-get install -y libfreetype6-dev libfontconfig1-dev wget bzip2  
  
RUN wget --no-check-certificate
https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOMJS_VERSION.tar.bz2  
RUN tar xvf ${PHANTOMJS_VERSION}.tar.bz2  
RUN mv $PHANTOMJS_VERSION/bin/phantomjs /usr/local/bin/  
RUN rm -rf phantom*  
  
RUN mkdir -p $PHANTOMJS_DIR  
RUN echo '"use strict"; \n\  
console.log("Hello, world!"); + \n\  
console.log("using PhantomJS version " + \n\  
phantom.version.major + "." + \n\  
phantom.version.minor + "." + \n\  
phantom.version.patch); \n\  
phantom.exit();' \  
> ${PHANTOMJS_DIR}/script.js  
  
WORKDIR $PHANTOMJS_DIR  
  
ENTRYPOINT ["phantomjs", "script.js"]  

