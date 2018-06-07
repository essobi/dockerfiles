from golang:1.6  
MAINTAINER tyler@disruptiveart.com  
  
  
# Install libraries need for packaging  
RUN apt-get update  
RUN apt-get install -y bzip2 makeself  
  
# Install Node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# Install Gulp  
RUN npm install -g gulp@3.9.0 bower@1.3.12 jshint@2.9.2 karma phantomjs  
  
# Install remaining npm  
RUN npm install -g graceful-fs babel-core@6.3.26 babel-preset-es2015@6.3.13
babelify@7.2.0 \  
brfs@1.2.0 browserify@12.0.0 browser-sync@2.7.6 imagemin-pngcrush@4.1.0 gulp-
sass@2.0.4 \  
pngcrush-bin@3.0.0 marked@0.3.6 node-gyp@3.4.0  
  
# Install go dependencies  
RUN go get github.com/smartystreets/goconvey  
  
# Install phantomJS dependency  
RUN apt-get install -y libfontconfig  

