FROM ubuntu:trusty  
MAINTAINER Andrew Malitski <andrew-writer@mail.ru>  
  
# Install phantomjs. See http://phantomjs.org/download.html  
ENV PHANTOMJS_NAME="phantomjs-2.1.1-linux-x86_64"  
RUN apt-get update -qq && apt-get install -y curl libfontconfig > /dev/null  
RUN cd /tmp && curl -s -o phantomjs.tar.bz2 -L
https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOMJS_NAME}.tar.bz2 && \  
tar xvjf phantomjs.tar.bz2 && mv ${PHANTOMJS_NAME}/bin/phantomjs
/usr/local/bin && \  
rm -rf ${PHANTOMJS_NAME} phantomjs.tar.bz2  
  
EXPOSE 8910  
CMD ["phantomjs", "--webdriver=8910"]  

