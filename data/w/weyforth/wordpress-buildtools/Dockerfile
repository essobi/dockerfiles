FROM weyforth/wordpress-base  
  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y curl git && \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs make ruby ruby-dev && \  
apt-get remove --purge curl -y && \  
apt-get clean  
  
RUN npm config set registry http://registry.npmjs.org/ && \  
npm install -g --no-optional bower@1.4.1 && \  
npm install -g --no-optional gulp@3.8.11 && \  
npm install -g --no-optional gulp-size@1.2.1 && \  
npm install -g --no-optional gulp-copy@0.0.2 && \  
npm install -g --no-optional gulp-bower@0.0.10 && \  
npm install -g --no-optional gulp-minify-css@1.2.0 && \  
npm install -g --no-optional gulp-uglify@1.2.0 && \  
npm install -g --no-optional gulp-jshint@1.11.2 && \  
npm install -g --no-optional jshint-stylish@2.0.1 && \  
npm install -g --no-optional gulp-compass@2.1.0 && \  
npm install -g --no-optional gulp-requirejs-optimize@0.1.3 && \  
npm install -g --no-optional gulp-modulizr@0.0.2  
  
RUN gem install compass -v 1.0.3  
  
WORKDIR /data/www  

