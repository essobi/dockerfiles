FROM debian:jessie  
  
# Install Node.js and npm  
# make sure apt is up to date  
RUN apt-get update  
  
# install nodejs and npm  
RUN apt-get install -y nodejs npm git git-core  
  
# Install libraries  
RUN apt-get install -y libwebp5  
RUN apt-get install -y libjpeg62  
RUN apt-get install -y libfontconfig1  
  
RUN apt-get install -y wget  
RUN wget
http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.6_amd64.deb  
RUN dpkg -i libicu52_52.1-3ubuntu0.6_amd64.deb  
  
# Install app dependencies  
COPY package.json /fullslider_src/package.json  
RUN cd /fullslider_src; npm install --production  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Bundle app source  
COPY . /fullslider_src  
  
EXPOSE 8888  
CMD cd /fullslider_src; node init.js  

