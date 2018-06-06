FROM node  
  
# Set ENV  
ENV PHANTOMJS_VERSION 2.1.1  
# Commands  
RUN apt update && apt -y upgrade  
RUN apt install -y \  
libfreetype6 \  
libfontconfig  
  
RUN curl -OL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
bunzip2 phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
tar -xf phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar && \  
rm -f phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar && \  
mv phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/bin/ && \  
rm -rf /var/www/phantomjs-$PHANTOMJS_VERSION-linux-x86_64 && \  
phantomjs --version  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
RUN cd /usr/src/app && yarn install --production  
  
EXPOSE 3000  
CMD yarn start  

